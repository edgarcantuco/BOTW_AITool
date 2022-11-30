from inspect import getmodule
import yaml
import configparser
import os

def CreateBaiprog(FileName, Roots, DemoActions = None, Queries = None):

    AIs = []
    Actions = []
    Behaviors = []

    def __GetChilds(Definition):
        if hasattr(Definition, "ChildNames"):
            for ChildId in range(len(Definition.ChildNames)):
                Child = getattr(Definition, f"Child{ChildId}")
                DefinitionType = getmodule(Child).__name__.replace("Classes.", "")

                if Child.Parent == None:
                    Child.Parent = Definition
                elif Child.Parent != None and Child.Parent != "Multiple":
                    Child.Parent = "Multiple"

                if not Child in AIs and not Child in Actions:
                    if DefinitionType == "AI":
                        AIs.append(Child)
                    else:
                        Actions.append(Child)

                    __GetChilds(Child)

        if Definition.Behaviors != None:
            for BehaviorId, Behavior in Definition.Behaviors.items():
                if not Behavior in Behaviors:
                    Behaviors.append(Behavior)

    # __GetChilds(Root)

    for Root in Roots:
        AIs.append(Root)
        __GetChilds(Root)

    if DemoActions != None:
        for DemoAction in DemoActions:
            Actions.append(DemoAction)

    AbsoluteId = 0

    for AI in AIs:
        AI.AbsoluteId = AbsoluteId
        AbsoluteId += 1
        AI.RelativeId = AIs.index(AI)

    for Action in Actions:
        Action.AbsoluteId = AbsoluteId
        AbsoluteId += 1
        Action.RelativeId = Actions.index(Action)

    for Behavior in Behaviors:
        Behavior.AbsoluteId = AbsoluteId
        AbsoluteId += 1
        Behavior.RelativeId = Behaviors.index(Behavior)

    for Query in Queries:
        Query.RelativeId = Queries.index(Query)

    BaiprogData = {"AI": AIs, "Action": Actions, "Behavior": Behaviors, "Query": Queries}

    Baiprog = "!io\nversion: 0\ntype: xml\nparam_root: !list\n  objects:\n    DemoAIActionIdx: !obj\n"

    DemoAIActions = {}

    for AI in AIs:
        if AI.DemoAIAction: DemoAIActions[AI.Name] = AI.AbsoluteId

    for Action in Actions:
        if Action.DemoAIAction: DemoAIActions[Action.Name] = Action.AbsoluteId

    sorted_DemoAIActions = sorted(DemoAIActions.keys(), key=lambda x:x.lower())

    for sorted_Action in sorted_DemoAIActions:
        Baiprog += f"      {sorted_Action}: {DemoAIActions[sorted_Action]}\n"

    Baiprog += "  lists:\n"

    for AIDefType in BaiprogData:

        typeString = f"    {AIDefType}: !list\n      objects: {{}}\n      lists:"

        AIDef = BaiprogData[AIDefType]

        if AIDef == None or len(AIDef) == 0:
            typeString += f" {{}}\n"
        else:
            typeString += f"\n"

            for Node in AIDef:
                typeString += f"        {AIDefType}_{Node.RelativeId}: !list\n"
                typeString += f"          objects:\n"
                typeString += f"            Def: !obj\n"


                if AIDefType == "AI" or AIDefType == "Action": 
                    typeString += f"              Name: {Node.Name}\n"

                typeString += f"              ClassName: !str32 {type(Node).__name__}\n"

                if AIDefType == "AI" or AIDefType == "Action":
                    typeString += f"              GroupName: "
                    if Node.Parent != None and Node.Parent != "Multiple":
                        typeString += f"{Node.Parent.Name}\n"
                    else:
                        typeString += f"''\n"

                childList = {}
                childNames = []
                SInst = {}

                if hasattr(Node, "ChildNames"):
                    childNames = getattr(Node, "ChildNames")

                ForgivenParameters = ["Name", "DemoAIAction", "Behaviors", "Parent", "AbsoluteId", "RelativeId"]

                for Parameter in vars(Node):
                    if Parameter in ForgivenParameters: continue
                    
                    if "Child" in Parameter and Parameter != "ChildNames":
                        try:
                            childList[childNames[int(Parameter.replace("Child", ""))]] = vars(Node)[Parameter]
                        except Exception as e:
                            pass
                    else:
                        SInst[Parameter] = str(vars(Node)[Parameter]).replace("False", "false").replace("True", "true")

                if len(childList) > 0:

                    typeString += f"            ChildIdx: !obj\n"

                    for Child in childList:
                        typeString += f"              {Child}: {childList[Child].AbsoluteId}\n"

                if len(SInst) > 0:

                    typeString += f"            SInst: !obj\n"

                    for Param in SInst:
                        Value = SInst[Param]

                        if "[" in Value and "]" in Value and Value.count(",") == 2:
                            Value = "!vec3 " + Value

                        if Value != "":
                            typeString += f"              {Param}: {Value}\n"
                        else:
                            typeString += f"              {Param}: ''\n"
                    
                if hasattr(Node, "Behaviors") and Node.Behaviors != None and len(Node.Behaviors) > 0:

                    typeString += f"            BehaviorIdx: !obj\n"

                    for Behavior in Node.Behaviors:
                        typeString += f"              {Behavior}: {Node.Behaviors[Behavior].RelativeId}\n"

                typeString += f"          lists: {{}}\n"

        Baiprog += typeString

    with open(f"{FileName}.baiprog.yml", "w", encoding="utf-8") as f:
        f.write(Baiprog)
        f.close()

    splitName = FileName
    if(len(splitName.split("\\")) > 1):
        splitName = FileName.split("\\")[-1]

    if(len(splitName.split("/")) > 1):
        splitName = FileName.split("/")[-1]

    print(f"Created {splitName}.baiprog.yml")

