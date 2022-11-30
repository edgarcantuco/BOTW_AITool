# BOTW AI Editor
Python tool designed to make editing baiprog files easier and in a tree way without having to worry about indices.

## Requirements
* Python 3.7+
* A little bit of knowledge on how to code simple scripts. Although, just by looking at some examples it should be pretty straighforward.

## Setup
1. Go to the [Releases](https://github.com/edgarcantuco/BOTW_AITool/releases) page and download the latest release.
2. Extract the zip file you downloaded into an empty folder.

## How to use
The tool works as a python script where you can write a baiprog file as a python file. The best way to see how this works is by following step 1. But if you already understand how the tool works and want to start from scratch, I then would recommend you to skip to step 2.

### 1. Converting from baiprog to .py
1. Obtain your baiprog either by using [botw_actor_tool](https://github.com/GingerAvalanche/botw_actor_tool), [WildBits](https://github.com/NiceneNerd/Wild-Bits) or any tool similar and copy it to either a .yml or .txt file.
2. There are two ways to convert your baiprog to .py
	1. Drag your .yml/.txt file into AICreator.py in your extracted folder. It will take the name of the file and save the python file with that name as well.
	2. Open a cmd in the folder where you extracted the project and run the following command: `AICreator.py <Src> <Dst: optional>` this will save the python file with the name you give in Dst.
3. Wait for the cmd to finish processing the baiprog file.

**Be careful because this will overwrite any existing python files with the same name as you are extracting.**

### 2. Writing the AI
1. Open your .py file with your favorite IDE.
2. Add the import statements for whatever you will use as shown next:
	1. `from Classes.Action import *`
	2. `from Classes.AI import *`
	3. `from Classes.Behavior import *`
	4. `from Classes.Query import *`
	5. `import AICreator`
3. Write all the AI blocks you need. **I recommend you to first export a baiprog file to see how the AI blocks should be written.**
4. Add the following statement `AICreator.CreateBaiprog(<ExportName: string>, [Root AIs], DemoAIAction, Queries)`
5. Run the script.