class AIDefinition:

    def __init__(self, Dict, RelativeId, Prefix):
        self.Dict = Dict
        self.Children = []
        self.Parents = []
        self.RelativeId = RelativeId
        self.AbsoluteId = -1
        self.VariableName = ""
        self.Prefix = Prefix
        self.DemoAction = False
        self.AlreadyAdded = False


from googletrans import Translator
    
def GetCode(Src, Dst, TranslateNames, TranslateChildren):

    splitSrc = Src
    if(len(splitSrc.split("\\")) > 1):
        splitSrc = splitSrc.split("\\")[-1]

    if(len(splitSrc.split("/")) > 1):
        splitSrc = splitSrc.split("/")[-1]

    splitDst = Dst
    if(len(splitDst.split("\\")) > 1):
        splitDst = splitDst.split("\\")[-1]

    if(len(splitDst.split("/")) > 1):
        splitDst = splitDst.split("/")[-1]

    print(f"Extracting {splitSrc} into {splitDst}.py")

    translator = Translator()

    with open(Src, "r", encoding = "utf-8") as f:
        baiprog = f.read().replace(" !list", "").replace(" !obj", "").replace("!io", "").replace(" !str32", "").replace(" !vec3", "")
        f.close()

    baiprog = yaml.safe_load(baiprog)["param_root"]

    DemoActions = baiprog["objects"]["DemoAIActionIdx"]

    baiprog = baiprog["lists"]

    Definitions = {}

    for DefType in baiprog:
        
        DefList = []
        DefCount = 0
        Prefix = ""

        if DefType == "AI": Prefix = "AI"
        if DefType == "Action": Prefix = "Act"
        if DefType == "Behavior": Prefix = "B"
        if DefType == "Query": Prefix = "Q"

        for Def in baiprog[DefType]["lists"]:
            DefList.append(AIDefinition(baiprog[DefType]["lists"][Def]["objects"], DefCount, Prefix))
            DefCount += 1

        Definitions[DefType]= DefList

    AllDefinitions = []
    DefCount = 0

    for DefType in Definitions:
        for Def in Definitions[DefType]:
            Def.AbsoluteId = DefCount
            DefCount += 1
            AllDefinitions.append(Def)

    for DemoAction in DemoActions:
        AllDefinitions[DemoActions[DemoAction]].DemoAction = True

    for DefType in Definitions:
        for Def in Definitions[DefType]:
            if "ChildIdx" in Def.Dict:
                for Child in Def.Dict["ChildIdx"]:
                    Def.Children.append(AllDefinitions[Def.Dict["ChildIdx"][Child]])
                    AllDefinitions[Def.Dict["ChildIdx"][Child]].Parents.append(Def)

    PossibleRoots = []

    for Def in Definitions["AI"]:
        if len(Def.Parents) == 0 and len(Def.Children) > 0: PossibleRoots.append(Def)

    VariablesCreated = []

    Ident = "\t"

    def GetVariableName(Def):
        ClassName = Def.Dict['Def']['ClassName']
        Prefix = Def.Prefix
        attempt = 0
        while f"{Prefix}_{ClassName}_{attempt}" in VariablesCreated: attempt += 1
        Def.VariableName = f"{Prefix}_{ClassName}_{attempt}"
        VariablesCreated.append(f"{Prefix}_{ClassName}_{attempt}")
        
        return f"{Prefix}_{ClassName}_{attempt}"

    def VariableDefinition(Def, NIdent):
        StringToSave = ""
        Def.AlreadyAdded = True
        DefDict = Def.Dict
        ClassName = DefDict["Def"]["ClassName"]
        Empty = "\'\'"

        StringToSave += f"{ClassName}("

        if not ("SInst" in DefDict or "BehaviorsIdx" in DefDict or "ChildIdx" in DefDict or "Name" in DefDict["Def"]):
            StringToSave += ")"
        else:
            StringToSave += "\n"

            if "Name" in DefDict["Def"]:
                StringToSave += f"{Ident * (NIdent + 1)}Name = \"{DefDict['Def']['Name']}\""

                translation = translator.translate(DefDict['Def']['Name'])

                if (TranslateNames and translation.src == "ja" or translation.src == "zh-CN") and translation.origin != translation.text:
                    StringToSave += f", ## Translation => {translation.text}\n "
                else:
                    StringToSave += ",\n "
                
                if not (Def.DemoAction or "BehaviorIdx" in DefDict or "ChildIdx" in DefDict or "SInst" in DefDict):
                    StringToSave = StringToSave[:-2]
                    StringToSave += "\n"

            if Def.DemoAction:
                StringToSave += f"{Ident * (NIdent + 1)}DemoAIAction = \"True\",\n"

                if not ("BehaviorIdx" in DefDict or "ChildIdx" in DefDict or "SInst" in DefDict):
                    StringToSave = StringToSave[:-2]
                    StringToSave += "\n"

            if "BehaviorIdx" in DefDict:
                StringToSave += f"{Ident * (NIdent + 1)}Behaviors = {{"

                for Behavior in DefDict["BehaviorIdx"]:
                    StringToSave += f"\"{Behavior}\": {Definitions['Behavior'][DefDict['BehaviorIdx'][Behavior]].VariableName}, "

                StringToSave = StringToSave[:-2]
                StringToSave += "},\n"

            if "SInst" in DefDict:
                for Param in DefDict["SInst"]:
                    Value = str(DefDict['SInst'][Param]).replace('false', 'False')

                    if Value == "":
                        Value == Empty

                    StringToSave += f"{Ident * (NIdent + 1)}{Param} = \"{Value}\",\n"

                if not ("ChildIdx" in DefDict):
                    StringToSave = StringToSave[:-2]
                    StringToSave += "\n"

            if "ChildIdx" in DefDict:
                ChildNumber = 0
                StringToSave += "\n"
                for Child in DefDict["ChildIdx"]:

                    StringToSave += f"{Ident * (NIdent + 1)}## {Child}"

                    if(TranslateChildren):
                        translatedChild = translator.translate(Child)

                        if (translatedChild.src == "ja" or translatedChild.src == "zh-CN") and translatedChild.origin != translatedChild.text:
                            StringToSave += f" - Translation => {translatedChild.text}"

                    StringToSave += f"\n"

                    StringToSave += f"{Ident * (NIdent + 1)}Child{ChildNumber} = "

                    if Def.Children[ChildNumber].VariableName != "":
                        StringToSave += f"{Def.Children[ChildNumber].VariableName},\n"
                    else:
                        StringToSave += f"{VariableDefinition(Def.Children[ChildNumber], NIdent + 1)},\n"
                    ChildNumber += 1

                StringToSave = StringToSave[:-2]
                StringToSave += "\n"

            # StringToSave = StringToSave[:-1]
            StringToSave += f"{Ident * (NIdent)})"

        return StringToSave


    PythonFile = "from Classes.Action import *\nfrom Classes.AI import *\nfrom Classes.Behavior import *\nfrom Classes.Query import *\n\nimport AICreator\n\n"

    if len(Definitions["Behavior"]) > 0:
        PythonFile += "#### Behaviors ####\n\n"

        for Behavior in Definitions["Behavior"]:
            PythonFile += f"{GetVariableName(Behavior)} = {VariableDefinition(Behavior, 0)}\n\n"

        AddGeneralActions = False

        for Action in Definitions["Action"]:
            if len(Action.Parents) > 1:
                AddGeneralActions = True
                break

        if AddGeneralActions:

            PythonFile += "#### General Actions ####\n\n"

            for Action in Definitions["Action"]:
                if len(Action.Parents) > 1:
                    PythonFile += f"{GetVariableName(Action)} = {VariableDefinition(Action, 0)}\n\n"

        PythonFile += f"#### Baiprog Content ####\n\n"

        Roots = []

        for PossibleRoot in PossibleRoots:
            PythonFile += f"{GetVariableName(PossibleRoot)} = {VariableDefinition(PossibleRoot, 0)}\n\n"
            Roots.append(PossibleRoot.VariableName)

        PythonFile += "\n#### DemoAIAction ####\n\nDemoAIAction = ["
        
        DemoActionString = "\n"

        for Def in AllDefinitions:
            if Def.DemoAction and not Def.AlreadyAdded:
                DemoActionString += f"\t{VariableDefinition(Def, 1)}, \n"

        if DemoActionString == "":
            PythonFile += "]\n"
        else:
            DemoActionString = DemoActionString[:-3]
            DemoActionString += "\n]\n"
            PythonFile += DemoActionString

        PythonFile += "\n\n#### Queries ####\n\nQueries = ["

        if len(Definitions["Query"]) > 0:
            PythonFile += "\n"
            for Query in Definitions["Query"]:
                PythonFile += f"\t{VariableDefinition(Query, 0)}, \n"

            PythonFile = PythonFile[:-3]
            PythonFile += "\n]\n"
        else:
            PythonFile += "]\n"

        PythonFile += f"\n\nAICreator.CreateBaiprog(\"{Dst}\", [{', '.join(Roots)}], DemoAIAction, Queries)"

    with open(f"{Dst}.py", "w", encoding="utf-8") as f:
        f.write(PythonFile)
        f.close()

def readConfig(ConfigName):
    PATH = os.path.dirname(os.path.abspath(__file__))
    CONFIGFILE = "\properties.ini"

    config = configparser.ConfigParser()
    config.read(PATH + CONFIGFILE)
    return config.get("TRANSLATE", ConfigName).lower() == "true"


if __name__ == "__main__":

    import sys

    Src = ""
    Dst = ""
    TranslateNames = readConfig("Names")
    TranslateChildren = readConfig("Children")

    Src = sys.argv[1]

    if(len(sys.argv) == 2):
        Dst = Src.replace(".baiprog", "").replace(".yml", "").replace(".txt", "")
    if(len(sys.argv) > 2):
        Dst = sys.argv[2]

    GetCode(Src, Dst, TranslateNames, TranslateChildren)