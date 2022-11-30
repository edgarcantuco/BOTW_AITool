class ASWeaponRoot:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, Equiped, UnEquiped, Thrown, Stick, CancelStick, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Equiped = Equiped
		self.UnEquiped = UnEquiped
		self.Thrown = Thrown
		self.Stick = Stick
		self.CancelStick = CancelStick
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class ActorWaterDepthSelect:
	ChildNames = ["浅瀬", "深瀬"]

	def __init__(self, Name, DeepDepth, OnEnterOnly, ForceDeepChange, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeepDepth = DeepDepth
		self.OnEnterOnly = OnEnterOnly
		self.ForceDeepChange = ForceDeepChange
		self.Child0 = Child0
		self.Child1 = Child1


class AddBasicLinkOn:
	ChildNames = ["行動"]

	def __init__(self, Name, OnlyOne, IsBroadCastOnlyOne, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnlyOne = OnlyOne
		self.IsBroadCastOnlyOne = IsBroadCastOnlyOne
		self.Child0 = Child0


class AddCarried:
	ChildNames = ["持ち上げられ中", "行動"]

	def __init__(self, Name, IsRecoverCharCtrlAxis, FailDistance, IsUseConstraint, HoldOnXLinkKey, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.FailDistance = FailDistance
		self.IsUseConstraint = IsUseConstraint
		self.HoldOnXLinkKey = HoldOnXLinkKey
		self.Child0 = Child0
		self.Child1 = Child1


class AddDemoCall:
	ChildNames = ["行動"]

	def __init__(self, Name, OnlyOne, IsBroadCastOnlyOne, EntryPoint, DemoName, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnlyOne = OnlyOne
		self.IsBroadCastOnlyOne = IsBroadCastOnlyOne
		self.EntryPoint = EntryPoint
		self.DemoName = DemoName
		self.Child0 = Child0


class AddNodeNodeCarried:
	ChildNames = ["持ち上げられ中", "行動"]

	def __init__(self, Name, MyNode, NodeRotOffset, IsRecoverCharCtrlAxis, FailDistance, IsUseConstraint, HoldOnXLinkKey, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MyNode = MyNode
		self.NodeRotOffset = NodeRotOffset
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.FailDistance = FailDistance
		self.IsUseConstraint = IsUseConstraint
		self.HoldOnXLinkKey = HoldOnXLinkKey
		self.Child0 = Child0
		self.Child1 = Child1


class AddPlayerLargeAttackJustGuard:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class AddSwarmMove:
	ChildNames = ["移動"]

	def __init__(self, Name, SubSpeed, SubAccRateMin, SubAccRateMax, IsEndBySensor, AnimName, IgnoreSensorTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubSpeed = SubSpeed
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.IsEndBySensor = IsEndBySensor
		self.AnimName = AnimName
		self.IgnoreSensorTime = IgnoreSensorTime
		self.Child0 = Child0


class AddViewTargetPos:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class AirOctaBoardBurn:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class AirOctaBurnReaction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, DisconnectTime, DisconnectRandTime, SingleBurnTime, ChangeRandTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisconnectTime = DisconnectTime
		self.DisconnectRandTime = DisconnectRandTime
		self.SingleBurnTime = SingleBurnTime
		self.ChangeRandTime = ChangeRandTime
		self.Child0 = Child0
		self.Child1 = Child1


class AirOctaFlyUp:
	ChildNames = ["終了", "開始"]

	def __init__(self, Name, FlyUpDuration, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FlyUpDuration = FlyUpDuration
		self.Child0 = Child0
		self.Child1 = Child1


class AirOctaReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class AirOctaRoot:
	ChildNames = ["子０", "子１"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class AirOctaState:
	ChildNames = ["オクタの数が減った", "プレイヤが板に乗った", "リアクション", "上昇", "呼ばれ", "奈落", "待機", "所持", "板切断", "板燃焼", "死亡生成", "水中", "滝死亡", "発見", "落下", "近接湧出", "逃げる", "通常", "騎乗"]

	def __init__(self, Name, RopeGravityFactor, BalloonMassRatio, WindForceScale, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RopeGravityFactor = RopeGravityFactor
		self.BalloonMassRatio = BalloonMassRatio
		self.WindForceScale = WindForceScale
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18


class AirOctaWait:
	ChildNames = ["水上", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class AlertCreationNestOnTree:
	ChildNames = ["もげる", "通常"]

	def __init__(self, Name, CreateIntervalTime, IsRemainNum, ActorNum, TargetEscapedRadius, AttOnTree, AttOnGround, FallPowerMin, FallPowerMax, FallOddsMin, FallOddsMax, FallIntervalRange, FallCheckSpeedTh, AtHitImpulseRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateIntervalTime = CreateIntervalTime
		self.IsRemainNum = IsRemainNum
		self.ActorNum = ActorNum
		self.TargetEscapedRadius = TargetEscapedRadius
		self.AttOnTree = AttOnTree
		self.AttOnGround = AttOnGround
		self.FallPowerMin = FallPowerMin
		self.FallPowerMax = FallPowerMax
		self.FallOddsMin = FallOddsMin
		self.FallOddsMax = FallOddsMax
		self.FallIntervalRange = FallIntervalRange
		self.FallCheckSpeedTh = FallCheckSpeedTh
		self.AtHitImpulseRate = AtHitImpulseRate
		self.Child0 = Child0
		self.Child1 = Child1


class AmbushableWeaponShoot:
	ChildNames = ["投擲", "迎撃"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class AnchorRangeSelectTwoAction:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, AnchorName, FarDist, BaseDist, WeaponIdx, IsSelectEveryFrame, IsRangeXZ, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnchorName = AnchorName
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.IsRangeXZ = IsRangeXZ
		self.Child0 = Child0
		self.Child1 = Child1


class AncientNecklaceBall:
	ChildNames = ["吊るす", "所持", "投擲生成", "通常"]

	def __init__(self, Name, LandNoiseLevel, OnAS, OffAS, IsIgnoreSameOnAS, IsIgnoreSameOffAS, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LandNoiseLevel = LandNoiseLevel
		self.OnAS = OnAS
		self.OffAS = OffAS
		self.IsIgnoreSameOnAS = IsIgnoreSameOnAS
		self.IsIgnoreSameOffAS = IsIgnoreSameOffAS
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AnimalAttackOtherTarget:
	ChildNames = ["待機", "戦闘行動", "攻撃後"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AnimalBattleAggressive:
	ChildNames = ["カウンター攻撃", "ダメージ後", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ForceAttackRange, ForceAttackTimer, CounterAttackRange, CounterAttackTimer, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceAttackRange = ForceAttackRange
		self.ForceAttackTimer = ForceAttackTimer
		self.CounterAttackRange = CounterAttackRange
		self.CounterAttackTimer = CounterAttackTimer
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AnimalBattleMoveLeave:
	ChildNames = ["旋回", "移動"]

	def __init__(self, Name, CheckForwardDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckForwardDist = CheckForwardDist
		self.Child0 = Child0
		self.Child1 = Child1


class AnimalEscapeAI:
	ChildNames = ["地形嵌り", "最後の手段", "逃走", "逃走前"]

	def __init__(self, Name, ContinueDistance, ShouldEscapeDistance, ShouldEscapeDistanceRand, PenaltyScale, NavMeshRadiusScale, FramesStuckOnTerrainAction, NumTimesAllowStuck, IsSendGoalPos, IsUseBeforeAction, IsDynamicallyOffsetNavChar, SearchNextPathRadius, RadiusLimit, ForwardDirDistCoefficient, DirRandomMinRatio, DirRangeAngle, RejectDistRatio, ContinueAddSearchAngle, ContinueReduceDistRatio, ContinueReduceRejectDistRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ContinueDistance = ContinueDistance
		self.ShouldEscapeDistance = ShouldEscapeDistance
		self.ShouldEscapeDistanceRand = ShouldEscapeDistanceRand
		self.PenaltyScale = PenaltyScale
		self.NavMeshRadiusScale = NavMeshRadiusScale
		self.FramesStuckOnTerrainAction = FramesStuckOnTerrainAction
		self.NumTimesAllowStuck = NumTimesAllowStuck
		self.IsSendGoalPos = IsSendGoalPos
		self.IsUseBeforeAction = IsUseBeforeAction
		self.IsDynamicallyOffsetNavChar = IsDynamicallyOffsetNavChar
		self.SearchNextPathRadius = SearchNextPathRadius
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomMinRatio = DirRandomMinRatio
		self.DirRangeAngle = DirRangeAngle
		self.RejectDistRatio = RejectDistRatio
		self.ContinueAddSearchAngle = ContinueAddSearchAngle
		self.ContinueReduceDistRatio = ContinueReduceDistRatio
		self.ContinueReduceRejectDistRatio = ContinueReduceRejectDistRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AnimalEscapeAfterDamage:
	ChildNames = ["ダメージ後", "地形嵌り", "最後の手段", "逃走", "逃走前"]

	def __init__(self, Name, ContinueDistance, ShouldEscapeDistance, ShouldEscapeDistanceRand, PenaltyScale, NavMeshRadiusScale, FramesStuckOnTerrainAction, NumTimesAllowStuck, IsSendGoalPos, IsUseBeforeAction, IsDynamicallyOffsetNavChar, SearchNextPathRadius, RadiusLimit, ForwardDirDistCoefficient, DirRandomMinRatio, DirRangeAngle, RejectDistRatio, ContinueAddSearchAngle, ContinueReduceDistRatio, ContinueReduceRejectDistRatio, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ContinueDistance = ContinueDistance
		self.ShouldEscapeDistance = ShouldEscapeDistance
		self.ShouldEscapeDistanceRand = ShouldEscapeDistanceRand
		self.PenaltyScale = PenaltyScale
		self.NavMeshRadiusScale = NavMeshRadiusScale
		self.FramesStuckOnTerrainAction = FramesStuckOnTerrainAction
		self.NumTimesAllowStuck = NumTimesAllowStuck
		self.IsSendGoalPos = IsSendGoalPos
		self.IsUseBeforeAction = IsUseBeforeAction
		self.IsDynamicallyOffsetNavChar = IsDynamicallyOffsetNavChar
		self.SearchNextPathRadius = SearchNextPathRadius
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomMinRatio = DirRandomMinRatio
		self.DirRangeAngle = DirRangeAngle
		self.RejectDistRatio = RejectDistRatio
		self.ContinueAddSearchAngle = ContinueAddSearchAngle
		self.ContinueReduceDistRatio = ContinueReduceDistRatio
		self.ContinueReduceRejectDistRatio = ContinueReduceRejectDistRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class AnimalFollowTarget:
	ChildNames = ["うろうろする", "追いかける(近い)", "追いかける(遠い)"]

	def __init__(self, Name, UseLocalOffsetType, DistanceSuccessEnd, DistanceMovingToward, DistanceRequestingPath, DistanceGivingUp, DistanceThresholdCry, DistanceCheckAvoidance, TargetVelocitySuccessEnd, UpdateTargetPosFrames, UpdateTargetPosFramesNear, SuccessEndDelays, SelfPositionOffsetLocal, SideDistance, TargetVelocityDistanceSec, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, CanIgnorePlayer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseLocalOffsetType = UseLocalOffsetType
		self.DistanceSuccessEnd = DistanceSuccessEnd
		self.DistanceMovingToward = DistanceMovingToward
		self.DistanceRequestingPath = DistanceRequestingPath
		self.DistanceGivingUp = DistanceGivingUp
		self.DistanceThresholdCry = DistanceThresholdCry
		self.DistanceCheckAvoidance = DistanceCheckAvoidance
		self.TargetVelocitySuccessEnd = TargetVelocitySuccessEnd
		self.UpdateTargetPosFrames = UpdateTargetPosFrames
		self.UpdateTargetPosFramesNear = UpdateTargetPosFramesNear
		self.SuccessEndDelays = SuccessEndDelays
		self.SelfPositionOffsetLocal = SelfPositionOffsetLocal
		self.SideDistance = SideDistance
		self.TargetVelocityDistanceSec = TargetVelocityDistanceSec
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.CanIgnorePlayer = CanIgnorePlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AnimalLineOfSightSelector:
	ChildNames = ["Gear1", "Gear2", "Gear3", "Gear4"]

	def __init__(self, Name, StartGear, MinGear, MaxGear, GearUpRestrictionFrames, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartGear = StartGear
		self.MinGear = MinGear
		self.MaxGear = MaxGear
		self.GearUpRestrictionFrames = GearUpRestrictionFrames
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AnimalPreAttack:
	ChildNames = ["対象を向く", "距離を取る"]

	def __init__(self, Name, KeepDistCheckLength, BackCliffCheckLength, ForceEndTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepDistCheckLength = KeepDistCheckLength
		self.BackCliffCheckLength = BackCliffCheckLength
		self.ForceEndTime = ForceEndTime
		self.Child0 = Child0
		self.Child1 = Child1


class AnimalRangeKeepMove:
	ChildNames = ["接近", "通常行動", "離脱"]

	def __init__(self, Name, CloseStartDist, CloseEndDist, LeaveStartDist, LeaveEndDist, BattleEndDist, BattleEndTimerMin, BattleEndTimerMax, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseStartDist = CloseStartDist
		self.CloseEndDist = CloseEndDist
		self.LeaveStartDist = LeaveStartDist
		self.LeaveEndDist = LeaveEndDist
		self.BattleEndDist = BattleEndDist
		self.BattleEndTimerMin = BattleEndTimerMin
		self.BattleEndTimerMax = BattleEndTimerMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AnimalRangeKeepMoveWithLOS:
	ChildNames = ["パス検索", "崖である", "接近", "通常行動", "離脱"]

	def __init__(self, Name, CloseStartDist, CloseEndDist, LeaveStartDist, LeaveEndDist, BattleEndDist, FindPathBeginTimer, NoPathTimer, DistFailOnUnreachablePath, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseStartDist = CloseStartDist
		self.CloseEndDist = CloseEndDist
		self.LeaveStartDist = LeaveStartDist
		self.LeaveEndDist = LeaveEndDist
		self.BattleEndDist = BattleEndDist
		self.FindPathBeginTimer = FindPathBeginTimer
		self.NoPathTimer = NoPathTimer
		self.DistFailOnUnreachablePath = DistFailOnUnreachablePath
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class AnimalRoam:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, LimitRadius, ChangeWaitRate, FinishChangeCount, IsSendGoalPos, FramesStuckOnTerrainAction, CheckValidStartPos, CheckLOS, SearchNextPathRadius, RadiusLimit, ForwardDirDistCoefficient, DirRandomMinRatio, DirRangeAngle, RejectDistRatio, ContinueAddSearchAngle, ContinueReduceDistRatio, ContinueReduceRejectDistRatio, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitRadius = LimitRadius
		self.ChangeWaitRate = ChangeWaitRate
		self.FinishChangeCount = FinishChangeCount
		self.IsSendGoalPos = IsSendGoalPos
		self.FramesStuckOnTerrainAction = FramesStuckOnTerrainAction
		self.CheckValidStartPos = CheckValidStartPos
		self.CheckLOS = CheckLOS
		self.SearchNextPathRadius = SearchNextPathRadius
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomMinRatio = DirRandomMinRatio
		self.DirRangeAngle = DirRangeAngle
		self.RejectDistRatio = RejectDistRatio
		self.ContinueAddSearchAngle = ContinueAddSearchAngle
		self.ContinueReduceDistRatio = ContinueReduceDistRatio
		self.ContinueReduceRejectDistRatio = ContinueReduceRejectDistRatio
		self.Child0 = Child0
		self.Child1 = Child1


class AnimalRoamCheckWater:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, WaterLevelLimitLower, WaterLevelLimitUpper, LimitRadius, ChangeWaitRate, FinishChangeCount, IsSendGoalPos, FramesStuckOnTerrainAction, CheckValidStartPos, CheckLOS, SearchNextPathRadius, RadiusLimit, ForwardDirDistCoefficient, DirRandomMinRatio, DirRangeAngle, RejectDistRatio, ContinueAddSearchAngle, ContinueReduceDistRatio, ContinueReduceRejectDistRatio, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaterLevelLimitLower = WaterLevelLimitLower
		self.WaterLevelLimitUpper = WaterLevelLimitUpper
		self.LimitRadius = LimitRadius
		self.ChangeWaitRate = ChangeWaitRate
		self.FinishChangeCount = FinishChangeCount
		self.IsSendGoalPos = IsSendGoalPos
		self.FramesStuckOnTerrainAction = FramesStuckOnTerrainAction
		self.CheckValidStartPos = CheckValidStartPos
		self.CheckLOS = CheckLOS
		self.SearchNextPathRadius = SearchNextPathRadius
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomMinRatio = DirRandomMinRatio
		self.DirRangeAngle = DirRangeAngle
		self.RejectDistRatio = RejectDistRatio
		self.ContinueAddSearchAngle = ContinueAddSearchAngle
		self.ContinueReduceDistRatio = ContinueReduceDistRatio
		self.ContinueReduceRejectDistRatio = ContinueReduceRejectDistRatio
		self.Child0 = Child0
		self.Child1 = Child1


class AnimalRushAttack:
	ChildNames = ["突進"]

	def __init__(self, Name, AttackPosOffsetLength, UpdateTargetPosTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPosOffsetLength = AttackPosOffsetLength
		self.UpdateTargetPosTime = UpdateTargetPosTime
		self.Child0 = Child0


class AnimalTimelineAI:
	ChildNames = ["Action1", "Action2", "Action3", "Action4", "Idle"]

	def __init__(self, Name, IntervalToCheckSchedule, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IntervalToCheckSchedule = IntervalToCheckSchedule
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class AppearFromTargetFrontAfterChase:
	ChildNames = ["湧出", "湧出出現", "湧出準備"]

	def __init__(self, Name, AppearDist, Dist, TeraDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AppearDist = AppearDist
		self.Dist = Dist
		self.TeraDist = TeraDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AppearFromTargetFrontGround:
	ChildNames = ["湧出", "湧出準備"]

	def __init__(self, Name, Dist, TeraDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.TeraDist = TeraDist
		self.Child0 = Child0
		self.Child1 = Child1


class AppearNearTargetOutOfScrnGnd:
	ChildNames = ["湧出", "湧出準備"]

	def __init__(self, Name, Dist, TeraDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.TeraDist = TeraDist
		self.Child0 = Child0
		self.Child1 = Child1


class ArmorSearchKorokRoot:
	ChildNames = ["未発見", "発見"]

	def __init__(self, Name, SearchKorokDis, SearchRefreshFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchKorokDis = SearchKorokDis
		self.SearchRefreshFrame = SearchRefreshFrame
		self.Child0 = Child0
		self.Child1 = Child1


class AroundEnemyCheckSelect:
	ChildNames = ["いない", "いる"]

	def __init__(self, Name, CheckDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.Child0 = Child0
		self.Child1 = Child1


class Arrow:
	ChildNames = ["ホーミング", "上空撃ち", "刺さる", "回収", "所持", "所持前", "接地", "消滅", "爆発", "発射", "跳ね返る"]

	def __init__(self, Name, GroundHitTime, StickTime, KillFireTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GroundHitTime = GroundHitTime
		self.StickTime = StickTime
		self.KillFireTime = KillFireTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class ArrowChargeAndShoot:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, WeaponIdx, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class ArrowDelete:
	ChildNames = ["ケミカル待機", "消滅"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ArrowStickAndPick:
	ChildNames = ["サブボタン", "メインボタン", "消滅", "通常"]

	def __init__(self, Name, CanGetOnBurning, GetAttKeyName, IsControlNoticeDo, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CanGetOnBurning = CanGetOnBurning
		self.GetAttKeyName = GetAttKeyName
		self.IsControlNoticeDo = IsControlNoticeDo
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AssassinBattle:
	ChildNames = ["内側転移", "直進不能接近", "直進接近", "諦め", "転移", "通常戦闘", "速攻"]

	def __init__(self, Name, WarpDist, BattleBaseDist, WeaponIdx, FirstAttackResetDist, BattleDistOutDist, FirstAttackAngle, TiredDist, TiredTime, FirstAttackDist, NearTiredOffset, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpDist = WarpDist
		self.BattleBaseDist = BattleBaseDist
		self.WeaponIdx = WeaponIdx
		self.FirstAttackResetDist = FirstAttackResetDist
		self.BattleDistOutDist = BattleDistOutDist
		self.FirstAttackAngle = FirstAttackAngle
		self.TiredDist = TiredDist
		self.TiredTime = TiredTime
		self.FirstAttackDist = FirstAttackDist
		self.NearTiredOffset = NearTiredOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class AssassinBattleMove:
	ChildNames = ["強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動", "転移"]

	def __init__(self, Name, WarpDist, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpDist = WarpDist
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class AssassinBattleRange:
	ChildNames = ["サービス", "変わり身", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ScapeGoatCheckInterval, ScapeGoatPer, ServiceCheckInterval, ServicePer, ServiceDist, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ScapeGoatCheckInterval = ScapeGoatCheckInterval
		self.ScapeGoatPer = ScapeGoatPer
		self.ServiceCheckInterval = ServiceCheckInterval
		self.ServicePer = ServicePer
		self.ServiceDist = ServiceDist
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AssassinBossAttackSeq:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class AssassinBossBattle:
	ChildNames = ["攻撃", "様子見", "移動"]

	def __init__(self, Name, IntervalIntensity, RetFrmDmgAtkTimer, AnchorName, HomeDist, BattleDist, DyingLifeRatio, BattleDistSecond, ReturnHeight, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IntervalIntensity = IntervalIntensity
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.AnchorName = AnchorName
		self.HomeDist = HomeDist
		self.BattleDist = BattleDist
		self.DyingLifeRatio = DyingLifeRatio
		self.BattleDistSecond = BattleDistSecond
		self.ReturnHeight = ReturnHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AssassinBossEscapeFromTarget:
	ChildNames = ["後退不能移動", "後退移動", "後退移動完了"]

	def __init__(self, Name, AnchorName, CheckDist, SpaceDist, KeepTime, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnchorName = AnchorName
		self.CheckDist = CheckDist
		self.SpaceDist = SpaceDist
		self.KeepTime = KeepTime
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AssassinBossFirstBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "絶対防御の構え"]

	def __init__(self, Name, IronBallKeyName, IronBallNum, GuardAngle, AttackInterseptDist, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallKeyName = IronBallKeyName
		self.IronBallNum = IronBallNum
		self.GuardAngle = GuardAngle
		self.AttackInterseptDist = AttackInterseptDist
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AssassinBossFirstBattleMove:
	ChildNames = ["直線接近不能", "直線接近可能"]

	def __init__(self, Name, AnchorName, DistXZ, CheckTargetDist, TooFarXZ, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnchorName = AnchorName
		self.DistXZ = DistXZ
		self.CheckTargetDist = CheckTargetDist
		self.TooFarXZ = TooFarXZ
		self.Child0 = Child0
		self.Child1 = Child1


class AssassinBossFirstRangeKeepMove:
	ChildNames = ["強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動"]

	def __init__(self, Name, AnchorName, NoMoveAnchorDist, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnchorName = AnchorName
		self.NoMoveAnchorDist = NoMoveAnchorDist
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class AssassinBossFirstRoot:
	ChildNames = ["リアクション", "リアクション復帰", "呼ばれ", "奈落", "強制ワープ回避", "所持", "撤退", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, ChangeModeLifeRatio, RockBallDamage, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeModeLifeRatio = ChangeModeLifeRatio
		self.RockBallDamage = RockBallDamage
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class AssassinBossIronBallAttack:
	ChildNames = ["攻撃", "準備完了待ち"]

	def __init__(self, Name, IronBallNum, IronBallPartsName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.IronBallPartsName = IronBallPartsName
		self.Child0 = Child0
		self.Child1 = Child1


class AssassinBossLastAttack:
	ChildNames = ["攻撃", "攻撃予兆", "攻撃失敗", "準備完了待ち"]

	def __init__(self, Name, IronBallNum, IronBallPartsName, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.IronBallPartsName = IronBallPartsName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AssassinBossRoot:
	ChildNames = ["デモ用移動", "リアクション", "リアクション復帰", "三段階目デモ用", "二段階目デモ用", "呼ばれ", "奈落", "強制ワープ回避", "所持", "撤退", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, IronBallNum, BattleAvoidNum, ChangeModeLifeRatio, RockBallDamage, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.BattleAvoidNum = BattleAvoidNum
		self.ChangeModeLifeRatio = ChangeModeLifeRatio
		self.RockBallDamage = RockBallDamage
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class AssassinCallSelect:
	ChildNames = ["出現", "変身デモ"]

	def __init__(self, Name, ChangeDemoName, ChangeDemoEPName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeDemoName = ChangeDemoName
		self.ChangeDemoEPName = ChangeDemoEPName
		self.Child0 = Child0
		self.Child1 = Child1


class AssassinFieldShooterBattle:
	ChildNames = ["待機", "戦闘攻撃", "諦め", "転移"]

	def __init__(self, Name, WarpDistNear, WarpDistFar, WeaponIdx, TerritoryDist, TiredGrHeight, TiredTime, IntervalIntensity, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpDistNear = WarpDistNear
		self.WarpDistFar = WarpDistFar
		self.WeaponIdx = WeaponIdx
		self.TerritoryDist = TerritoryDist
		self.TiredGrHeight = TiredGrHeight
		self.TiredTime = TiredTime
		self.IntervalIntensity = IntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class AssassinMiddleAzitoDlcRoot:
	ChildNames = ["プレイヤー発見", "不審物排除後", "不審物発見", "不審者発見", "不調仲間発見", "危険回避", "好物発見", "待機", "怒り", "攻撃反応", "気配気づき", "浮遊物発見", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, EntryPoint, DemoName, LikeItem, TerrorIgnoreDist, ExplosivesSearchDist, ExplosivesSearchSpeed, ExplosivesSearchAng, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EntryPoint = EntryPoint
		self.DemoName = DemoName
		self.LikeItem = LikeItem
		self.TerrorIgnoreDist = TerrorIgnoreDist
		self.ExplosivesSearchDist = ExplosivesSearchDist
		self.ExplosivesSearchSpeed = ExplosivesSearchSpeed
		self.ExplosivesSearchAng = ExplosivesSearchAng
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16


class AssassinMiddleAzitoNoMemberDemo:
	ChildNames = ["待機", "気づき"]

	def __init__(self, Name, DelayTimeMin, DelayTimeMax, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DelayTimeMin = DelayTimeMin
		self.DelayTimeMax = DelayTimeMax
		self.Child0 = Child0
		self.Child1 = Child1


class AssassinMiddleAzitoRoot:
	ChildNames = ["プレイヤー発見", "不審物排除後", "不審物発見", "不審者発見", "不調仲間発見", "危険回避", "好物発見", "待機", "怒り", "攻撃反応", "気配気づき", "浮遊物発見", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, EntryPoint, DemoName, LikeItem, TerrorIgnoreDist, ExplosivesSearchDist, ExplosivesSearchSpeed, ExplosivesSearchAng, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EntryPoint = EntryPoint
		self.DemoName = DemoName
		self.LikeItem = LikeItem
		self.TerrorIgnoreDist = TerrorIgnoreDist
		self.ExplosivesSearchDist = ExplosivesSearchDist
		self.ExplosivesSearchSpeed = ExplosivesSearchSpeed
		self.ExplosivesSearchAng = ExplosivesSearchAng
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16


class AssassinMiddleAzitoRootAccept:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, EntryPoint, DemoName, SheathOffset, PodModelUnitIdx, PodNodeName, MagicUsePartsName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EntryPoint = EntryPoint
		self.DemoName = DemoName
		self.SheathOffset = SheathOffset
		self.PodModelUnitIdx = PodModelUnitIdx
		self.PodNodeName = PodNodeName
		self.MagicUsePartsName = MagicUsePartsName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class AssassinMiddleDlcGrabAdapter:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class AssassinMiddleMagicAfter:
	ChildNames = ["エリア内", "エリア外", "一度やられた"]

	def __init__(self, Name, Height, Option, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Height = Height
		self.Option = Option
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AssassinMiddleRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, SheathOffset, PodModelUnitIdx, PodNodeName, MagicUsePartsName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SheathOffset = SheathOffset
		self.PodModelUnitIdx = PodModelUnitIdx
		self.PodNodeName = PodNodeName
		self.MagicUsePartsName = MagicUsePartsName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class AssassinRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, ChangeDistance, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeDistance = ChangeDistance
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class AssassinShooterJuniorAzitoRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, RememberKey, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RememberKey = RememberKey
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class AttackGrave:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class AttackGraveChase:
	ChildNames = ["接近後", "行動"]

	def __init__(self, Name, EndHeight, EndNear, ActionTime, NearTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndHeight = EndHeight
		self.EndNear = EndNear
		self.ActionTime = ActionTime
		self.NearTime = NearTime
		self.Child0 = Child0
		self.Child1 = Child1


class AttackGraveChaseWithSensor:
	ChildNames = ["接近後", "行動"]

	def __init__(self, Name, RigidBodyGroupName, RigidBodyName, EndHeight, EndNear, ActionTime, NearTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyGroupName = RigidBodyGroupName
		self.RigidBodyName = RigidBodyName
		self.EndHeight = EndHeight
		self.EndNear = EndNear
		self.ActionTime = ActionTime
		self.NearTime = NearTime
		self.Child0 = Child0
		self.Child1 = Child1


class AttackHitCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, AtkType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkType = AtkType
		self.Child0 = Child0
		self.Child1 = Child1


class AwarenessScale:
	ChildNames = ["行動"]

	def __init__(self, Name, Scale, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Scale = Scale
		self.Child0 = Child0


class BackAttackEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "背面攻撃"]

	def __init__(self, Name, BackAttackAngle, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BackAttackAngle = BackAttackAngle
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BackStepAndAttack:
	ChildNames = ["バックステップ", "回転", "攻撃"]

	def __init__(self, Name, BackStepMinDist, BackStepDist, FrontAngle, NoBackStepRange, BackStepMax, TurnRepeatMax, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BackStepMinDist = BackStepMinDist
		self.BackStepDist = BackStepDist
		self.FrontAngle = FrontAngle
		self.NoBackStepRange = NoBackStepRange
		self.BackStepMax = BackStepMax
		self.TurnRepeatMax = TurnRepeatMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BalloonPlantNormal:
	ChildNames = ["失敗", "寄生する", "準備待機"]

	def __init__(self, Name, RopeActorName, RopeLength, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RopeActorName = RopeActorName
		self.RopeLength = RopeLength
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BarrelBomb:
	ChildNames = ["所持", "投擲生成", "爆発", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class BasicStatusRoot:
	ChildNames = ["凍結", "持ち運びボックス内", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BattleBgmRequestFinishTag:
	ChildNames = ["待機"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class BeamExplode:
	ChildNames = ["後処理", "爆発", "着弾前"]

	def __init__(self, Name, MaxDistance, IsDelete, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistance = MaxDistance
		self.IsDelete = IsDelete
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BeamExplodeEitherHit:
	ChildNames = ["後処理", "爆発", "着弾前"]

	def __init__(self, Name, MaxDistance, IsDelete, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistance = MaxDistance
		self.IsDelete = IsDelete
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BeamosCarried:
	ChildNames = ["持ち上げられ中", "行動"]

	def __init__(self, Name, IsRecoverCharCtrlAxis, FailDistance, IsUseConstraint, HoldOnXLinkKey, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.FailDistance = FailDistance
		self.IsUseConstraint = IsUseConstraint
		self.HoldOnXLinkKey = HoldOnXLinkKey
		self.Child0 = Child0
		self.Child1 = Child1


class BeeBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class BeeSwarmFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class BeeSwarmNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "死亡", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class BeeSwarmReaction:
	ChildNames = ["ケミカル接触", "死亡", "消滅", "突風", "範囲ダメージ", "通常ダメージ"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class BeeSwarmRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, ASName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class BirdDead:
	ChildNames = ["空中死亡", "通常死亡"]

	def __init__(self, Name, GravityScale, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GravityScale = GravityScale
		self.Child0 = Child0
		self.Child1 = Child1


class BirdEscape:
	ChildNames = ["逃走", "逃走前", "逃走終了"]

	def __init__(self, Name, ForceEndTimer, IsUseEscapeBefore, IsUseEscapeEnd, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceEndTimer = ForceEndTimer
		self.IsUseEscapeBefore = IsUseEscapeBefore
		self.IsUseEscapeEnd = IsUseEscapeEnd
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BlownOff:
	ChildNames = ["ふっとび", "凍結", "水死", "起き上がり", "起き上がり凍結"]

	def __init__(self, Name, DrownDepth, IsForceGetUp, IsIceBreak, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DrownDepth = DrownDepth
		self.IsForceGetUp = IsForceGetUp
		self.IsIceBreak = IsIceBreak
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class BocoblinBackStepAttack:
	ChildNames = ["バックステップ", "バックステップアタック"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class BokoblinArrowAttack:
	ChildNames = ["前進", "後ずさり", "静止"]

	def __init__(self, Name, WeaponIdx, BackWalkStartDist, BackWalkEndDist, CliffCheckDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.BackWalkStartDist = BackWalkStartDist
		self.BackWalkEndDist = BackWalkEndDist
		self.CliffCheckDist = CliffCheckDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BokoblinArrowBattle:
	ChildNames = ["弓構え", "待機", "離脱"]

	def __init__(self, Name, HoldInterval, HoldIntervalLast, HoldIntervalRand, LeaveStartDist, LeaveEndDist, LeaveTime, LeaveWaitTime, BaseDist, OutDist, OutDistVMin, OutDistVMax, WeaponIdx, BlindlyAttackMinNum, BlindlyAttackMaxNum, ShootDistRatio, IsEndAfterAttack, IsUpdateNoticeState, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HoldInterval = HoldInterval
		self.HoldIntervalLast = HoldIntervalLast
		self.HoldIntervalRand = HoldIntervalRand
		self.LeaveStartDist = LeaveStartDist
		self.LeaveEndDist = LeaveEndDist
		self.LeaveTime = LeaveTime
		self.LeaveWaitTime = LeaveWaitTime
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.OutDistVMin = OutDistVMin
		self.OutDistVMax = OutDistVMax
		self.WeaponIdx = WeaponIdx
		self.BlindlyAttackMinNum = BlindlyAttackMinNum
		self.BlindlyAttackMaxNum = BlindlyAttackMaxNum
		self.ShootDistRatio = ShootDistRatio
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class BokoblinHoldArrow:
	ChildNames = ["溜め", "発射"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class BokoblinNoise:
	ChildNames = ["囃し立てる", "待機"]

	def __init__(self, Name, MaxContinueNum, EnterNoiseRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxContinueNum = MaxContinueNum
		self.EnterNoiseRate = EnterNoiseRate
		self.Child0 = Child0
		self.Child1 = Child1


class BokoblinRestraint:
	ChildNames = ["威嚇", "投石"]

	def __init__(self, Name, BaseDist, AttackIntervalMin, AttackIntervalMax, LostVMin, LostVMax, LostTimer, LostRange, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseDist = BaseDist
		self.AttackIntervalMin = AttackIntervalMin
		self.AttackIntervalMax = AttackIntervalMax
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.Child0 = Child0
		self.Child1 = Child1


class BokoblinRoam:
	ChildNames = ["回転", "待機", "暇つぶし", "移動", "索敵"]

	def __init__(self, Name, FreeIntervalMin, FreeIntervalMax, FreePer, MoveIntervalMin, MoveIntervalMax, Territory, TargetDistMin, TargetDistMax, NoMoveTime, NoSpAttackMoveTime, SpAttackServiceDist, SpAttackServiceTime, SpAttackServiceAngle, TurnCheckDist, TurnCheckHeight, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FreeIntervalMin = FreeIntervalMin
		self.FreeIntervalMax = FreeIntervalMax
		self.FreePer = FreePer
		self.MoveIntervalMin = MoveIntervalMin
		self.MoveIntervalMax = MoveIntervalMax
		self.Territory = Territory
		self.TargetDistMin = TargetDistMin
		self.TargetDistMax = TargetDistMax
		self.NoMoveTime = NoMoveTime
		self.NoSpAttackMoveTime = NoSpAttackMoveTime
		self.SpAttackServiceDist = SpAttackServiceDist
		self.SpAttackServiceTime = SpAttackServiceTime
		self.SpAttackServiceAngle = SpAttackServiceAngle
		self.TurnCheckDist = TurnCheckDist
		self.TurnCheckHeight = TurnCheckHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class BossBattleRoomRoot:

	def __init__(self, Name, TitleAngle, RollAngle, FramesRotate, FramesReset, FramesRoll, FramesDelayRoll, FramesRollKeepFirst, FramesRollKeepSecond, NumTimesRoll, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TitleAngle = TitleAngle
		self.RollAngle = RollAngle
		self.FramesRotate = FramesRotate
		self.FramesReset = FramesReset
		self.FramesRoll = FramesRoll
		self.FramesDelayRoll = FramesDelayRoll
		self.FramesRollKeepFirst = FramesRollKeepFirst
		self.FramesRollKeepSecond = FramesRollKeepSecond
		self.NumTimesRoll = NumTimesRoll


class BowEquiped:
	ChildNames = ["射撃", "装備"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class BowShoot:
	ChildNames = ["リロード", "溜め", "発射", "空撃ち"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class BowlPin:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機", "ピンと衝突", "雪玉と衝突"]

	def __init__(self, Name, Degree, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Degree = Degree
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class BoxWaterRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BreathAttackEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1


class BreathEnemyRangeKeepMove:
	ChildNames = ["ブレス終了", "ブレス開始", "強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動"]

	def __init__(self, Name, BreathName, AttackRatio, BreathSize, EnlargeTime, BaseNode, LoopTime, BreathEndDist, BreathMinTime, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BreathName = BreathName
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.BaseNode = BaseNode
		self.LoopTime = LoopTime
		self.BreathEndDist = BreathEndDist
		self.BreathMinTime = BreathMinTime
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class CalledEnemyMove:
	ChildNames = ["待機", "近づき"]

	def __init__(self, Name, LostDist, WaitDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostDist = LostDist
		self.WaitDist = WaitDist
		self.Child0 = Child0
		self.Child1 = Child1


class CameraBow:
	ChildNames = ["弓ズームカメラ", "弓注目魔獣ガノンカメラ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class CameraEditRoot:
	ChildNames = ["Default", "DefaultIndoor_031", "DnugeonMove", "Dungeon", "InHouse", "LostWoods_031", "MapTower_031"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class CameraEventReturnSavePoint:
	ChildNames = ["エラー", "デフォルト", "会話"]

	def __init__(self, Name, SavePoint, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SavePoint = SavePoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CameraEventTalkAI:
	ChildNames = ["オート", "マニュアル"]

	def __init__(self, Name, HeightOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeightOffset = HeightOffset
		self.Child0 = Child0
		self.Child1 = Child1


class CameraEventTalkAIRet:
	ChildNames = ["オート", "マニュアル"]

	def __init__(self, Name, HeightOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeightOffset = HeightOffset
		self.Child0 = Child0
		self.Child1 = Child1


class CameraGameRoot:
	ChildNames = ["イベント用_会話", "イベント用_会話水中用", "イベント用_看板", "イベント用_記録したカメラに戻る", "ルートAI"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class CameraRoot:
	ChildNames = ["アイテムカメラ", "カメラアプリカメラ", "カメラアプリ自撮りカメラ", "ゴーレム掴まりカメラ", "スナザラシカメラ", "ゾーラプリンスアイテムカメラ", "ゾーラプリンスカメラ", "ゾーラプリンス弓カメラ", "ゾーラプリンス注目カメラ", "ゾーラプリンス滝登りカメラ", "ゾーラプリンス長距離射程弓カメラ", "ツールカメラ", "マグネキャッチカメラ", "不完全体ガノン壁注目カメラ", "中型敵用注目カメラ", "奈落カメラ", "巨大敵用ロックオンカメラ", "弓カメラ", "水の神獣咆哮カメラ", "泳ぎカメラ", "泳ぎ注目カメラ", "滝登りカメラ", "現状維持カメラ", "盾サーフィンカメラ", "遺物戦用スナザラシカメラ", "馬ガーディアン注目カメラ", "馬ロデオカメラ", "馬弓カメラ", "馬弓注目カメラ", "馬弓注目魔獣ガノンカメラ", "馬弓空注目カメラ", "馬望遠鏡カメラ", "馬注目カメラ", "馬空注目カメラ", "馬通常カメラ", "馬長距離射程弓カメラ"]

	def __init__(self, Name, sideOffsetBowCus, guardianDist, guardianAngle, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Child19, Child20, Child21, Child22, Child23, Child24, Child25, Child26, Child27, Child28, Child29, Child30, Child31, Child32, Child33, Child34, Child35, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.sideOffsetBowCus = sideOffsetBowCus
		self.guardianDist = guardianDist
		self.guardianAngle = guardianAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18
		self.Child19 = Child19
		self.Child20 = Child20
		self.Child21 = Child21
		self.Child22 = Child22
		self.Child23 = Child23
		self.Child24 = Child24
		self.Child25 = Child25
		self.Child26 = Child26
		self.Child27 = Child27
		self.Child28 = Child28
		self.Child29 = Child29
		self.Child30 = Child30
		self.Child31 = Child31
		self.Child32 = Child32
		self.Child33 = Child33
		self.Child34 = Child34
		self.Child35 = Child35


class CameraTool:
	ChildNames = ["DefaultIndoorNormal", "DefaultLockOn", "DefaultNormal", "DefaultNormalSubject", "DefaultWall", "DungeonMove", "DungeonNormal", "InHouseNormal", "LostWoodsNormal", "MapTowerNormal_031a", "デフォルト弓カメラ", "デフォルト弓屈みカメラ", "デフォルト弓注目カメラ", "マップ塔弓カメラ", "マップ塔弓屈みカメラ", "マップ塔弓注目カメラ"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class CannonBallRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class CapturedActDeadSelector:
	ChildNames = ["ドロップ", "手置き", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CapturedActorReaction:
	ChildNames = ["怨念", "死亡", "死亡後ダメージ", "消滅"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class CapturedActorReactionChemical:
	ChildNames = ["凍結", "感電", "通常"]

	def __init__(self, Name, OnEnterOnly, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CarryBox:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CastleLynelBattle:
	ChildNames = ["6足攻撃", "ブレス", "咆哮攻撃", "弓装備", "斬り抜け", "突進切り", "近接戦闘"]

	def __init__(self, Name, CloseBattleStartDist, CloseBattleStartAngle, WeaponIdx, HornAttackRate, RoarRate, BreathStartLifeRate, RoarStartLifeRate, BattleEndDist, RoarFlamePartsKey, BreathPartsKey0, BreathPartsKey1, BreathPartsKey2, CloseBattleRepeatMax, ThroughAttackRepeatNum, SkipBreathRoarRate, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseBattleStartDist = CloseBattleStartDist
		self.CloseBattleStartAngle = CloseBattleStartAngle
		self.WeaponIdx = WeaponIdx
		self.HornAttackRate = HornAttackRate
		self.RoarRate = RoarRate
		self.BreathStartLifeRate = BreathStartLifeRate
		self.RoarStartLifeRate = RoarStartLifeRate
		self.BattleEndDist = BattleEndDist
		self.RoarFlamePartsKey = RoarFlamePartsKey
		self.BreathPartsKey0 = BreathPartsKey0
		self.BreathPartsKey1 = BreathPartsKey1
		self.BreathPartsKey2 = BreathPartsKey2
		self.CloseBattleRepeatMax = CloseBattleRepeatMax
		self.ThroughAttackRepeatNum = ThroughAttackRepeatNum
		self.SkipBreathRoarRate = SkipBreathRoarRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class ChangeWeatherTagRoot:
	ChildNames = ["通知"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class ChangeWindTagRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChaseSound:
	ChildNames = ["回転", "直線追跡", "見まわす", "近場追跡", "遠方追跡"]

	def __init__(self, Name, NearDist, TargetUpdateIntervalMin, TargetUpdateIntervalMax, TurnDir, UseViewPointSimpleOffset, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDist = NearDist
		self.TargetUpdateIntervalMin = TargetUpdateIntervalMin
		self.TargetUpdateIntervalMax = TargetUpdateIntervalMax
		self.TurnDir = TurnDir
		self.UseViewPointSimpleOffset = UseViewPointSimpleOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class ChemicalEnemyFindPlayer:
	ChildNames = ["ケミカル仲間招来", "ケミカル攻撃", "ナビメッシュ無し", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "武器ケミカル付与", "武器投げ", "気づき", "速攻"]

	def __init__(self, Name, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, ChemicalSearchDist, NoSearchDist, Voltage, ChemicalActionDist, ThrowWeaponPer, ThrowWeaponDist, NoChemSearchWpIdx, NoBurnWaterDepth, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.ChemicalSearchDist = ChemicalSearchDist
		self.NoSearchDist = NoSearchDist
		self.Voltage = Voltage
		self.ChemicalActionDist = ChemicalActionDist
		self.ThrowWeaponPer = ThrowWeaponPer
		self.ThrowWeaponDist = ThrowWeaponDist
		self.NoChemSearchWpIdx = NoChemSearchWpIdx
		self.NoBurnWaterDepth = NoBurnWaterDepth
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class ChemicalEnemyRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, IsElementNoHit, IsElectricWater, ColorASName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsElementNoHit = IsElementNoHit
		self.IsElectricWater = IsElectricWater
		self.ColorASName = ColorASName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class ChemicalExplode:
	ChildNames = ["爆破", "爆破予約"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ChemicalGiantArmorRoot:
	ChildNames = ["装備", "非装備"]

	def __init__(self, Name, ElectricDamageScale, ElectricTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ElectricDamageScale = ElectricDamageScale
		self.ElectricTime = ElectricTime
		self.Child0 = Child0
		self.Child1 = Child1


class ChemicalStayObjectRoot:
	ChildNames = ["強制消滅", "自然消滅", "通常"]

	def __init__(self, Name, IsCheckDelete, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckDelete = IsCheckDelete
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ChemicalWeaponRoot:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class ChildDeviceReflectArrow:
	ChildNames = ["刺さる", "所持", "爆発", "発射"]

	def __init__(self, Name, ReflectCountMax, ReflectAimSpeed, ReflectAccel, Accel, AimSpeed, FallAccel, FallAimSpeed, Gravity, AtRange, AtImpulse, AtImpact, CanReflect, IsReflectToParent, ReflectOffset, RotOffset, IsDelete, AtAttr, IsBreakIceBlock, StickTime, IsAtHitPlayerIgnore, ReflectDamageRate, TransOffset, BindNodeName, IsDeleteAtHit, CallHitSEKey, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReflectCountMax = ReflectCountMax
		self.ReflectAimSpeed = ReflectAimSpeed
		self.ReflectAccel = ReflectAccel
		self.Accel = Accel
		self.AimSpeed = AimSpeed
		self.FallAccel = FallAccel
		self.FallAimSpeed = FallAimSpeed
		self.Gravity = Gravity
		self.AtRange = AtRange
		self.AtImpulse = AtImpulse
		self.AtImpact = AtImpact
		self.CanReflect = CanReflect
		self.IsReflectToParent = IsReflectToParent
		self.ReflectOffset = ReflectOffset
		self.RotOffset = RotOffset
		self.IsDelete = IsDelete
		self.AtAttr = AtAttr
		self.IsBreakIceBlock = IsBreakIceBlock
		self.StickTime = StickTime
		self.IsAtHitPlayerIgnore = IsAtHitPlayerIgnore
		self.ReflectDamageRate = ReflectDamageRate
		self.TransOffset = TransOffset
		self.BindNodeName = BindNodeName
		self.IsDeleteAtHit = IsDeleteAtHit
		self.CallHitSEKey = CallHitSEKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ChildFavoriteSelector:
	ChildNames = ["成立", "非成立"]

	def __init__(self, Name, IsNoChildForceEnd, IsCheckEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsNoChildForceEnd = IsNoChildForceEnd
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class ChildHaveSelect:
	ChildNames = ["子所持", "非子所持"]

	def __init__(self, Name, IsCheckEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class ChmCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, ChmType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChmType = ChmType
		self.Child0 = Child0
		self.Child1 = Child1


class ChmVolRateCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, VolTh, DebugDraw, IsInvalidBreakJudge, DebugScale, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VolTh = VolTh
		self.DebugDraw = DebugDraw
		self.IsInvalidBreakJudge = IsInvalidBreakJudge
		self.DebugScale = DebugScale
		self.Child0 = Child0
		self.Child1 = Child1


class ChmVolRateCheckBlankOk:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, VolTh, DebugDraw, IsInvalidBreakJudge, DebugScale, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VolTh = VolTh
		self.DebugDraw = DebugDraw
		self.IsInvalidBreakJudge = IsInvalidBreakJudge
		self.DebugScale = DebugScale
		self.Child0 = Child0
		self.Child1 = Child1


class ChuchuDieSelect:
	ChildNames = ["ケミカル放射", "凍死", "凍特効死", "凍結砕き", "感電死", "死亡", "消滅", "溺死", "濡死", "焼死", "焼特効死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class ChuchuJellyRoot:
	ChildNames = ["リアクション", "通常"]

	def __init__(self, Name, AtHitImpulseRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtHitImpulseRate = AtHitImpulseRate
		self.Child0 = Child0
		self.Child1 = Child1


class ChuchuNavMoveTarget:
	ChildNames = ["ジャンプ", "直進", "移動", "見まわす"]

	def __init__(self, Name, WallHitTime, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, UseCharacterRadius, VibrateCheckTime, RotVibrateCheckTime, IsLastLineReachCheck, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WallHitTime = WallHitTime
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.UseCharacterRadius = UseCharacterRadius
		self.VibrateCheckTime = VibrateCheckTime
		self.RotVibrateCheckTime = RotVibrateCheckTime
		self.IsLastLineReachCheck = IsLastLineReachCheck
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ChuchuRoot:
	ChildNames = ["ドロップ生成", "リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, SubAS, SubASSlot, ChemicalFieldKey, ChemicalScaleTime, ClothStiffness30, ClothStiffness20, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.ChemicalFieldKey = ChemicalFieldKey
		self.ChemicalScaleTime = ChemicalScaleTime
		self.ClothStiffness30 = ClothStiffness30
		self.ClothStiffness20 = ClothStiffness20
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class ChuchuTypeSelect:
	ChildNames = ["アイス", "エレキ", "ノーマル", "ファイア"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class CircleMoveFlying:
	ChildNames = ["移動"]

	def __init__(self, Name, IsCheckSafetyAreaRadius, IsUseHomePos, Speed, RadiusX, RadiusZ, MinRandRadiusRate, MaxRandRadiusRate, AddAngleRateX, AddAngleRateZ, RandRangeY, RandRangeYOffest, LimitSpeedMoveY, ChangeInterval, RandChangeInterval, ReverseMoveRate, IsSetSystemDeleteDistance, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckSafetyAreaRadius = IsCheckSafetyAreaRadius
		self.IsUseHomePos = IsUseHomePos
		self.Speed = Speed
		self.RadiusX = RadiusX
		self.RadiusZ = RadiusZ
		self.MinRandRadiusRate = MinRandRadiusRate
		self.MaxRandRadiusRate = MaxRandRadiusRate
		self.AddAngleRateX = AddAngleRateX
		self.AddAngleRateZ = AddAngleRateZ
		self.RandRangeY = RandRangeY
		self.RandRangeYOffest = RandRangeYOffest
		self.LimitSpeedMoveY = LimitSpeedMoveY
		self.ChangeInterval = ChangeInterval
		self.RandChangeInterval = RandChangeInterval
		self.ReverseMoveRate = ReverseMoveRate
		self.IsSetSystemDeleteDistance = IsSetSystemDeleteDistance
		self.Child0 = Child0


class CircleMoveInWater:
	ChildNames = ["移動"]

	def __init__(self, Name, AllowMoveWaterDepth, Speed, RadiusX, RadiusZ, MinRandRadiusRate, MaxRandRadiusRate, AddAngleRateX, AddAngleRateZ, RandRangeY, RandRangeYOffest, LimitSpeedMoveY, ChangeInterval, RandChangeInterval, ReverseMoveRate, IsSetSystemDeleteDistance, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AllowMoveWaterDepth = AllowMoveWaterDepth
		self.Speed = Speed
		self.RadiusX = RadiusX
		self.RadiusZ = RadiusZ
		self.MinRandRadiusRate = MinRandRadiusRate
		self.MaxRandRadiusRate = MaxRandRadiusRate
		self.AddAngleRateX = AddAngleRateX
		self.AddAngleRateZ = AddAngleRateZ
		self.RandRangeY = RandRangeY
		self.RandRangeYOffest = RandRangeYOffest
		self.LimitSpeedMoveY = LimitSpeedMoveY
		self.ChangeInterval = ChangeInterval
		self.RandChangeInterval = RandChangeInterval
		self.ReverseMoveRate = ReverseMoveRate
		self.IsSetSystemDeleteDistance = IsSetSystemDeleteDistance
		self.Child0 = Child0


class CircleMovePos:
	ChildNames = ["移動", "近づき", "遠ざかり"]

	def __init__(self, Name, Radius, RadiusMargin, Speed, Direction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.RadiusMargin = RadiusMargin
		self.Speed = Speed
		self.Direction = Direction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CircleMoveTarget:
	ChildNames = ["移動", "近づき", "遠ざかり"]

	def __init__(self, Name, Radius, RadiusMargin, Speed, Direction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.RadiusMargin = RadiusMargin
		self.Speed = Speed
		self.Direction = Direction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CliffCheckSelect:
	ChildNames = ["崖である", "崖でない"]

	def __init__(self, Name, CheckDist, CheckAngle, IsSelectFirstTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.CheckAngle = CheckAngle
		self.IsSelectFirstTime = IsSelectFirstTime
		self.Child0 = Child0
		self.Child1 = Child1


class CliffCheckTargetDirSelect:
	ChildNames = ["崖である", "崖でない"]

	def __init__(self, Name, CheckDist, CheckAngle, IsSelectFirstTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.CheckAngle = CheckAngle
		self.IsSelectFirstTime = IsSelectFirstTime
		self.Child0 = Child0
		self.Child1 = Child1


class CliffCheckToTargetPosDirSelect:
	ChildNames = ["崖である", "崖でない"]

	def __init__(self, Name, CheckDist, CheckAngle, IsSelectFirstTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.CheckAngle = CheckAngle
		self.IsSelectFirstTime = IsSelectFirstTime
		self.Child0 = Child0
		self.Child1 = Child1


class CliffDistanceSelectThreeAction:
	ChildNames = ["崖である", "崖でない", "崖近距離"]

	def __init__(self, Name, CheckDist, NearCliffDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.NearCliffDist = NearCliffDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class CloseSmallAttack:
	ChildNames = ["ステップ", "小攻撃"]

	def __init__(self, Name, CloseRadius, WeaponIdx, IsIgnoreSmallHit, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseRadius = CloseRadius
		self.WeaponIdx = WeaponIdx
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.Child0 = Child0
		self.Child1 = Child1


class ClusterRenderCheckTag:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ColGroundHitSelect:
	ChildNames = ["地上", "空中"]

	def __init__(self, Name, IsCheckEachFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckEachFrame = IsCheckEachFrame
		self.Child0 = Child0
		self.Child1 = Child1


class CollaborationShootingStarRoot:
	ChildNames = ["光の柱を出す", "飛んでいく"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class CommonPickedItem:
	ChildNames = ["サブボタン", "メインボタン", "消滅", "通常"]

	def __init__(self, Name, CanGetOnBurning, GetAttKeyName, IsControlNoticeDo, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CanGetOnBurning = CanGetOnBurning
		self.GetAttKeyName = GetAttKeyName
		self.IsControlNoticeDo = IsControlNoticeDo
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ConditionMoveActionSelect:
	ChildNames = ["条件失敗", "条件成功"]

	def __init__(self, Name, CheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckLineReachable = CheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class CookPotRoot:
	ChildNames = ["待機", "着火"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class CountSelect:
	ChildNames = ["以前", "以後"]

	def __init__(self, Name, Counter, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Counter = Counter
		self.Child0 = Child0
		self.Child1 = Child1


class CreateCarryActor:
	ChildNames = ["生成", "生成中"]

	def __init__(self, Name, ActorName, CreatePriorityState, Scale, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorName = ActorName
		self.CreatePriorityState = CreatePriorityState
		self.Scale = Scale
		self.Child0 = Child0
		self.Child1 = Child1


class CreateOnFaceSelect:
	ChildNames = ["表面生成", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DamageAttrSelect:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, KeyAttribute, Option, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeyAttribute = KeyAttribute
		self.Option = Option
		self.Child0 = Child0
		self.Child1 = Child1


class DamageTypeSelect:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, DamageType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DamageType = DamageType
		self.Child0 = Child0
		self.Child1 = Child1


class DangerAvoidFlagSelect:
	ChildNames = ["通常", "避ける"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DashAndAttack:
	ChildNames = ["斬り付け", "駆け寄り"]

	def __init__(self, Name, OffsetLR, WeaponIdx, AttackRange, AttackFrame, TiredAngle, IsAbleSkipNear, TargetSpeedClampMax, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetLR = OffsetLR
		self.WeaponIdx = WeaponIdx
		self.AttackRange = AttackRange
		self.AttackFrame = AttackFrame
		self.TiredAngle = TiredAngle
		self.IsAbleSkipNear = IsAbleSkipNear
		self.TargetSpeedClampMax = TargetSpeedClampMax
		self.Child0 = Child0
		self.Child1 = Child1


class DeadOrOtherState:
	ChildNames = ["その他", "死亡"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DeadlyBlowWeaponRoot:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class DefWanderAI:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, ChangeWaitRate, MaxWaitTime, MinWaitTime, FinishChangeCount, CheckWaitIsChangable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeWaitRate = ChangeWaitRate
		self.MaxWaitTime = MaxWaitTime
		self.MinWaitTime = MinWaitTime
		self.FinishChangeCount = FinishChangeCount
		self.CheckWaitIsChangable = CheckWaitIsChangable
		self.Child0 = Child0
		self.Child1 = Child1


class DemoRailMoveRemains:
	ChildNames = ["一時停止", "停止", "再稼働", "移動"]

	def __init__(self, Name, ReactivateTime, FrontCheckMinDist, FrontDirUpdateInterval, SpeedScale, InitPosByRailRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactivateTime = ReactivateTime
		self.FrontCheckMinDist = FrontCheckMinDist
		self.FrontDirUpdateInterval = FrontDirUpdateInterval
		self.SpeedScale = SpeedScale
		self.InitPosByRailRatio = InitPosByRailRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class DemoRootAI:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_CWRotDirSwitch:
	ChildNames = ["False", "True"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DgnObj_DLC_CW_WithEntityBody00:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, CorrectConstraint, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CorrectConstraint = CorrectConstraint
		self.Child0 = Child0
		self.Child1 = Child1


class DgnObj_DLC_CogWheel2:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, CorrectConstraint, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CorrectConstraint = CorrectConstraint
		self.Child0 = Child0
		self.Child1 = Child1


class DgnObj_DLC_CogWheel_Physics_Ctr:
	ChildNames = ["atk有効", "無効"]

	def __init__(self, Name, StateRot, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StateRot = StateRot
		self.Child0 = Child0
		self.Child1 = Child1


class DgnObj_DLC_DungeonRotateTag:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DgnObj_DLC_Faucet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_SliderBlock:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DieSelect:
	ChildNames = ["凍結砕き", "死亡", "消滅", "溺死", "濡死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class DieSelectBombPlus:
	ChildNames = ["凍結砕き", "死亡", "消滅", "溺死", "濡死", "爆死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class DieSelectChemShockPlus:
	ChildNames = ["ショック死", "凍死", "凍特効死", "凍結砕き", "感電死", "死亡", "消滅", "溺死", "濡死", "焼死", "焼特効死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class DieSelectChemicalPlus:
	ChildNames = ["凍死", "凍特効死", "凍結砕き", "感電死", "死亡", "消滅", "溺死", "濡死", "焼死", "焼特効死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class DisplaySelect:
	ChildNames = ["画面内", "画面外"]

	def __init__(self, Name, Radius, IsCheckEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class DistanceKeepMove:
	ChildNames = ["待機", "後退", "近づき"]

	def __init__(self, Name, StartBackDistOffset, WeaponIdx, BaseDist, StartCloseDistOffset, OutDistOffset, IsCheckLineReachableForClose, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartBackDistOffset = StartBackDistOffset
		self.WeaponIdx = WeaponIdx
		self.BaseDist = BaseDist
		self.StartCloseDistOffset = StartCloseDistOffset
		self.OutDistOffset = OutDistOffset
		self.IsCheckLineReachableForClose = IsCheckLineReachableForClose
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DistanceLostCheck:
	ChildNames = ["発見行動"]

	def __init__(self, Name, LostTimer, LostRange, AddAwarenessRangeType, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.AddAwarenessRangeType = AddAwarenessRangeType
		self.Child0 = Child0


class DoChangeOneTime:
	ChildNames = ["Off待機", "Off起動", "On待機", "On起動"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class DogNormal:
	ChildNames = ["なつき", "ふり向き", "よろけ", "ターゲット通知", "ダメージ逃走", "ロケーター待機", "威嚇", "宝まで誘導", "帰還", "徘徊", "戦闘", "最後の手段", "気づき", "注目", "興味対象発見", "逃走"]

	def __init__(self, Name, MaxFollowDist, MaxFollowFriendDecayRate, FoodFriendRate, FoodFriendDist, NearFriendRate, NearFriendDist, FarFriendDecayRate, FarFriendDist, FarFriendFriendlyDist, AttackFriendDecayRate, FriendTickRate, NoMoveFriendDecayRate, NoMoveThreshold, FramesKeepMaxFriendly, FramesStayAfterLead, NumFriendlyFoodForLeadTreasure, AngleTurnToPlayer, DistUntilReturnToHomePos, WaitFramesAfterRunMin, WaitFramesAfterRunMax, StaggerVelocityThreshold, DistHomePosFadeout, NumFailPathHomeFadeout, IsUseEscapeState, IsPositiveAttacker, IsSearchTarget, IsEmitForceEscapeSignal, IsReceivedForceEscapeSignal, IsCheckSandStorm, ChangeBattleStateRadius, CounterAttackRadius, CounterAttackRate, AddCautionLevelVal, AutoReduceCautionLevelVal, LimitOverReduceCautionLevelVal, AwnRangeScaleWhenAttention, TargetLostTime, AllowRoarRadius, EscapeWaterFlowLimit, NewFoodAddTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxFollowDist = MaxFollowDist
		self.MaxFollowFriendDecayRate = MaxFollowFriendDecayRate
		self.FoodFriendRate = FoodFriendRate
		self.FoodFriendDist = FoodFriendDist
		self.NearFriendRate = NearFriendRate
		self.NearFriendDist = NearFriendDist
		self.FarFriendDecayRate = FarFriendDecayRate
		self.FarFriendDist = FarFriendDist
		self.FarFriendFriendlyDist = FarFriendFriendlyDist
		self.AttackFriendDecayRate = AttackFriendDecayRate
		self.FriendTickRate = FriendTickRate
		self.NoMoveFriendDecayRate = NoMoveFriendDecayRate
		self.NoMoveThreshold = NoMoveThreshold
		self.FramesKeepMaxFriendly = FramesKeepMaxFriendly
		self.FramesStayAfterLead = FramesStayAfterLead
		self.NumFriendlyFoodForLeadTreasure = NumFriendlyFoodForLeadTreasure
		self.AngleTurnToPlayer = AngleTurnToPlayer
		self.DistUntilReturnToHomePos = DistUntilReturnToHomePos
		self.WaitFramesAfterRunMin = WaitFramesAfterRunMin
		self.WaitFramesAfterRunMax = WaitFramesAfterRunMax
		self.StaggerVelocityThreshold = StaggerVelocityThreshold
		self.DistHomePosFadeout = DistHomePosFadeout
		self.NumFailPathHomeFadeout = NumFailPathHomeFadeout
		self.IsUseEscapeState = IsUseEscapeState
		self.IsPositiveAttacker = IsPositiveAttacker
		self.IsSearchTarget = IsSearchTarget
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.IsReceivedForceEscapeSignal = IsReceivedForceEscapeSignal
		self.IsCheckSandStorm = IsCheckSandStorm
		self.ChangeBattleStateRadius = ChangeBattleStateRadius
		self.CounterAttackRadius = CounterAttackRadius
		self.CounterAttackRate = CounterAttackRate
		self.AddCautionLevelVal = AddCautionLevelVal
		self.AutoReduceCautionLevelVal = AutoReduceCautionLevelVal
		self.LimitOverReduceCautionLevelVal = LimitOverReduceCautionLevelVal
		self.AwnRangeScaleWhenAttention = AwnRangeScaleWhenAttention
		self.TargetLostTime = TargetLostTime
		self.AllowRoarRadius = AllowRoarRadius
		self.EscapeWaterFlowLimit = EscapeWaterFlowLimit
		self.NewFoodAddTime = NewFoodAddTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class DomesticNormal:
	ChildNames = ["ふり向き", "よろけ", "ターゲット通知", "ダメージ逃走", "ロケーター待機", "威嚇", "帰還", "徘徊", "戦闘", "最後の手段", "気づき", "注目", "興味対象発見", "逃走"]

	def __init__(self, Name, DistUntilReturnToHomePos, WaitFramesAfterRunMin, WaitFramesAfterRunMax, StaggerVelocityThreshold, DistHomePosFadeout, NumFailPathHomeFadeout, IsUseEscapeState, IsPositiveAttacker, IsSearchTarget, IsEmitForceEscapeSignal, IsReceivedForceEscapeSignal, IsCheckSandStorm, ChangeBattleStateRadius, CounterAttackRadius, CounterAttackRate, AddCautionLevelVal, AutoReduceCautionLevelVal, LimitOverReduceCautionLevelVal, AwnRangeScaleWhenAttention, TargetLostTime, AllowRoarRadius, EscapeWaterFlowLimit, NewFoodAddTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistUntilReturnToHomePos = DistUntilReturnToHomePos
		self.WaitFramesAfterRunMin = WaitFramesAfterRunMin
		self.WaitFramesAfterRunMax = WaitFramesAfterRunMax
		self.StaggerVelocityThreshold = StaggerVelocityThreshold
		self.DistHomePosFadeout = DistHomePosFadeout
		self.NumFailPathHomeFadeout = NumFailPathHomeFadeout
		self.IsUseEscapeState = IsUseEscapeState
		self.IsPositiveAttacker = IsPositiveAttacker
		self.IsSearchTarget = IsSearchTarget
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.IsReceivedForceEscapeSignal = IsReceivedForceEscapeSignal
		self.IsCheckSandStorm = IsCheckSandStorm
		self.ChangeBattleStateRadius = ChangeBattleStateRadius
		self.CounterAttackRadius = CounterAttackRadius
		self.CounterAttackRate = CounterAttackRate
		self.AddCautionLevelVal = AddCautionLevelVal
		self.AutoReduceCautionLevelVal = AutoReduceCautionLevelVal
		self.LimitOverReduceCautionLevelVal = LimitOverReduceCautionLevelVal
		self.AwnRangeScaleWhenAttention = AwnRangeScaleWhenAttention
		self.TargetLostTime = TargetLostTime
		self.AllowRoarRadius = AllowRoarRadius
		self.EscapeWaterFlowLimit = EscapeWaterFlowLimit
		self.NewFoodAddTime = NewFoodAddTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class DominoRoot:
	ChildNames = ["倒れる", "待機"]

	def __init__(self, Name, PointVelTh, LinearRate, AngRate, CheckHeightRate, IsIgnoreWater, Friction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PointVelTh = PointVelTh
		self.LinearRate = LinearRate
		self.AngRate = AngRate
		self.CheckHeightRate = CheckHeightRate
		self.IsIgnoreWater = IsIgnoreWater
		self.Friction = Friction
		self.Child0 = Child0
		self.Child1 = Child1


class DoorRoot:
	ChildNames = ["Close", "Open", "Wait"]

	def __init__(self, Name, Open_L_AS, Open_R_AS, Close_L_AS, Close_R_AS, CloseWaitFrame, IsCheckBack, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Open_L_AS = Open_L_AS
		self.Open_R_AS = Open_R_AS
		self.Close_L_AS = Close_L_AS
		self.Close_R_AS = Close_R_AS
		self.CloseWaitFrame = CloseWaitFrame
		self.IsCheckBack = IsCheckBack
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DoubtItemSubTargetSelect:
	ChildNames = ["あった", "なかった"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DragonDropItemTargetRootAI:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DragonElecRoot:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "帰還", "移動"]

	def __init__(self, Name, OnRailDistance, FarDistance, Speed, CommonTableName, TsunoTableName, TsumeTableName, KibaTableName, IsEmitChemical, ChemicalBulletActor, ChemicalBulletArea, ChemicalBulletRate, ChemicalBulletNum, ChemicalWindArea, ChemicalWindPower, ChemicalWindLimitHeight, UpdraftPower, UpdraftTime, UpdraftInterval, UpdraftBoost, ReturnTime, BodyHitDamage, BodyHitPower, BodyHitImpact, BodyHitShieldDamage, InitBackRailDistance, DefaultMaterialAnmName, HornAnmName, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.CommonTableName = CommonTableName
		self.TsunoTableName = TsunoTableName
		self.TsumeTableName = TsumeTableName
		self.KibaTableName = KibaTableName
		self.IsEmitChemical = IsEmitChemical
		self.ChemicalBulletActor = ChemicalBulletActor
		self.ChemicalBulletArea = ChemicalBulletArea
		self.ChemicalBulletRate = ChemicalBulletRate
		self.ChemicalBulletNum = ChemicalBulletNum
		self.ChemicalWindArea = ChemicalWindArea
		self.ChemicalWindPower = ChemicalWindPower
		self.ChemicalWindLimitHeight = ChemicalWindLimitHeight
		self.UpdraftPower = UpdraftPower
		self.UpdraftTime = UpdraftTime
		self.UpdraftInterval = UpdraftInterval
		self.UpdraftBoost = UpdraftBoost
		self.ReturnTime = ReturnTime
		self.BodyHitDamage = BodyHitDamage
		self.BodyHitPower = BodyHitPower
		self.BodyHitImpact = BodyHitImpact
		self.BodyHitShieldDamage = BodyHitShieldDamage
		self.InitBackRailDistance = InitBackRailDistance
		self.DefaultMaterialAnmName = DefaultMaterialAnmName
		self.HornAnmName = HornAnmName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class DragonFireRoot:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "帰還", "移動"]

	def __init__(self, Name, OnRailDistance, FarDistance, Speed, CommonTableName, TsunoTableName, TsumeTableName, KibaTableName, IsEmitChemical, ChemicalBulletActor, ChemicalBulletArea, ChemicalBulletRate, ChemicalBulletNum, ChemicalWindArea, ChemicalWindPower, ChemicalWindLimitHeight, UpdraftPower, UpdraftTime, UpdraftInterval, UpdraftBoost, ReturnTime, BodyHitDamage, BodyHitPower, BodyHitImpact, BodyHitShieldDamage, InitBackRailDistance, DefaultMaterialAnmName, HornAnmName, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.CommonTableName = CommonTableName
		self.TsunoTableName = TsunoTableName
		self.TsumeTableName = TsumeTableName
		self.KibaTableName = KibaTableName
		self.IsEmitChemical = IsEmitChemical
		self.ChemicalBulletActor = ChemicalBulletActor
		self.ChemicalBulletArea = ChemicalBulletArea
		self.ChemicalBulletRate = ChemicalBulletRate
		self.ChemicalBulletNum = ChemicalBulletNum
		self.ChemicalWindArea = ChemicalWindArea
		self.ChemicalWindPower = ChemicalWindPower
		self.ChemicalWindLimitHeight = ChemicalWindLimitHeight
		self.UpdraftPower = UpdraftPower
		self.UpdraftTime = UpdraftTime
		self.UpdraftInterval = UpdraftInterval
		self.UpdraftBoost = UpdraftBoost
		self.ReturnTime = ReturnTime
		self.BodyHitDamage = BodyHitDamage
		self.BodyHitPower = BodyHitPower
		self.BodyHitImpact = BodyHitImpact
		self.BodyHitShieldDamage = BodyHitShieldDamage
		self.InitBackRailDistance = InitBackRailDistance
		self.DefaultMaterialAnmName = DefaultMaterialAnmName
		self.HornAnmName = HornAnmName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class DragonIceRoot:
	ChildNames = ["ラネール山頂からの帰還予備動作", "ラネール山頂から移動開始", "ラネール山頂から空へ", "ラネール山頂へ帰還", "ラネール山頂待機", "レールに向かう", "停止", "停止点移動", "帰還", "移動"]

	def __init__(self, Name, GrudgeEventRail_Start, GrudgeEventRail_pre1st, GrudgeEventRail_1st, GrudgeEventRail_pre2nd, GrudgeEventRail_2nd, GrudgeEventRail_pre3rd, GrudgeEventRail_3rd, GrudgeEventRail_preEnd, GrudgeEventRail_End, GrudgeEventRail_ReturnToSky, GrudgeEventRail_pre1stSpeed, GrudgeEventRail_1stSpeed, GrudgeEventRail_pre2ndSpeed, GrudgeEventRail_2ndSpeed, GrudgeEventRail_pre3rdSpeed, GrudgeEventRail_3rdSpeed, GrudgeEventRail_preEndSpeed, GrudgeEventRail_EndSpeed, GrudgeEventRail_ReturnSpeed, GrudgeBulletRate, GrudgeBulletMaxNum, GrudgeBulletMinInterval, GrudgeBulletActorName, GrudgeSmokeTime, OnRailDistance, FarDistance, Speed, CommonTableName, TsunoTableName, TsumeTableName, KibaTableName, IsEmitChemical, ChemicalBulletActor, ChemicalBulletArea, ChemicalBulletRate, ChemicalBulletNum, ChemicalWindArea, ChemicalWindPower, ChemicalWindLimitHeight, UpdraftPower, UpdraftTime, UpdraftInterval, UpdraftBoost, ReturnTime, BodyHitDamage, BodyHitPower, BodyHitImpact, BodyHitShieldDamage, InitBackRailDistance, DefaultMaterialAnmName, HornAnmName, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrudgeEventRail_Start = GrudgeEventRail_Start
		self.GrudgeEventRail_pre1st = GrudgeEventRail_pre1st
		self.GrudgeEventRail_1st = GrudgeEventRail_1st
		self.GrudgeEventRail_pre2nd = GrudgeEventRail_pre2nd
		self.GrudgeEventRail_2nd = GrudgeEventRail_2nd
		self.GrudgeEventRail_pre3rd = GrudgeEventRail_pre3rd
		self.GrudgeEventRail_3rd = GrudgeEventRail_3rd
		self.GrudgeEventRail_preEnd = GrudgeEventRail_preEnd
		self.GrudgeEventRail_End = GrudgeEventRail_End
		self.GrudgeEventRail_ReturnToSky = GrudgeEventRail_ReturnToSky
		self.GrudgeEventRail_pre1stSpeed = GrudgeEventRail_pre1stSpeed
		self.GrudgeEventRail_1stSpeed = GrudgeEventRail_1stSpeed
		self.GrudgeEventRail_pre2ndSpeed = GrudgeEventRail_pre2ndSpeed
		self.GrudgeEventRail_2ndSpeed = GrudgeEventRail_2ndSpeed
		self.GrudgeEventRail_pre3rdSpeed = GrudgeEventRail_pre3rdSpeed
		self.GrudgeEventRail_3rdSpeed = GrudgeEventRail_3rdSpeed
		self.GrudgeEventRail_preEndSpeed = GrudgeEventRail_preEndSpeed
		self.GrudgeEventRail_EndSpeed = GrudgeEventRail_EndSpeed
		self.GrudgeEventRail_ReturnSpeed = GrudgeEventRail_ReturnSpeed
		self.GrudgeBulletRate = GrudgeBulletRate
		self.GrudgeBulletMaxNum = GrudgeBulletMaxNum
		self.GrudgeBulletMinInterval = GrudgeBulletMinInterval
		self.GrudgeBulletActorName = GrudgeBulletActorName
		self.GrudgeSmokeTime = GrudgeSmokeTime
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.CommonTableName = CommonTableName
		self.TsunoTableName = TsunoTableName
		self.TsumeTableName = TsumeTableName
		self.KibaTableName = KibaTableName
		self.IsEmitChemical = IsEmitChemical
		self.ChemicalBulletActor = ChemicalBulletActor
		self.ChemicalBulletArea = ChemicalBulletArea
		self.ChemicalBulletRate = ChemicalBulletRate
		self.ChemicalBulletNum = ChemicalBulletNum
		self.ChemicalWindArea = ChemicalWindArea
		self.ChemicalWindPower = ChemicalWindPower
		self.ChemicalWindLimitHeight = ChemicalWindLimitHeight
		self.UpdraftPower = UpdraftPower
		self.UpdraftTime = UpdraftTime
		self.UpdraftInterval = UpdraftInterval
		self.UpdraftBoost = UpdraftBoost
		self.ReturnTime = ReturnTime
		self.BodyHitDamage = BodyHitDamage
		self.BodyHitPower = BodyHitPower
		self.BodyHitImpact = BodyHitImpact
		self.BodyHitShieldDamage = BodyHitShieldDamage
		self.InitBackRailDistance = InitBackRailDistance
		self.DefaultMaterialAnmName = DefaultMaterialAnmName
		self.HornAnmName = HornAnmName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class DragonIceWaitRunel:
	ChildNames = ["怨念待機", "正常待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DragonItemRoot:
	ChildNames = ["体に貼り付く", "打ち上がる", "通常"]

	def __init__(self, Name, Gravity, TailXLinkEventName, AuraXLinkEventName, FlyPrepareXinkEventName, FlyStartXinkEventName, HitGroundXLinkEventName, LightShaftXLinkEventName, ActivateXlinkEventName, FlyStartTime, DestroySwitchGameData, FlyStartHeightAtRunel, ClearFlagTimeAtRunel, ClearFlagLabel, DropItemFlagLabel, AtHitImpulseRate, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Gravity = Gravity
		self.TailXLinkEventName = TailXLinkEventName
		self.AuraXLinkEventName = AuraXLinkEventName
		self.FlyPrepareXinkEventName = FlyPrepareXinkEventName
		self.FlyStartXinkEventName = FlyStartXinkEventName
		self.HitGroundXLinkEventName = HitGroundXLinkEventName
		self.LightShaftXLinkEventName = LightShaftXLinkEventName
		self.ActivateXlinkEventName = ActivateXlinkEventName
		self.FlyStartTime = FlyStartTime
		self.DestroySwitchGameData = DestroySwitchGameData
		self.FlyStartHeightAtRunel = FlyStartHeightAtRunel
		self.ClearFlagTimeAtRunel = ClearFlagTimeAtRunel
		self.ClearFlagLabel = ClearFlagLabel
		self.DropItemFlagLabel = DropItemFlagLabel
		self.AtHitImpulseRate = AtHitImpulseRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DragonReturn:
	ChildNames = ["移動", "高高度飛行"]

	def __init__(self, Name, Speed, RotateRate, ChangeMoveHeight, FinishHeight, Angle, AvoidStartDistance, ReturnStartFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotateRate = RotateRate
		self.ChangeMoveHeight = ChangeMoveHeight
		self.FinishHeight = FinishHeight
		self.Angle = Angle
		self.AvoidStartDistance = AvoidStartDistance
		self.ReturnStartFrame = ReturnStartFrame
		self.Child0 = Child0
		self.Child1 = Child1


class DragonTurn:
	ChildNames = ["移動"]

	def __init__(self, Name, Speed, AvoidStartDistance, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.AvoidStartDistance = AvoidStartDistance
		self.Child0 = Child0


class DrawnSwordBowSelect:
	ChildNames = ["抜刀", "抜弓", "素手"]

	def __init__(self, Name, CloseWeaponIdx, BowWeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseWeaponIdx = CloseWeaponIdx
		self.BowWeaponIdx = BowWeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DrawnWeaponSelector:
	ChildNames = ["剣盾装備", "剣装備", "大剣装備", "弓装備", "槍装備", "素手"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class DuckRoot:
	ChildNames = ["スクリプト用", "リアクション", "上機嫌", "所持", "水中行動", "滝接触", "落下", "通常行動", "騎乗中"]

	def __init__(self, Name, InWaterDepth, IsCheckFreeFall, IsCheckStuckConsiderY, IsUseWeakForcePushOutside, IsEnableEscapeForceEndCheck, EscapeForceEndTime, AfterEscapeForceEndState, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.IsCheckFreeFall = IsCheckFreeFall
		self.IsCheckStuckConsiderY = IsCheckStuckConsiderY
		self.IsUseWeakForcePushOutside = IsUseWeakForcePushOutside
		self.IsEnableEscapeForceEndCheck = IsEnableEscapeForceEndCheck
		self.EscapeForceEndTime = EscapeForceEndTime
		self.AfterEscapeForceEndState = AfterEscapeForceEndState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class DungeonCannonBallAutoDelete:
	ChildNames = ["消滅", "通常"]

	def __init__(self, Name, TriggerVelocity, TriggerVelocityKeepTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TriggerVelocity = TriggerVelocity
		self.TriggerVelocityKeepTime = TriggerVelocityKeepTime
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonEntranceRoot:
	ChildNames = ["オープン", "クリア", "クローズ"]

	def __init__(self, Name, IsCheckClear, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckClear = IsCheckClear
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DungeonMoveTag:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonMoveTagCont:
	ChildNames = ["待機", "戻る", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class DungeonRemainsFire:
	ChildNames = ["停止", "移動"]

	def __init__(self, Name, RailName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RailName = RailName
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonResetPosTag:
	ChildNames = ["待機", "復帰位置指定"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag3D:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TargetRad, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetRad = TargetRad
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag4ElecApp:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag4FireApp:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag4WaterApp:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Lv0, Lv1, Lv2, Lv3, Lv4, Lv5, Lv6, Lv7, Lv8, Lv9, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Lv0 = Lv0
		self.Lv1 = Lv1
		self.Lv2 = Lv2
		self.Lv3 = Lv3
		self.Lv4 = Lv4
		self.Lv5 = Lv5
		self.Lv6 = Lv6
		self.Lv7 = Lv7
		self.Lv8 = Lv8
		self.Lv9 = Lv9
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTag4WindApp:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTagCont:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, RotateTurnOn, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateTurnOn = RotateTurnOn
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTagInOrder:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, RotateTurnOn, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateTurnOn = RotateTurnOn
		self.Child0 = Child0
		self.Child1 = Child1


class DungeonRotateTagShuttle:
	ChildNames = ["反時計回り回転", "反時計回り回転後待機", "時計回り回転", "時計回り回転後待機"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class DungeonRotateTagWaterChemical:
	ChildNames = ["反時計回り", "待機", "時計回り", "減速"]

	def __init__(self, Name, SlowDownRotRadAccel, SlowDownTimer, RotRadAccel, ReverseDotTh, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlowDownRotRadAccel = SlowDownRotRadAccel
		self.SlowDownTimer = SlowDownTimer
		self.RotRadAccel = RotRadAccel
		self.ReverseDotTh = ReverseDotTh
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class DynTargetStoneShootEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ShootItemName, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootItemName = ShootItemName
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class DynTgBreathAttackEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1


class EarthReleaseAttack:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, EarthReleaseActorName, EarthReleasePartsName, AttackPower, EnlargeTime, Range, Scale, UseAfterAction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EarthReleaseActorName = EarthReleaseActorName
		self.EarthReleasePartsName = EarthReleasePartsName
		self.AttackPower = AttackPower
		self.EnlargeTime = EnlargeTime
		self.Range = Range
		self.Scale = Scale
		self.UseAfterAction = UseAfterAction
		self.Child0 = Child0
		self.Child1 = Child1


class ElectricBall:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, TargetVol, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetVol = TargetVol
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ElectricCable:
	ChildNames = ["Energized", "Wait"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyAngry:
	ChildNames = ["回転", "怒り"]

	def __init__(self, Name, TurnAng, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnAng = TurnAng
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyAttackAndAway:
	ChildNames = ["戦闘攻撃", "戦闘離脱"]

	def __init__(self, Name, WeaponIdx, AwayStartDist, CheckCliffDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.AwayStartDist = AwayStartDist
		self.CheckCliffDist = CheckCliffDist
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyBaseArrowAttack:
	ChildNames = ["リロード", "攻撃", "準備"]

	def __init__(self, Name, WeaponIdx, IntervalIntensity, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IntervalIntensity = IntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyBaseFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class EnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyBattleWithAreaCheck:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, AttackVMin, AttackVMax, AttackFar, WeaponIdx, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.AttackFar = AttackFar
		self.WeaponIdx = WeaponIdx
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyCalledAppear:
	ChildNames = ["出現"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class EnemyChaseShield:
	ChildNames = ["ナビ追跡", "取得", "回転", "追跡"]

	def __init__(self, Name, TurnAng, EquipItemSearchIdx, ShieldReachDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnAng = TurnAng
		self.EquipItemSearchIdx = EquipItemSearchIdx
		self.ShieldReachDist = ShieldReachDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyChaseTargetAndAction:
	ChildNames = ["アクション", "ジャンプ", "回転", "直進", "移動", "見まわす"]

	def __init__(self, Name, RepathTime, LostDist, LostSpeed, LostAng, WeaponIdx, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RepathTime = RepathTime
		self.LostDist = LostDist
		self.LostSpeed = LostSpeed
		self.LostAng = LostAng
		self.WeaponIdx = WeaponIdx
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class EnemyChemTargetAction:
	ChildNames = ["アクション", "回転", "移動"]

	def __init__(self, Name, ActionDist, ActionDir, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActionDist = ActionDist
		self.ActionDir = ActionDir
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyChemicalPowerSelect:
	ChildNames = ["ケミカル有効", "ケミカル無効"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyChemicalSelect:
	ChildNames = ["アイス", "エレキ", "ノーマル", "ファイア"]

	def __init__(self, Name, IsCheckActive, ChmObjName, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckActive = IsCheckActive
		self.ChmObjName = ChmObjName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyConfuse:
	ChildNames = ["行動"]

	def __init__(self, Name, ConfuseTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ConfuseTime = ConfuseTime
		self.Child0 = Child0


class EnemyCutRope:
	ChildNames = ["カット", "回転", "接近"]

	def __init__(self, Name, CutFlyAttack, WeaponIdx, CutDist, CutAngle, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CutFlyAttack = CutFlyAttack
		self.WeaponIdx = WeaponIdx
		self.CutDist = CutDist
		self.CutAngle = CutAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyDefaultReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class EnemyDemoSumonRecgTgt:
	ChildNames = ["仕掛け作動", "戦況不利", "戦況不利認識", "気づき", "発見", "連絡"]

	def __init__(self, Name, DemoName, EntryPoint, OnlyOne, IsBroadCastOnlyOne, LostTimer, WeaponIdx, SpreadDist, CryInterval, RandomCryInterval, RandomCryIntervalMax, NoCryDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DemoName = DemoName
		self.EntryPoint = EntryPoint
		self.OnlyOne = OnlyOne
		self.IsBroadCastOnlyOne = IsBroadCastOnlyOne
		self.LostTimer = LostTimer
		self.WeaponIdx = WeaponIdx
		self.SpreadDist = SpreadDist
		self.CryInterval = CryInterval
		self.RandomCryInterval = RandomCryInterval
		self.RandomCryIntervalMax = RandomCryIntervalMax
		self.NoCryDist = NoCryDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class EnemyEscape:
	ChildNames = ["こける", "逃走移動"]

	def __init__(self, Name, TumbleTime, TumbleRand, EscapeTime, EscapeRand, EscapeDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TumbleTime = TumbleTime
		self.TumbleRand = TumbleRand
		self.EscapeTime = EscapeTime
		self.EscapeRand = EscapeRand
		self.EscapeDist = EscapeDist
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyEscapeMove:
	ChildNames = ["ジャンプ", "探索逃走", "直進逃走", "見まわす"]

	def __init__(self, Name, BehindCheckDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BehindCheckDist = BehindCheckDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyEscapeRoot:
	ChildNames = ["逃走", "逃走終了振り向き", "逃走開始振り向き"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyFeintBattle:
	ChildNames = ["フェイント", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, IsAttackEnd, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAttackEnd = IsAttackEnd
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyFindBadStatusFriend:
	ChildNames = ["ビタロック"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class EnemyFindHorseRideTarget:
	ChildNames = ["不意討ち", "戦闘", "追跡", "追跡諦め"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, WeaponIdx, LostVMin, LostVMax, LostTimer, LostRange, AttackTargetSpeed, ChaseTime, ReChaseDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.AttackTargetSpeed = AttackTargetSpeed
		self.ChaseTime = ChaseTime
		self.ReChaseDist = ReChaseDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyFindShootable:
	ChildNames = ["アクション", "接近"]

	def __init__(self, Name, AttOffset, CanGrabHeavy, GrabCheckRadius, ChaseItemDist, ChaseItemSpeed, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttOffset = AttOffset
		self.CanGrabHeavy = CanGrabHeavy
		self.GrabCheckRadius = GrabCheckRadius
		self.ChaseItemDist = ChaseItemDist
		self.ChaseItemSpeed = ChaseItemSpeed
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyFortressChat:
	ChildNames = ["会話", "向き直り", "呼びかけ"]

	def __init__(self, Name, NextPer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NextPer = NextPer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyFortressMgrTag:
	ChildNames = ["会話", "待機"]

	def __init__(self, Name, CheckInterval, ChangePer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckInterval = CheckInterval
		self.ChangePer = ChangePer
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyFortressWait:
	ChildNames = ["しょんぼり", "ダンス", "反応待ち", "向き直り", "呼びかけ", "囃し立てる", "団欒", "注意", "注視", "聞く", "話す", "食事"]

	def __init__(self, Name, ReactDelayMin, ReactDelayMax, EatPer, EatItem, DanceReactRand, TalkEndDelayMin, TalkEndDelayMax, FortressTag, TalkChangeViewTargetTimerMin, TalkChangeViewTargetTimerMax, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactDelayMin = ReactDelayMin
		self.ReactDelayMax = ReactDelayMax
		self.EatPer = EatPer
		self.EatItem = EatItem
		self.DanceReactRand = DanceReactRand
		self.TalkEndDelayMin = TalkEndDelayMin
		self.TalkEndDelayMax = TalkEndDelayMax
		self.FortressTag = FortressTag
		self.TalkChangeViewTargetTimerMin = TalkChangeViewTargetTimerMin
		self.TalkChangeViewTargetTimerMax = TalkChangeViewTargetTimerMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class EnemyFortressWatchKeepingWait:
	ChildNames = ["サボり", "ダンス", "反応待ち", "向き直り", "呼びかけ", "回転", "待機", "注意", "聞く", "話す"]

	def __init__(self, Name, ReactDelayMin, ReactDelayMax, DanceReactRand, TalkEndDelayMin, TalkEndDelayMax, FortressTag, TalkChangeViewTargetTimerMin, TalkChangeViewTargetTimerMax, IdleCheckMin, IdleCheckMax, IdlePer, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactDelayMin = ReactDelayMin
		self.ReactDelayMax = ReactDelayMax
		self.DanceReactRand = DanceReactRand
		self.TalkEndDelayMin = TalkEndDelayMin
		self.TalkEndDelayMax = TalkEndDelayMax
		self.FortressTag = FortressTag
		self.TalkChangeViewTargetTimerMin = TalkChangeViewTargetTimerMin
		self.TalkChangeViewTargetTimerMax = TalkChangeViewTargetTimerMax
		self.IdleCheckMin = IdleCheckMin
		self.IdleCheckMax = IdleCheckMax
		self.IdlePer = IdlePer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class EnemyHide:
	ChildNames = ["回転", "待機", "見まわす", "隠れる"]

	def __init__(self, Name, TurnStartAng, RepathTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAng = TurnStartAng
		self.RepathTime = RepathTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyHideGrass:
	ChildNames = ["待機"]

	def __init__(self, Name, SightRatio, HearingRatio, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SightRatio = SightRatio
		self.HearingRatio = HearingRatio
		self.Child0 = Child0


class EnemyHideShootingBattle:
	ChildNames = ["戦闘", "隠れる"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyHorseRide:
	ChildNames = ["乗る", "復帰"]

	def __init__(self, Name, UpperBodyASSlot, LowerBodyASSlot, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyLifeSelect:
	ChildNames = ["ハンター", "一般", "見張り"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyLiftShootItem:
	ChildNames = ["回転", "投げつけ", "持ち上げ", "移動"]

	def __init__(self, Name, ShootAngle, ShootDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootAngle = ShootAngle
		self.ShootDist = ShootDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyLifted:
	ChildNames = ["所持", "投擲", "着地"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyLost:
	ChildNames = ["強制帰還", "行動"]

	def __init__(self, Name, RailCheckInterval, SealForceReturn, ForceReturnNoCameraRad, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RailCheckInterval = RailCheckInterval
		self.SealForceReturn = SealForceReturn
		self.ForceReturnNoCameraRad = ForceReturnNoCameraRad
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyMimicrySelect:
	ChildNames = ["擬態", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyMoveBattle:
	ChildNames = ["回転", "戦闘攻撃", "戦闘準備", "移動"]

	def __init__(self, Name, LimitMoveTime, MoveDist, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitMoveTime = LimitMoveTime
		self.MoveDist = MoveDist
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyMoveToGround:
	ChildNames = ["未発見", "発見"]

	def __init__(self, Name, AreaThreshold, SearchRadius, RetryTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AreaThreshold = AreaThreshold
		self.SearchRadius = SearchRadius
		self.RetryTime = RetryTime
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoiseTarget:
	ChildNames = ["到達不能", "後退", "接近", "気づき", "盾拾い", "騒ぐ"]

	def __init__(self, Name, LostTime, NearDist, WeaponIdx, FarDist, RerouteTimeMin, RerouteTimeMax, ShieldIdx, SearchShieldDist, NoShieldSearchDist, UnReachableToRepathDist, NoShieldEquipWpIdx, TooFarPathDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostTime = LostTime
		self.NearDist = NearDist
		self.WeaponIdx = WeaponIdx
		self.FarDist = FarDist
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.ShieldIdx = ShieldIdx
		self.SearchShieldDist = SearchShieldDist
		self.NoShieldSearchDist = NoShieldSearchDist
		self.UnReachableToRepathDist = UnReachableToRepathDist
		self.NoShieldEquipWpIdx = NoShieldEquipWpIdx
		self.TooFarPathDist = TooFarPathDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class EnemyNotice:
	ChildNames = ["ターン", "追跡"]

	def __init__(self, Name, TurnStartAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeActiveEnemy:
	ChildNames = ["気づき", "行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeFearfulLastAttacker:
	ChildNames = ["気づき", "眺める", "逃走"]

	def __init__(self, Name, NoWarnDist, WaitTime, NoWarnHeightMin, NoWarnHeightMax, NoTerrorDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoWarnDist = NoWarnDist
		self.WaitTime = WaitTime
		self.NoWarnHeightMin = NoWarnHeightMin
		self.NoWarnHeightMax = NoWarnHeightMax
		self.NoTerrorDist = NoTerrorDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyNoticeFearfulTarget:
	ChildNames = ["気づき", "眺める", "逃走"]

	def __init__(self, Name, NoWarnDist, WaitTime, NoWarnHeightMin, NoWarnHeightMax, NoTerrorDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoWarnDist = NoWarnDist
		self.WaitTime = WaitTime
		self.NoWarnHeightMin = NoWarnHeightMin
		self.NoWarnHeightMax = NoWarnHeightMax
		self.NoTerrorDist = NoTerrorDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyNoticeLimit:
	ChildNames = ["定員オーバー", "定員内"]

	def __init__(self, Name, OverNum, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OverNum = OverNum
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeSound:
	ChildNames = ["気づき", "行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeSoundSensitiveTimer:
	ChildNames = ["気づき", "行動"]

	def __init__(self, Name, Timer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Timer = Timer
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeSoundWithUI:
	ChildNames = ["気づき", "行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyNoticeTerror:
	ChildNames = ["気づき", "眺める", "逃走"]

	def __init__(self, Name, NoWarnDist, WaitTime, NoWarnHeightMin, NoWarnHeightMax, NoTerrorDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoWarnDist = NoWarnDist
		self.WaitTime = WaitTime
		self.NoWarnHeightMin = NoWarnHeightMin
		self.NoWarnHeightMax = NoWarnHeightMax
		self.NoTerrorDist = NoTerrorDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyPermitAttackSelect:
	ChildNames = ["攻撃禁止", "攻撃許可"]

	def __init__(self, Name, IsIgnoreEnemyMgr, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsIgnoreEnemyMgr = IsIgnoreEnemyMgr
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyPursuingArrowBattle:
	ChildNames = ["弓構え", "待機", "追撃ち", "離脱"]

	def __init__(self, Name, PursuingAttackInterval, PursuingAttackIntervalRand, PursuingAttackStartAng, PursuingAttackStartDist, HoldInterval, HoldIntervalLast, HoldIntervalRand, LeaveStartDist, LeaveEndDist, LeaveTime, LeaveWaitTime, BaseDist, OutDist, OutDistVMin, OutDistVMax, WeaponIdx, BlindlyAttackMinNum, BlindlyAttackMaxNum, ShootDistRatio, IsEndAfterAttack, IsUpdateNoticeState, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PursuingAttackInterval = PursuingAttackInterval
		self.PursuingAttackIntervalRand = PursuingAttackIntervalRand
		self.PursuingAttackStartAng = PursuingAttackStartAng
		self.PursuingAttackStartDist = PursuingAttackStartDist
		self.HoldInterval = HoldInterval
		self.HoldIntervalLast = HoldIntervalLast
		self.HoldIntervalRand = HoldIntervalRand
		self.LeaveStartDist = LeaveStartDist
		self.LeaveEndDist = LeaveEndDist
		self.LeaveTime = LeaveTime
		self.LeaveWaitTime = LeaveWaitTime
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.OutDistVMin = OutDistVMin
		self.OutDistVMax = OutDistVMax
		self.WeaponIdx = WeaponIdx
		self.BlindlyAttackMinNum = BlindlyAttackMinNum
		self.BlindlyAttackMaxNum = BlindlyAttackMaxNum
		self.ShootDistRatio = ShootDistRatio
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyPursuingAttackCheck:
	ChildNames = ["追撃ち攻撃", "通常戦闘"]

	def __init__(self, Name, PursuingAttackInterval, PursuingAttackIntervalRand, PursuingAttackStartAng, AttackAng, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PursuingAttackInterval = PursuingAttackInterval
		self.PursuingAttackIntervalRand = PursuingAttackIntervalRand
		self.PursuingAttackStartAng = PursuingAttackStartAng
		self.AttackAng = AttackAng
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyPursuingBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "追撃ち攻撃"]

	def __init__(self, Name, PursuingAttackInterval, PursuingAttackIntervalRand, PursuingAttackStartAng, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PursuingAttackInterval = PursuingAttackInterval
		self.PursuingAttackIntervalRand = PursuingAttackIntervalRand
		self.PursuingAttackStartAng = PursuingAttackStartAng
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyRandomRepeatSideStep:
	ChildNames = ["サイドステップ", "待機"]

	def __init__(self, Name, MinRepeatNum, MaxRepeatNum, StepDist, StepAngle, WeaponIdx, BaseDist, OutDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinRepeatNum = MinRepeatNum
		self.MaxRepeatNum = MaxRepeatNum
		self.StepDist = StepDist
		self.StepAngle = StepAngle
		self.WeaponIdx = WeaponIdx
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyRangeKeepMove:
	ChildNames = ["強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動"]

	def __init__(self, Name, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class EnemyRangeKeepSwimMove:
	ChildNames = ["戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動"]

	def __init__(self, Name, CloseDist, FarDist, WeaponIdx, OutDist, Time, BaseDist, SpaceDist, IsCheckCliff, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.Time = Time
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.IsCheckCliff = IsCheckCliff
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyRecognizeTarget:
	ChildNames = ["仕掛け作動", "戦況不利", "戦況不利認識", "気づき", "発見", "連絡"]

	def __init__(self, Name, SummonNum, SummonGrassHeight, SummonCheckDist, LostTimer, WeaponIdx, SpreadDist, CryInterval, RandomCryInterval, RandomCryIntervalMax, NoCryDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SummonNum = SummonNum
		self.SummonGrassHeight = SummonGrassHeight
		self.SummonCheckDist = SummonCheckDist
		self.LostTimer = LostTimer
		self.WeaponIdx = WeaponIdx
		self.SpreadDist = SpreadDist
		self.CryInterval = CryInterval
		self.RandomCryInterval = RandomCryInterval
		self.RandomCryIntervalMax = RandomCryIntervalMax
		self.NoCryDist = NoCryDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class EnemyRestraintCheckBattle:
	ChildNames = ["戦闘", "牽制"]

	def __init__(self, Name, CheckDist, CheckVmin, CheckVmax, CheckAngle, CheckInterval, CheckRandTime, IsResetInterval, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.CheckVmin = CheckVmin
		self.CheckVmax = CheckVmax
		self.CheckAngle = CheckAngle
		self.CheckInterval = CheckInterval
		self.CheckRandTime = CheckRandTime
		self.IsResetInterval = IsResetInterval
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyReturnSelect:
	ChildNames = ["帰還", "未帰還"]

	def __init__(self, Name, NotReturnDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotReturnDist = NotReturnDist
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyRoam:
	ChildNames = ["徘徊待機", "徘徊探索", "徘徊歩行"]

	def __init__(self, Name, TerritoryRadius, TerritoryRadiusRnd, SearchPer, MinMoveDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryRadius = TerritoryRadius
		self.TerritoryRadiusRnd = TerritoryRadiusRnd
		self.SearchPer = SearchPer
		self.MinMoveDist = MinMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyRoamSelect:
	ChildNames = ["レール移動", "単純徘徊", "小物連携", "待ち伏せ", "未帰還"]

	def __init__(self, Name, HideGrassHeight, NotReturnDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HideGrassHeight = HideGrassHeight
		self.NotReturnDist = NotReturnDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class EnemyRoamViewItem:
	ChildNames = ["変化感知", "行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class EnemySearchHorse:
	ChildNames = ["怒り", "直進", "馬到達", "馬未発見"]

	def __init__(self, Name, SearchDist, RepathTime, RideRadius, NoWeaponRiding, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchDist = SearchDist
		self.RepathTime = RepathTime
		self.RideRadius = RideRadius
		self.NoWeaponRiding = NoWeaponRiding
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemySearchShieldItemFindPlayer:
	ChildNames = ["アイテム発見", "ケミカル仲間招来", "ナビメッシュ無し", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "武器ケミカル付与", "武器投げ", "気づき", "盾拾い", "速攻"]

	def __init__(self, Name, SearchShieldDist, NoShieldSearchDist, ShieldIdx, SearchObjectDist, ItemChaseableSpd, ItemChasealeRot, CanGrabHeavy, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, ChemicalSearchDist, NoSearchDist, Voltage, ChemicalActionDist, ThrowWeaponPer, ThrowWeaponDist, NoChemSearchWpIdx, NoBurnWaterDepth, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchShieldDist = SearchShieldDist
		self.NoShieldSearchDist = NoShieldSearchDist
		self.ShieldIdx = ShieldIdx
		self.SearchObjectDist = SearchObjectDist
		self.ItemChaseableSpd = ItemChaseableSpd
		self.ItemChasealeRot = ItemChasealeRot
		self.CanGrabHeavy = CanGrabHeavy
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.ChemicalSearchDist = ChemicalSearchDist
		self.NoSearchDist = NoSearchDist
		self.Voltage = Voltage
		self.ChemicalActionDist = ChemicalActionDist
		self.ThrowWeaponPer = ThrowWeaponPer
		self.ThrowWeaponDist = ThrowWeaponDist
		self.NoChemSearchWpIdx = NoChemSearchWpIdx
		self.NoBurnWaterDepth = NoBurnWaterDepth
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class EnemyShieldSearchOrBattle:
	ChildNames = ["盾拾い", "通常"]

	def __init__(self, Name, SearchShieldDist, NoShieldSearchDist, ShieldIdx, NoShieldTargetNearDist, ShieldReachDist, NoShieldEquipWpIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchShieldDist = SearchShieldDist
		self.NoShieldSearchDist = NoShieldSearchDist
		self.ShieldIdx = ShieldIdx
		self.NoShieldTargetNearDist = NoShieldTargetNearDist
		self.ShieldReachDist = ShieldReachDist
		self.NoShieldEquipWpIdx = NoShieldEquipWpIdx
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyShootAttackExplosives:
	ChildNames = ["リロード", "回転", "後ずさり", "攻撃", "準備", "逃走"]

	def __init__(self, Name, ExplosivesAvoidDist, TurnStartAng, WeaponIdx, IntervalIntensity, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.TurnStartAng = TurnStartAng
		self.WeaponIdx = WeaponIdx
		self.IntervalIntensity = IntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class EnemySittingTogether:
	ChildNames = ["座る", "騒ぐ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemySkyArrowAttack:
	ChildNames = ["リロード", "攻撃", "準備"]

	def __init__(self, Name, WeaponIdx, IntervalIntensity, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IntervalIntensity = IntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemySomeIgniteBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, IgniteNum, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteNum = IgniteNum
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1


class EnemySyncAttack:
	ChildNames = ["待機", "行動"]

	def __init__(self, Name, NormalASSlot, AttackASSlot, JustAvoidCheckLength, JustAvoidCheckAngle, RootNodeName, AttackNodeName, AttackNodeNameWait, AttackASName, AtNodeName, AttackDistMin, AttackDistMax, AttackInterval, AttackIntervalRand, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NormalASSlot = NormalASSlot
		self.AttackASSlot = AttackASSlot
		self.JustAvoidCheckLength = JustAvoidCheckLength
		self.JustAvoidCheckAngle = JustAvoidCheckAngle
		self.RootNodeName = RootNodeName
		self.AttackNodeName = AttackNodeName
		self.AttackNodeNameWait = AttackNodeNameWait
		self.AttackASName = AttackASName
		self.AtNodeName = AtNodeName
		self.AttackDistMin = AttackDistMin
		self.AttackDistMax = AttackDistMax
		self.AttackInterval = AttackInterval
		self.AttackIntervalRand = AttackIntervalRand
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyTargetGearSelect:
	ChildNames = ["対象低速ギア", "対象高速ギア"]

	def __init__(self, Name, GearThreashold, IsSelectEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GearThreashold = GearThreashold
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyTargetInAreaSelect:
	ChildNames = ["エリア内", "エリア外"]

	def __init__(self, Name, LengthXZ, LengthMaxY, LengthMinY, CentOffset, Option, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LengthXZ = LengthXZ
		self.LengthMaxY = LengthMaxY
		self.LengthMinY = LengthMinY
		self.CentOffset = CentOffset
		self.Option = Option
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyTargetInSightSelect:
	ChildNames = ["見えてない", "見えてる"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyTimelineAI:
	ChildNames = ["Idle", "Sleep", "Wander"]

	def __init__(self, Name, IntervalToCheckSchedule, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IntervalToCheckSchedule = IntervalToCheckSchedule
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyTired:
	ChildNames = ["帰還", "見まわす"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyTreeWeaponSearchOrBattle:
	ChildNames = ["戦闘", "木武器発見", "木発見"]

	def __init__(self, Name, SearchDist, NoSearchDist, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchDist = SearchDist
		self.NoSearchDist = NoSearchDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyVacuumBombSelect:
	ChildNames = ["所持", "非所持"]

	def __init__(self, Name, PartsKey0, PartsKey1, PartsKey2, PartsKey3, PartsKey4, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey0 = PartsKey0
		self.PartsKey1 = PartsKey1
		self.PartsKey2 = PartsKey2
		self.PartsKey3 = PartsKey3
		self.PartsKey4 = PartsKey4
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyVacuumChangeItemSelect:
	ChildNames = ["所持", "非所持"]

	def __init__(self, Name, PartsKey0, PartsKey1, PartsKey2, PartsKey3, PartsKey4, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey0 = PartsKey0
		self.PartsKey1 = PartsKey1
		self.PartsKey2 = PartsKey2
		self.PartsKey3 = PartsKey3
		self.PartsKey4 = PartsKey4
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyVacuumWeaponTypeSelect:
	ChildNames = ["その他", "ブーメラン", "大剣", "小剣", "弓", "槍", "盾"]

	def __init__(self, Name, PartsKey, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey = PartsKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class EnemyWaitViewItem:
	ChildNames = ["しょんぼり", "囃し立てる", "団欒", "注視"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class EnemyWarnNoticeEndChase:
	ChildNames = ["発見", "警戒", "追跡"]

	def __init__(self, Name, WarnNoticeTime, WarnNoticeTimeRnd, IsSight, IsWorry, WarnBlinkTime, LostCounter, MaxCountUp, Penalty, PenaltyStair2Num, NoPenaltyNum, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarnNoticeTime = WarnNoticeTime
		self.WarnNoticeTimeRnd = WarnNoticeTimeRnd
		self.IsSight = IsSight
		self.IsWorry = IsWorry
		self.WarnBlinkTime = WarnBlinkTime
		self.LostCounter = LostCounter
		self.MaxCountUp = MaxCountUp
		self.Penalty = Penalty
		self.PenaltyStair2Num = PenaltyStair2Num
		self.NoPenaltyNum = NoPenaltyNum
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnemyWarnNoticeSelect:
	ChildNames = ["発見", "警戒"]

	def __init__(self, Name, WarnNoticeTime, WarnNoticeTimeRnd, IsSight, IsWorry, WarnBlinkTime, LostCounter, MaxCountUp, Penalty, PenaltyStair2Num, NoPenaltyNum, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarnNoticeTime = WarnNoticeTime
		self.WarnNoticeTimeRnd = WarnNoticeTimeRnd
		self.IsSight = IsSight
		self.IsWorry = IsWorry
		self.WarnBlinkTime = WarnBlinkTime
		self.LostCounter = LostCounter
		self.MaxCountUp = MaxCountUp
		self.Penalty = Penalty
		self.PenaltyStair2Num = PenaltyStair2Num
		self.NoPenaltyNum = NoPenaltyNum
		self.Child0 = Child0
		self.Child1 = Child1


class EnemyWatchKeepingWait:
	ChildNames = ["サボり", "回転", "待機"]

	def __init__(self, Name, IdleCheckMin, IdleCheckMax, IdlePer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IdleCheckMin = IdleCheckMin
		self.IdleCheckMax = IdleCheckMax
		self.IdlePer = IdlePer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class EnterFromResetSelect:
	ChildNames = ["初期状態", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EnvSeEmitPointRootAI:
	ChildNames = ["再生", "待機"]

	def __init__(self, Name, InvalidatePlayDistance, PlayDistance, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InvalidatePlayDistance = InvalidatePlayDistance
		self.PlayDistance = PlayDistance
		self.Child0 = Child0
		self.Child1 = Child1


class EquipConditionSelect:
	ChildNames = ["炎上", "通常"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class EquipHaveSelector:
	ChildNames = ["所持", "非所持"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class EquipShieldEnemySearchWeapon:
	ChildNames = ["ジャンプ", "回転", "武器拾い", "武器拾い待ち", "直進", "盾捨て", "移動", "見まわす"]

	def __init__(self, Name, EquipItemSearchIdx, RepathTime, SearchDist, SearchAng, IsUseSight, LineReachableWeaponDist, WeaponIdx, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EquipItemSearchIdx = EquipItemSearchIdx
		self.RepathTime = RepathTime
		self.SearchDist = SearchDist
		self.SearchAng = SearchAng
		self.IsUseSight = IsUseSight
		self.LineReachableWeaponDist = LineReachableWeaponDist
		self.WeaponIdx = WeaponIdx
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class EquipStand:
	ChildNames = ["待機", "飾りゲット", "飾り待機", "飾り生成", "飾る"]

	def __init__(self, Name, DisplayAttKey, TakeOutAttKey, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisplayAttKey = DisplayAttKey
		self.TakeOutAttKey = TakeOutAttKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class EscapeFromTargetFrontRandomDir:
	ChildNames = ["回転移動"]

	def __init__(self, Name, InverseDirRatio, UseCameraFrontByTargetPlayer, MaxTime, MinTime, FrontAngle, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InverseDirRatio = InverseDirRatio
		self.UseCameraFrontByTargetPlayer = UseCameraFrontByTargetPlayer
		self.MaxTime = MaxTime
		self.MinTime = MinTime
		self.FrontAngle = FrontAngle
		self.Child0 = Child0


class EscapeOppositeToTargetInWater:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, RunAwayDistanceMax, AllowRandAngleVertical, AllowRandAngleHorizontal, DivePercent, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RunAwayDistanceMax = RunAwayDistanceMax
		self.AllowRandAngleVertical = AllowRandAngleVertical
		self.AllowRandAngleHorizontal = AllowRandAngleHorizontal
		self.DivePercent = DivePercent
		self.Child0 = Child0
		self.Child1 = Child1


class EscapeOrWaitSelect:
	ChildNames = ["待機", "逃走"]

	def __init__(self, Name, EscapeRange, EscapeMoveDistMin, EscapeMoveDistMax, CheckBackAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EscapeRange = EscapeRange
		self.EscapeMoveDistMin = EscapeMoveDistMin
		self.EscapeMoveDistMax = EscapeMoveDistMax
		self.CheckBackAngle = CheckBackAngle
		self.Child0 = Child0
		self.Child1 = Child1


class EternalPlayerTarget:
	ChildNames = ["プレイヤー死亡", "プレイヤー生存"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class EventTagRootAI:
	ChildNames = ["Dummy"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class EventTimeRoot:
	ChildNames = ["待機"]

	def __init__(self, Name, TimeLimit, IsCountDown, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TimeLimit = TimeLimit
		self.IsCountDown = IsCountDown
		self.Child0 = Child0


class ExceededImpulseCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ExplodeCheck:
	ChildNames = ["爆発", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class FirstSelect:
	ChildNames = ["二回目以降", "初回"]

	def __init__(self, Name, ResetFromDemo, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ResetFromDemo = ResetFromDemo
		self.Child0 = Child0
		self.Child1 = Child1


class FishGoToAndNibble:
	ChildNames = ["前進", "待機", "移動", "行進", "行進最後"]

	def __init__(self, Name, NumTimeNibbleMin, NumTimeNibbleRand, DistStartNibble, DistBackward, DepthGiveUp, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NumTimeNibbleMin = NumTimeNibbleMin
		self.NumTimeNibbleRand = NumTimeNibbleRand
		self.DistStartNibble = DistStartNibble
		self.DistBackward = DistBackward
		self.DepthGiveUp = DepthGiveUp
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class FishRoot:
	ChildNames = ["ジャンプ", "ロケーターわき出し", "初期配置帰還", "地上待機", "帰還", "待機", "死亡", "潜水", "興味対象発見", "逃走", "通常行動"]

	def __init__(self, Name, InWaterDepth, OnGroundDepth, NextJumpTimeBase, NextJumpTimeRand, AllowReturnThreatDist, FrameUntilOutOfWater, DistRunFromPlayerOnReturn, IgnoreFoodBase, IgnoreFoodRand, IgnoreFoodAfterSuccessBase, IgnoreFoodAfterSuccessRand, IsDeleteWhenDead, IsDeadWhenPut, IsEscapeWhenPut, IsDeadWhenDrop, InvalidTgtTimerVal, InvalidEscapeTimerVal, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.OnGroundDepth = OnGroundDepth
		self.NextJumpTimeBase = NextJumpTimeBase
		self.NextJumpTimeRand = NextJumpTimeRand
		self.AllowReturnThreatDist = AllowReturnThreatDist
		self.FrameUntilOutOfWater = FrameUntilOutOfWater
		self.DistRunFromPlayerOnReturn = DistRunFromPlayerOnReturn
		self.IgnoreFoodBase = IgnoreFoodBase
		self.IgnoreFoodRand = IgnoreFoodRand
		self.IgnoreFoodAfterSuccessBase = IgnoreFoodAfterSuccessBase
		self.IgnoreFoodAfterSuccessRand = IgnoreFoodAfterSuccessRand
		self.IsDeleteWhenDead = IsDeleteWhenDead
		self.IsDeadWhenPut = IsDeadWhenPut
		self.IsEscapeWhenPut = IsEscapeWhenPut
		self.IsDeadWhenDrop = IsDeadWhenDrop
		self.InvalidTgtTimerVal = InvalidTgtTimerVal
		self.InvalidEscapeTimerVal = InvalidEscapeTimerVal
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class FishSafeReturn:
	ChildNames = ["フェードアウト", "フェードイン", "ワープ", "待機", "移動", "逃走"]

	def __init__(self, Name, InWaterDepth, DivePercent, AllowReturnThreatDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.DivePercent = DivePercent
		self.AllowReturnThreatDist = AllowReturnThreatDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class FixableLiftable:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, CancelFixedScale, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CancelFixedScale = CancelFixedScale
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class FldObjDlcHeroMapRelief:
	ChildNames = ["オープン", "クリア", "クローズ"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class FldObjIvyBurnRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FlyInsectRoam:
	ChildNames = ["徘徊飛行", "着地"]

	def __init__(self, Name, TerritoryRadius, TerritoryRadiusRand, MinHeight, MaxHeight, RePathDist, RePathDistRand, RePathYDistRand, IsEnableOnLand, MaxRotRand, MaxRotRandOuter, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryRadius = TerritoryRadius
		self.TerritoryRadiusRand = TerritoryRadiusRand
		self.MinHeight = MinHeight
		self.MaxHeight = MaxHeight
		self.RePathDist = RePathDist
		self.RePathDistRand = RePathDistRand
		self.RePathYDistRand = RePathYDistRand
		self.IsEnableOnLand = IsEnableOnLand
		self.MaxRotRand = MaxRotRand
		self.MaxRotRandOuter = MaxRotRandOuter
		self.Child0 = Child0
		self.Child1 = Child1


class FlyMoveToTarget:
	ChildNames = ["ナビメッシュ移動", "上昇", "下降", "待機", "目標位置移動", "経由点移動", "見回し", "遠距離移動"]

	def __init__(self, Name, FarDist, OutDist, OffsetHeight, MoveFailCount, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.OutDist = OutDist
		self.OffsetHeight = OffsetHeight
		self.MoveFailCount = MoveFailCount
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class FlyingEnemyBackKeepMove:
	ChildNames = ["上昇", "下降", "位置調整", "待機", "移動"]

	def __init__(self, Name, LostDistance, AngleRange, SpaceDistance, NearDist, FarDist, BaseDist, BaseHeight, LowHeight, HighHeight, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostDistance = LostDistance
		self.AngleRange = AngleRange
		self.SpaceDistance = SpaceDistance
		self.NearDist = NearDist
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.BaseHeight = BaseHeight
		self.LowHeight = LowHeight
		self.HighHeight = HighHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class FlyingEnemyDiagonallyKeepMove:
	ChildNames = ["上昇", "下降", "位置調整", "待機", "移動"]

	def __init__(self, Name, DiagAngle, SideDirType, LostDistance, AngleRange, SpaceDistance, NearDist, FarDist, BaseDist, BaseHeight, LowHeight, HighHeight, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DiagAngle = DiagAngle
		self.SideDirType = SideDirType
		self.LostDistance = LostDistance
		self.AngleRange = AngleRange
		self.SpaceDistance = SpaceDistance
		self.NearDist = NearDist
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.BaseHeight = BaseHeight
		self.LowHeight = LowHeight
		self.HighHeight = HighHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class FlyingEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class FlyingEnemyFrontKeepMove:
	ChildNames = ["上昇", "下降", "位置調整", "待機", "移動"]

	def __init__(self, Name, LostDistance, AngleRange, SpaceDistance, NearDist, FarDist, BaseDist, BaseHeight, LowHeight, HighHeight, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostDistance = LostDistance
		self.AngleRange = AngleRange
		self.SpaceDistance = SpaceDistance
		self.NearDist = NearDist
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.BaseHeight = BaseHeight
		self.LowHeight = LowHeight
		self.HighHeight = HighHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class ForSaleOrNot:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ForbidDoubleNoticeSelect:
	ChildNames = ["禁止", "解禁"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ForceAttackArea, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceAttackArea = ForceAttackArea
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantBattleMove:
	ChildNames = ["待機", "近づき"]

	def __init__(self, Name, AttackHeightMin, AttackHeightMax, WeaponIdx, BaseDist, StartCloseDistOffset, OutDistOffset, IsCheckLineReachableForClose, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackHeightMin = AttackHeightMin
		self.AttackHeightMax = AttackHeightMax
		self.WeaponIdx = WeaponIdx
		self.BaseDist = BaseDist
		self.StartCloseDistOffset = StartCloseDistOffset
		self.OutDistOffset = OutDistOffset
		self.IsCheckLineReachableForClose = IsCheckLineReachableForClose
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantChanceWait:
	ChildNames = ["チャンス", "回転", "待機"]

	def __init__(self, Name, ChanceRate, CorrectRate, TurnStartAngle, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChanceRate = ChanceRate
		self.CorrectRate = CorrectRate
		self.TurnStartAngle = TurnStartAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ForestGiantClosestAttackSelect:
	ChildNames = ["ヒップドロップ", "足踏み"]

	def __init__(self, Name, HipDropRate, HipDropRateFar, FarDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HipDropRate = HipDropRate
		self.HipDropRateFar = HipDropRateFar
		self.FarDist = FarDist
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class ForestGiantNormal:
	ChildNames = ["プレイヤー発見", "プレイヤー見失い", "不審者発見", "不調仲間発見", "初期待機", "待機", "怒り", "攻撃反応", "暗闇目覚め", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, SleepingHearAwnRatio, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SleepingHearAwnRatio = SleepingHearAwnRatio
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class ForestGiantNoticeSound:
	ChildNames = ["気づき", "行動"]

	def __init__(self, Name, FrontAngle, UseSimpleOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FrontAngle = FrontAngle
		self.UseSimpleOffset = UseSimpleOffset
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "右腕大ダメージ", "右足ダメージ", "大落下", "小ダメージ", "崩れ落ち", "左足ダメージ", "弱点ダメージ", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, TgLegL, BgLegL, TgLegR, BgLegR, TgArmR, RightLegArmorSlot, LeftLegArmorSlot, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Child19, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TgLegL = TgLegL
		self.BgLegL = BgLegL
		self.TgLegR = TgLegR
		self.BgLegR = BgLegR
		self.TgArmR = TgArmR
		self.RightLegArmorSlot = RightLegArmorSlot
		self.LeftLegArmorSlot = LeftLegArmorSlot
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18
		self.Child19 = Child19


class ForestGiantRecognizeTarget:
	ChildNames = ["気づき", "発見"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ForestGiantRoam:
	ChildNames = ["回転", "帰還", "待機", "暇つぶし", "移動", "索敵"]

	def __init__(self, Name, ReturnHomeDist, FreeIntervalMin, FreeIntervalMax, FreePer, MoveIntervalMin, MoveIntervalMax, Territory, TargetDistMin, TargetDistMax, NoMoveTime, NoSpAttackMoveTime, SpAttackServiceDist, SpAttackServiceTime, SpAttackServiceAngle, TurnCheckDist, TurnCheckHeight, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReturnHomeDist = ReturnHomeDist
		self.FreeIntervalMin = FreeIntervalMin
		self.FreeIntervalMax = FreeIntervalMax
		self.FreePer = FreePer
		self.MoveIntervalMin = MoveIntervalMin
		self.MoveIntervalMax = MoveIntervalMax
		self.Territory = Territory
		self.TargetDistMin = TargetDistMin
		self.TargetDistMax = TargetDistMax
		self.NoMoveTime = NoMoveTime
		self.NoSpAttackMoveTime = NoSpAttackMoveTime
		self.SpAttackServiceDist = SpAttackServiceDist
		self.SpAttackServiceTime = SpAttackServiceTime
		self.SpAttackServiceAngle = SpAttackServiceAngle
		self.TurnCheckDist = TurnCheckDist
		self.TurnCheckHeight = TurnCheckHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class ForestGiantRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, WeakPointNode0, WeakPointNode1, WeakPointNode2, WeakPointNode3, WeakPointNode4, NecklaceTgtName0, NecklaceTgtName1, NecklaceTgtName2, NecklaceWeaponIdx0, NecklaceWeaponIdx1, NecklaceWeaponIdx2, NecklaceClothParticleIdx0, NecklaceClothParticle2Idx0, ObjNecklaceClothParticleIdx0, NecklaceClothParticleIdx1, NecklaceClothParticle2Idx1, ObjNecklaceClothParticleIdx1, NecklaceClothParticleIdx2, NecklaceClothParticle2Idx2, ObjNecklaceClothParticleIdx2, NecklaceClothObjName, DefaultWeaponParticleRadius, IsDamageToEnemy, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeakPointNode0 = WeakPointNode0
		self.WeakPointNode1 = WeakPointNode1
		self.WeakPointNode2 = WeakPointNode2
		self.WeakPointNode3 = WeakPointNode3
		self.WeakPointNode4 = WeakPointNode4
		self.NecklaceTgtName0 = NecklaceTgtName0
		self.NecklaceTgtName1 = NecklaceTgtName1
		self.NecklaceTgtName2 = NecklaceTgtName2
		self.NecklaceWeaponIdx0 = NecklaceWeaponIdx0
		self.NecklaceWeaponIdx1 = NecklaceWeaponIdx1
		self.NecklaceWeaponIdx2 = NecklaceWeaponIdx2
		self.NecklaceClothParticleIdx0 = NecklaceClothParticleIdx0
		self.NecklaceClothParticle2Idx0 = NecklaceClothParticle2Idx0
		self.ObjNecklaceClothParticleIdx0 = ObjNecklaceClothParticleIdx0
		self.NecklaceClothParticleIdx1 = NecklaceClothParticleIdx1
		self.NecklaceClothParticle2Idx1 = NecklaceClothParticle2Idx1
		self.ObjNecklaceClothParticleIdx1 = ObjNecklaceClothParticleIdx1
		self.NecklaceClothParticleIdx2 = NecklaceClothParticleIdx2
		self.NecklaceClothParticle2Idx2 = NecklaceClothParticle2Idx2
		self.ObjNecklaceClothParticleIdx2 = ObjNecklaceClothParticleIdx2
		self.NecklaceClothObjName = NecklaceClothObjName
		self.DefaultWeaponParticleRadius = DefaultWeaponParticleRadius
		self.IsDamageToEnemy = IsDamageToEnemy
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class ForestGiantStoneShootBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "近接攻撃"]

	def __init__(self, Name, ForceAttackArea, ShootItemName2, ShootItemRate1, ShootItemName, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceAttackArea = ForceAttackArea
		self.ShootItemName2 = ShootItemName2
		self.ShootItemRate1 = ShootItemRate1
		self.ShootItemName = ShootItemName
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class Fork2AI:
	ChildNames = ["子０", "子１"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class Fork2AIUpperLowerBody:
	ChildNames = ["上半身", "下半身"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class Fork3AI:
	ChildNames = ["子０", "子１", "子２"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class Fork4AI:
	ChildNames = ["子０", "子１", "子２", "子３"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class Fork5AI:
	ChildNames = ["子０", "子１", "子２", "子３", "子４"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class Fork6AI:
	ChildNames = ["子０", "子１", "子２", "子３", "子４", "子５"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class ForkActionAndJoin:
	ChildNames = ["同期待ち", "行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ForkBeastGanonRoot:
	ChildNames = ["光壁管理", "姫様絶叫", "弱点管理", "接触怨念", "気流管理", "環境変化", "足元変化", "身体動作", "頭上防風"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class FreezeInWaterSelect:
	ChildNames = ["凍結解除", "水上", "水中"]

	def __init__(self, Name, IceBreakTime, InWaterDepth, IsCheckEveryFrame, IsForceChange, OutWaterDepth, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IceBreakTime = IceBreakTime
		self.InWaterDepth = InWaterDepth
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.IsForceChange = IsForceChange
		self.OutWaterDepth = OutWaterDepth
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class FriendCallAction:
	ChildNames = ["アクション", "呼ぶ", "待つ"]

	def __init__(self, Name, NearDistH, NearDistVMax, NearDistVMin, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDistH = NearDistH
		self.NearDistVMax = NearDistVMax
		self.NearDistVMin = NearDistVMin
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class FromPopPoolDamageSelect:
	ChildNames = ["ストップタイマー", "非ストップタイマー"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GambleTreasureBoxRoot:
	ChildNames = ["オープン待機", "クローズ待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GameDataFlagSelector:
	ChildNames = ["False", "True"]

	def __init__(self, Name, CheckOnEnterOnly, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckOnEnterOnly = CheckOnEnterOnly
		self.Child0 = Child0
		self.Child1 = Child1


class GanonApproachOnFloorRoot:
	ChildNames = ["移動"]

	def __init__(self, Name, FinDist, ApproachTime, FinFarDist, MoveFrontRate, MoveFrontLRRate, MoveBackLRRate, CloseDist, ForbitAngMin, ForbitAngMax, CheckPosAng0, CheckPosAng1, CheckPosAng2, CheckPosAng3, CheckPosAng4, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinDist = FinDist
		self.ApproachTime = ApproachTime
		self.FinFarDist = FinFarDist
		self.MoveFrontRate = MoveFrontRate
		self.MoveFrontLRRate = MoveFrontLRRate
		self.MoveBackLRRate = MoveBackLRRate
		self.CloseDist = CloseDist
		self.ForbitAngMin = ForbitAngMin
		self.ForbitAngMax = ForbitAngMax
		self.CheckPosAng0 = CheckPosAng0
		self.CheckPosAng1 = CheckPosAng1
		self.CheckPosAng2 = CheckPosAng2
		self.CheckPosAng3 = CheckPosAng3
		self.CheckPosAng4 = CheckPosAng4
		self.Child0 = Child0


class GanonApproachOnWallRoot:
	ChildNames = ["移動"]

	def __init__(self, Name, ApproachTime, MinDist, MaxDist, FinDist, IsInterpolateYUp, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ApproachTime = ApproachTime
		self.MinDist = MinDist
		self.MaxDist = MaxDist
		self.FinDist = FinDist
		self.IsInterpolateYUp = IsInterpolateYUp
		self.Child0 = Child0


class GanonBattleOnFloorRoot:
	ChildNames = ["待機", "近接攻撃", "遠距離攻撃"]

	def __init__(self, Name, FarAttackDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarAttackDist = FarAttackDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GanonBattleOnWallRoot:
	ChildNames = ["ガーディアン活性化", "待機", "移動", "落下攻撃", "遠距離攻撃"]

	def __init__(self, Name, GuardianActivateHP, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GuardianActivateHP = GuardianActivateHP
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class GanonBattleRoot:
	ChildNames = ["ジャストガード後攻撃", "初回ガーディアン活性化", "初回ガーディアン活性化移動", "初回バリア", "初回バリア移動", "壁", "床", "状態遷移"]

	def __init__(self, Name, BarrierHPRate, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BarrierHPRate = BarrierHPRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class GanonBeamOnFloor:
	ChildNames = ["弾発射", "準備", "終了"]

	def __init__(self, Name, WalkAS, TurnAS, TurnStartAng, KeepMinDist, TurnRate, ArrowNum, ArrowName, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, BattleNodeOffsetLR, BattleNodeOffsetUD, PartsName, IsPrepreNextArrow, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WalkAS = WalkAS
		self.TurnAS = TurnAS
		self.TurnStartAng = TurnStartAng
		self.KeepMinDist = KeepMinDist
		self.TurnRate = TurnRate
		self.ArrowNum = ArrowNum
		self.ArrowName = ArrowName
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD
		self.PartsName = PartsName
		self.IsPrepreNextArrow = IsPrepreNextArrow
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GanonBeamOnWall:
	ChildNames = ["弾発射", "準備", "終了"]

	def __init__(self, Name, ArrowNum, ArrowName, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, BattleNodeOffsetLR, BattleNodeOffsetUD, PartsName, IsPrepreNextArrow, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.ArrowName = ArrowName
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD
		self.PartsName = PartsName
		self.IsPrepreNextArrow = IsPrepreNextArrow
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GanonBeastDying:
	ChildNames = ["レーザー発射", "弱点露出", "待機", "復帰"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GanonBeastMoveSelect:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, Dist, IsMoveFinishEnd, CentralPoint, FrontOffset, WallDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.IsMoveFinishEnd = IsMoveFinishEnd
		self.CentralPoint = CentralPoint
		self.FrontOffset = FrontOffset
		self.WallDist = WallDist
		self.Child0 = Child0
		self.Child1 = Child1


class GanonBeastReaction:
	ChildNames = ["弱点ヒット", "形態変化ダメージ", "死亡"]

	def __init__(self, Name, ASSlot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASSlot = ASSlot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GanonBeastRoot:
	ChildNames = ["リアクション", "初弱点露出デモ", "待機", "怒り", "怒りデモ", "瀕死"]

	def __init__(self, Name, GrudeRainObject, GrudeInterval3, GrudeInterval4, GrudeInterval5, GrudeCreateNum, GrudePlayerDist, GrudeRandRange, GrudeCenterOffset, InitWeakPointASName, WeakPointASSlot, GrudeRainObject2, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrudeRainObject = GrudeRainObject
		self.GrudeInterval3 = GrudeInterval3
		self.GrudeInterval4 = GrudeInterval4
		self.GrudeInterval5 = GrudeInterval5
		self.GrudeCreateNum = GrudeCreateNum
		self.GrudePlayerDist = GrudePlayerDist
		self.GrudeRandRange = GrudeRandRange
		self.GrudeCenterOffset = GrudeCenterOffset
		self.InitWeakPointASName = InitWeakPointASName
		self.WeakPointASSlot = WeakPointASSlot
		self.GrudeRainObject2 = GrudeRainObject2
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class GanonBeastStairState:
	ChildNames = ["段階１", "段階２", "段階３", "段階４"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GanonBeastSufferChanger:
	ChildNames = ["弱点露出", "無敵モード", "通常"]

	def __init__(self, Name, WeakPoint1Time, WeakPoint2Time, WeakPoint3Time, WeakPoint4Time, mstxtName, labelName, CloseOption, Timer, labelName2, labelName3, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeakPoint1Time = WeakPoint1Time
		self.WeakPoint2Time = WeakPoint2Time
		self.WeakPoint3Time = WeakPoint3Time
		self.WeakPoint4Time = WeakPoint4Time
		self.mstxtName = mstxtName
		self.labelName = labelName
		self.CloseOption = CloseOption
		self.Timer = Timer
		self.labelName2 = labelName2
		self.labelName3 = labelName3
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GanonBeastWait:
	ChildNames = ["レーザー発射", "弱点露出", "待機", "復帰"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GanonDemoMoveSeqTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GanonFarAttackRootOnWall:
	ChildNames = ["ビーム攻撃", "ラリー球", "弓矢攻撃", "槍投げ", "氷柱", "火球", "疾風弾", "竜巻", "落雷", "落雷後待機"]

	def __init__(self, Name, PillarMax, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PillarMax = PillarMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class GanonGrudgeNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "出現", "待機", "怒り", "攻撃反応", "気配気づき", "消失", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class GanonNearAttackOnFloorRoot:
	ChildNames = ["ビーム攻撃", "大剣攻撃", "大剣横攻撃", "小剣攻撃", "槍攻撃", "衝撃波"]

	def __init__(self, Name, NearDist, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDist = NearDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class GanonNormalRoot:
	ChildNames = ["未発見", "発見"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GanonReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "デモ待ち大ダメージ", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16


class GanonRecognizeRoot:
	ChildNames = ["前半", "後半"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GanonShockRoot:
	ChildNames = ["ショック", "瀕死時復帰"]

	def __init__(self, Name, IsDoRecoverAction, IsGuardJust, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsDoRecoverAction = IsDoRecoverAction
		self.IsGuardJust = IsGuardJust
		self.Child0 = Child0
		self.Child1 = Child1


class GanonStateChangeRoot:
	ChildNames = ["壁に向かう", "壁張り付き"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GanonThrowActorRoot:
	ChildNames = ["弾消え待ち", "所持", "投げる", "生成待ち"]

	def __init__(self, Name, ThrowActorName, AttackDamage, AtMinDamage, RegisterPartsName, IsThrowQuick, IsWaitBulletDelete, IsSetSystemGroupHandler, IsSendDeleteMessageAtLeave, AddAtackPower, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowActorName = ThrowActorName
		self.AttackDamage = AttackDamage
		self.AtMinDamage = AtMinDamage
		self.RegisterPartsName = RegisterPartsName
		self.IsThrowQuick = IsThrowQuick
		self.IsWaitBulletDelete = IsWaitBulletDelete
		self.IsSetSystemGroupHandler = IsSetSystemGroupHandler
		self.IsSendDeleteMessageAtLeave = IsSendDeleteMessageAtLeave
		self.AddAtackPower = AddAtackPower
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GanonThrowMultiActorRoot:
	ChildNames = ["弾消え待ち", "所持", "投げる", "生成待ち"]

	def __init__(self, Name, PartsName1, PartsName2, PartsName3, PartsName4, PartsName5, PartsName6, PartsName7, PartsName8, ThrowActorName, AttackDamage, AtMinDamage, RegisterPartsName, IsThrowQuick, IsWaitBulletDelete, IsSetSystemGroupHandler, IsSendDeleteMessageAtLeave, AddAtackPower, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName1 = PartsName1
		self.PartsName2 = PartsName2
		self.PartsName3 = PartsName3
		self.PartsName4 = PartsName4
		self.PartsName5 = PartsName5
		self.PartsName6 = PartsName6
		self.PartsName7 = PartsName7
		self.PartsName8 = PartsName8
		self.ThrowActorName = ThrowActorName
		self.AttackDamage = AttackDamage
		self.AtMinDamage = AtMinDamage
		self.RegisterPartsName = RegisterPartsName
		self.IsThrowQuick = IsThrowQuick
		self.IsWaitBulletDelete = IsWaitBulletDelete
		self.IsSetSystemGroupHandler = IsSetSystemGroupHandler
		self.IsSendDeleteMessageAtLeave = IsSendDeleteMessageAtLeave
		self.AddAtackPower = AddAtackPower
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GanonWeaponAttackOnFloor:
	ChildNames = ["接近", "攻撃"]

	def __init__(self, Name, WeaponIdx, CloseDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.CloseDist = CloseDist
		self.Child0 = Child0
		self.Child1 = Child1


class GearRangeSelect:
	ChildNames = ["低速ギア", "高速ギア"]

	def __init__(self, Name, GearThreashold, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GearThreashold = GearThreashold
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class GelEnemyReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ケミカル鎮静", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16


class GerudoHeroSoulGiftRoot:
	ChildNames = ["待機", "発動", "退場"]

	def __init__(self, Name, MaxLength, PosOffset, RotOffset, UseInitMtxForBasePos, UseInitMtxForBaseRot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxLength = MaxLength
		self.PosOffset = PosOffset
		self.RotOffset = RotOffset
		self.UseInitMtxForBasePos = UseInitMtxForBasePos
		self.UseInitMtxForBaseRot = UseInitMtxForBaseRot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GerudoQueenBattle:
	ChildNames = ["チャンス", "プレイヤーを心配", "先導開始", "心配解消", "撤退", "警戒", "通常", "遺物弱点破壊", "雷攻撃無効化"]

	def __init__(self, Name, RetireFrame, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RetireFrame = RetireFrame
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class GetItemBrightBow:
	ChildNames = ["ゲット", "待機"]

	def __init__(self, Name, GetRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GetRadius = GetRadius
		self.Child0 = Child0
		self.Child1 = Child1


class GetItemNormal:
	ChildNames = ["ゲット", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GiantArmorAsWeakPoint:
	ChildNames = ["装備", "非装備"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GiantEarthReleaseAttack:
	ChildNames = ["先行動", "後行動", "準備"]

	def __init__(self, Name, StartHeight, StartDistFromTarget, EarthReleaseActorName, EarthReleasePartsName, AttackPower, EnlargeTime, Range, Scale, UseAfterAction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartHeight = StartHeight
		self.StartDistFromTarget = StartDistFromTarget
		self.EarthReleaseActorName = EarthReleaseActorName
		self.EarthReleasePartsName = EarthReleasePartsName
		self.AttackPower = AttackPower
		self.EnlargeTime = EnlargeTime
		self.Range = Range
		self.Scale = Scale
		self.UseAfterAction = UseAfterAction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GiantEscapeFromDamageWater:
	ChildNames = ["初回探索", "待機", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GiantNavMoveTarget:
	ChildNames = ["直進", "移動", "脱出", "見まわす"]

	def __init__(self, Name, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, TargetVMax, TargetVMin, FrontAngle, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.TargetVMax = TargetVMax
		self.TargetVMin = TargetVMin
		self.FrontAngle = FrontAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GiantNavMoveWithFirstAction:
	ChildNames = ["先行動", "直進", "移動", "脱出", "見まわす"]

	def __init__(self, Name, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, TargetVMax, TargetVMin, FrontAngle, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.TargetVMax = TargetVMax
		self.TargetVMin = TargetVMin
		self.FrontAngle = FrontAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class GiantRoamSelect:
	ChildNames = ["レール移動", "待機", "徘徊"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GiantSleepNormal:
	ChildNames = ["待機", "横になる", "睡眠", "起き上がる"]

	def __init__(self, Name, AwakeRbName, ForceAwakeDist, IsAwakenByHearing, IsWaitAfterAwaken, AwakeDelayTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AwakeRbName = AwakeRbName
		self.ForceAwakeDist = ForceAwakeDist
		self.IsAwakenByHearing = IsAwakenByHearing
		self.IsWaitAfterAwaken = IsWaitAfterAwaken
		self.AwakeDelayTime = AwakeDelayTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GiantSleepReaction:
	ChildNames = ["睡眠", "音反応"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GiantStoneShootAngrySelect:
	ChildNames = ["怒り", "投石"]

	def __init__(self, Name, ThrowableAngryRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowableAngryRate = ThrowableAngryRate
		self.Child0 = Child0
		self.Child1 = Child1


class GolemChemicalResetSelect:
	ChildNames = ["ケミカル復帰", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GolemChemicalVanishedSelect:
	ChildNames = ["ケミカル消失", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GolemClimbedSelect:
	ChildNames = ["対象よじ登り中", "対象通常"]

	def __init__(self, Name, ClimbTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ClimbTime = ClimbTime
		self.Child0 = Child0
		self.Child1 = Child1


class GolemClimbedTimeSelect:
	ChildNames = ["時間内", "時間超過"]

	def __init__(self, Name, LimitTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitTime = LimitTime
		self.Child0 = Child0
		self.Child1 = Child1


class GolemFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SearchExplosiveDist, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchExplosiveDist = SearchExplosiveDist
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class GolemFireREnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, PlayerRecoverFromFallFrames, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerRecoverFromFallFrames = PlayerRecoverFromFallFrames
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class GolemNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "初期待機", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class GolemNoticeWorry:
	ChildNames = ["回転", "待機", "見まわす"]

	def __init__(self, Name, TurnStartAngle, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GolemPartRoot:
	ChildNames = ["投擲生成", "通常"]

	def __init__(self, Name, NormalAS, ActiveAS, ChemFieldScale, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NormalAS = NormalAS
		self.ActiveAS = ActiveAS
		self.ChemFieldScale = ChemFieldScale
		self.Child0 = Child0
		self.Child1 = Child1


class GolemPartsSelect:
	ChildNames = ["両腕有", "右腕のみ", "左腕のみ", "腕なし"]

	def __init__(self, Name, ArmRModelMatrialName, ArmLModelMatrialName, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArmRModelMatrialName = ArmRModelMatrialName
		self.ArmLModelMatrialName = ArmLModelMatrialName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GolemRWeakPointRoot:
	ChildNames = ["リアクション", "通常"]

	def __init__(self, Name, OwnerDamage, IsBreakable, IsSyncDamage, IsShowCriticalEffect, IsNoReaction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OwnerDamage = OwnerDamage
		self.IsBreakable = IsBreakable
		self.IsSyncDamage = IsSyncDamage
		self.IsShowCriticalEffect = IsShowCriticalEffect
		self.IsNoReaction = IsNoReaction
		self.Child0 = Child0
		self.Child1 = Child1


class GolemReaction:
	ChildNames = ["ふっとび", "小ダメージ", "振り落し", "死亡", "起き上がる"]

	def __init__(self, Name, RightArmTgtBodyName, LeftArmTgtBodyName, ClimbLimitTime, ClampRestClimbTime, IgnoreBombTime, BreakArmLXLinkKey, BodyArmLName1, BodyArmLName2, ChmArmLName, ArmLMaterialName, BreakArmRXLinkKey, BodyArmRName1, BodyArmRName2, ChmArmRName, ArmRMaterialName, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RightArmTgtBodyName = RightArmTgtBodyName
		self.LeftArmTgtBodyName = LeftArmTgtBodyName
		self.ClimbLimitTime = ClimbLimitTime
		self.ClampRestClimbTime = ClampRestClimbTime
		self.IgnoreBombTime = IgnoreBombTime
		self.BreakArmLXLinkKey = BreakArmLXLinkKey
		self.BodyArmLName1 = BodyArmLName1
		self.BodyArmLName2 = BodyArmLName2
		self.ChmArmLName = ChmArmLName
		self.ArmLMaterialName = ArmLMaterialName
		self.BreakArmRXLinkKey = BreakArmRXLinkKey
		self.BodyArmRName1 = BodyArmRName1
		self.BodyArmRName2 = BodyArmRName2
		self.ChmArmRName = ChmArmRName
		self.ArmRMaterialName = ArmRMaterialName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class GolemRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, ClimbFinishTime, StandContactHeight, IsBreakContactTree, UpperArmL_PartsKey, LowerArmL_PartsKey, UpperArmR_PartsKey, LowerArmR_PartsKey, ChemicalFieldKey, BodyDeactiveAS, ArmRDeactiveAS, ArmLDeactiveAS, BodyActiveAS, ArmRActiveAS, ArmLActiveAS, BodyMimicAS, ArmRMimicAS, ArmLMimicAS, ShaderASTargetBone, BodyShaderSeqBank, ArmRShaderSeqBank, ArmLShaderSeqBank, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ClimbFinishTime = ClimbFinishTime
		self.StandContactHeight = StandContactHeight
		self.IsBreakContactTree = IsBreakContactTree
		self.UpperArmL_PartsKey = UpperArmL_PartsKey
		self.LowerArmL_PartsKey = LowerArmL_PartsKey
		self.UpperArmR_PartsKey = UpperArmR_PartsKey
		self.LowerArmR_PartsKey = LowerArmR_PartsKey
		self.ChemicalFieldKey = ChemicalFieldKey
		self.BodyDeactiveAS = BodyDeactiveAS
		self.ArmRDeactiveAS = ArmRDeactiveAS
		self.ArmLDeactiveAS = ArmLDeactiveAS
		self.BodyActiveAS = BodyActiveAS
		self.ArmRActiveAS = ArmRActiveAS
		self.ArmLActiveAS = ArmLActiveAS
		self.BodyMimicAS = BodyMimicAS
		self.ArmRMimicAS = ArmRMimicAS
		self.ArmLMimicAS = ArmLMimicAS
		self.ShaderASTargetBone = ShaderASTargetBone
		self.BodyShaderSeqBank = BodyShaderSeqBank
		self.ArmRShaderSeqBank = ArmRShaderSeqBank
		self.ArmLShaderSeqBank = ArmLShaderSeqBank
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class GolemSleepNormal:
	ChildNames = ["待機", "横になる", "睡眠", "起き上がる"]

	def __init__(self, Name, IsAwakenByHearing, IsWaitAfterAwaken, AwakeDelayTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAwakenByHearing = IsAwakenByHearing
		self.IsWaitAfterAwaken = IsWaitAfterAwaken
		self.AwakeDelayTime = AwakeDelayTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GolemSleepTypeSelect:
	ChildNames = ["うつ伏せA", "うつ伏せB", "仰向けA", "仰向けB"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GolemWeakPointRoot:
	ChildNames = ["リアクション", "通常"]

	def __init__(self, Name, OwnerDamage, IsBreakable, IsSyncDamage, IsShowCriticalEffect, IsNoReaction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OwnerDamage = OwnerDamage
		self.IsBreakable = IsBreakable
		self.IsSyncDamage = IsSyncDamage
		self.IsShowCriticalEffect = IsShowCriticalEffect
		self.IsNoReaction = IsNoReaction
		self.Child0 = Child0
		self.Child1 = Child1


class GolfBallRoot:

	def __init__(self, Name, FloatJudgeSmash, IntSmashJudgeFrame, FloatJudgeStop, IntSmashContinueFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FloatJudgeSmash = FloatJudgeSmash
		self.IntSmashJudgeFrame = IntSmashJudgeFrame
		self.FloatJudgeStop = FloatJudgeStop
		self.IntSmashContinueFrame = IntSmashContinueFrame


class GoronCannon:
	ChildNames = ["冷却中", "発射", "発射前待機", "発射後待機"]

	def __init__(self, Name, ActName, Offset, ShotNodeName, IsDrawDebug, RotRadAccel, RotBrake, IsUseShotNodeAngle, ShotCannonBallScale, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActName = ActName
		self.Offset = Offset
		self.ShotNodeName = ShotNodeName
		self.IsDrawDebug = IsDrawDebug
		self.RotRadAccel = RotRadAccel
		self.RotBrake = RotBrake
		self.IsUseShotNodeAngle = IsUseShotNodeAngle
		self.ShotCannonBallScale = ShotCannonBallScale
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GoronHeroDescendentRoot:
	ChildNames = ["ジャンプ", "ジャンプ準備", "プレイヤー接近待機", "プレイヤー追従", "停止", "停止命令", "停止指示", "屈む", "帰還", "待機", "敵に怯える", "減速", "着地", "砲台内", "移動指示", "退避"]

	def __init__(self, Name, PlayerFollowOffset, PlayerNearDist, PlayerLeaveDist, PlayerSeparateDist, GuardEndDelayTime, WhistleReactTimeGo, WhistleReactTimeStop, AppearWaitTime, FollowModeFlagName, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerFollowOffset = PlayerFollowOffset
		self.PlayerNearDist = PlayerNearDist
		self.PlayerLeaveDist = PlayerLeaveDist
		self.PlayerSeparateDist = PlayerSeparateDist
		self.GuardEndDelayTime = GuardEndDelayTime
		self.WhistleReactTimeGo = WhistleReactTimeGo
		self.WhistleReactTimeStop = WhistleReactTimeStop
		self.AppearWaitTime = AppearWaitTime
		self.FollowModeFlagName = FollowModeFlagName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class GoronHeroSoulGiftRoot:
	ChildNames = ["待機", "発動", "退場"]

	def __init__(self, Name, PosOffset, RotOffset, UseInitMtxForBasePos, UseInitMtxForBaseRot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosOffset = PosOffset
		self.RotOffset = RotOffset
		self.UseInitMtxForBasePos = UseInitMtxForBasePos
		self.UseInitMtxForBaseRot = UseInitMtxForBaseRot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GroundAngleSelect:
	ChildNames = ["平地", "斜面"]

	def __init__(self, Name, IsCheckEveryFrame, SlopeAngle, IsCheckActorMtx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.SlopeAngle = SlopeAngle
		self.IsCheckActorMtx = IsCheckActorMtx
		self.Child0 = Child0
		self.Child1 = Child1


class GroundHitSelect:
	ChildNames = ["接地", "通常"]

	def __init__(self, Name, IsActionEndEnd, IsEnterCheck, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsActionEndEnd = IsActionEndEnd
		self.IsEnterCheck = IsEnterCheck
		self.Child0 = Child0
		self.Child1 = Child1


class GrudgeEyeball:
	ChildNames = ["発見", "閉じてダメージ", "閉じて待機", "閉じる", "開けて待機"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class GuardAndRevenge:
	ChildNames = ["ガード", "反撃", "水死"]

	def __init__(self, Name, DrownDepth, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DrownDepth = DrownDepth
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardFlagSelect:
	ChildNames = ["盾構え", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GuardFrequencySelect:
	ChildNames = ["ガード", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianBattleBeamAttack:
	ChildNames = ["チャージ", "照準", "発射"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianBeam:
	ChildNames = ["爆発", "爆発後", "着弾前"]

	def __init__(self, Name, MaxDistance, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistance = MaxDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianBeamAttack:
	ChildNames = ["チャージ", "待機", "照準", "照準準備", "発射", "破壊"]

	def __init__(self, Name, LightRadius, LightLength, LightLengthOffset, AdjustRadius, EarSpeed, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LightRadius = LightRadius
		self.LightLength = LightLength
		self.LightLengthOffset = LightLengthOffset
		self.AdjustRadius = AdjustRadius
		self.EarSpeed = EarSpeed
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class GuardianBezierRailMove:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "移動"]

	def __init__(self, Name, OnRailDistance, FarDistance, Speed, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GuardianChase:
	ChildNames = ["回避", "戦闘", "移動", "範囲外"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GuardianCloseBattle:
	ChildNames = ["ビーム攻撃", "待機", "掴み攻撃"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianDown:
	ChildNames = ["ダウン中", "起き上がり"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMini2ndBattle:
	ChildNames = ["反撃", "反撃終了", "右腕フェイント攻撃", "回転攻撃", "左腕フェイント攻撃", "左腕攻撃", "戦闘攻撃", "戦闘準備", "旋回移動"]

	def __init__(self, Name, AttackHitNum, CounterStopTime, RootNodeName, Arm1NodeName, Arm2NodeName, Arm3NodeName, ASSlotRight, ASSlotLeft, ASSlotBack, RollingInterval, IsIgnoreArmCondition, BaseDist, FarDist, TurnMoveTime, TurnMovePer, TurnMoveStartDist, CounterStartDamageCount, CounterStartTime, CheckOnNoNavMesh, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackHitNum = AttackHitNum
		self.CounterStopTime = CounterStopTime
		self.RootNodeName = RootNodeName
		self.Arm1NodeName = Arm1NodeName
		self.Arm2NodeName = Arm2NodeName
		self.Arm3NodeName = Arm3NodeName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.RollingInterval = RollingInterval
		self.IsIgnoreArmCondition = IsIgnoreArmCondition
		self.BaseDist = BaseDist
		self.FarDist = FarDist
		self.TurnMoveTime = TurnMoveTime
		self.TurnMovePer = TurnMovePer
		self.TurnMoveStartDist = TurnMoveStartDist
		self.CounterStartDamageCount = CounterStartDamageCount
		self.CounterStartTime = CounterStartTime
		self.CheckOnNoNavMesh = CheckOnNoNavMesh
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class GuardianMini2ndBattleAttack:
	ChildNames = ["戦闘予兆", "戦闘予兆終了", "戦闘攻撃", "戦闘攻撃終了"]

	def __init__(self, Name, AscendingCurrentName, AscendingCurrentTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AscendingCurrentName = AscendingCurrentName
		self.AscendingCurrentTime = AscendingCurrentTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GuardianMiniBattle:
	ChildNames = ["反撃", "右腕フェイント攻撃", "回転攻撃", "左腕フェイント攻撃", "左腕攻撃", "戦闘攻撃", "戦闘準備", "旋回移動"]

	def __init__(self, Name, RootNodeName, Arm1NodeName, Arm2NodeName, Arm3NodeName, ASSlotRight, ASSlotLeft, ASSlotBack, RollingInterval, IsIgnoreArmCondition, BaseDist, FarDist, TurnMoveTime, TurnMovePer, TurnMoveStartDist, CounterStartDamageCount, CounterStartTime, CheckOnNoNavMesh, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RootNodeName = RootNodeName
		self.Arm1NodeName = Arm1NodeName
		self.Arm2NodeName = Arm2NodeName
		self.Arm3NodeName = Arm3NodeName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.RollingInterval = RollingInterval
		self.IsIgnoreArmCondition = IsIgnoreArmCondition
		self.BaseDist = BaseDist
		self.FarDist = FarDist
		self.TurnMoveTime = TurnMoveTime
		self.TurnMovePer = TurnMovePer
		self.TurnMoveStartDist = TurnMoveStartDist
		self.CounterStartDamageCount = CounterStartDamageCount
		self.CounterStartTime = CounterStartTime
		self.CheckOnNoNavMesh = CheckOnNoNavMesh
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class GuardianMiniBattleStateSelect:
	ChildNames = ["最終段階", "第一段階", "第二段階"]

	def __init__(self, Name, SecondLifeRatio, FinalLifeRatio, IsEnterOnly, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SecondLifeRatio = SecondLifeRatio
		self.FinalLifeRatio = FinalLifeRatio
		self.IsEnterOnly = IsEnterOnly
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniBeam:
	ChildNames = ["後処理", "着弾前"]

	def __init__(self, Name, MaxDistance, IsDelete, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistance = MaxDistance
		self.IsDelete = IsDelete
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniBeamAttack:
	ChildNames = ["ビーム準備", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, HeadNodeName, AttackInterval, EndShaderASFrame, LoopShaderASName, EndShaderASName, PreLaunchEffectName, IsChangeable, IsFinalBattle, InDirAngle, FluctuationRange, FluctuationSpan, TargetOffsetY, NodeName, IsValidGuide, IsIgnoreSmallHit, AimEffectName, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeadNodeName = HeadNodeName
		self.AttackInterval = AttackInterval
		self.EndShaderASFrame = EndShaderASFrame
		self.LoopShaderASName = LoopShaderASName
		self.EndShaderASName = EndShaderASName
		self.PreLaunchEffectName = PreLaunchEffectName
		self.IsChangeable = IsChangeable
		self.IsFinalBattle = IsFinalBattle
		self.InDirAngle = InDirAngle
		self.FluctuationRange = FluctuationRange
		self.FluctuationSpan = FluctuationSpan
		self.TargetOffsetY = TargetOffsetY
		self.NodeName = NodeName
		self.IsValidGuide = IsValidGuide
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.AimEffectName = AimEffectName
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniBeamAttackMove:
	ChildNames = ["移動"]

	def __init__(self, Name, MoveTime, BaseNode, BeamSpeed, AttackInterval, TargetDistOffset, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveTime = MoveTime
		self.BaseNode = BaseNode
		self.BeamSpeed = BeamSpeed
		self.AttackInterval = AttackInterval
		self.TargetDistOffset = TargetDistOffset
		self.Child0 = Child0


class GuardianMiniBeamAttackNoWait:
	ChildNames = ["ビーム準備", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, HeadNodeName, AttackInterval, EndShaderASFrame, LoopShaderASName, EndShaderASName, PreLaunchEffectName, IsChangeable, IsFinalBattle, InDirAngle, FluctuationRange, FluctuationSpan, TargetOffsetY, NodeName, IsValidGuide, IsIgnoreSmallHit, AimEffectName, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeadNodeName = HeadNodeName
		self.AttackInterval = AttackInterval
		self.EndShaderASFrame = EndShaderASFrame
		self.LoopShaderASName = LoopShaderASName
		self.EndShaderASName = EndShaderASName
		self.PreLaunchEffectName = PreLaunchEffectName
		self.IsChangeable = IsChangeable
		self.IsFinalBattle = IsFinalBattle
		self.InDirAngle = InDirAngle
		self.FluctuationRange = FluctuationRange
		self.FluctuationSpan = FluctuationSpan
		self.TargetOffsetY = TargetOffsetY
		self.NodeName = NodeName
		self.IsValidGuide = IsValidGuide
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.AimEffectName = AimEffectName
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniBeamToExplosives:
	ChildNames = ["ビーム準備", "後ずさり", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ExplosivesAvoidDist, HeadNodeName, AttackInterval, EndShaderASFrame, LoopShaderASName, EndShaderASName, PreLaunchEffectName, IsChangeable, IsFinalBattle, InDirAngle, FluctuationRange, FluctuationSpan, TargetOffsetY, NodeName, IsValidGuide, IsIgnoreSmallHit, AimEffectName, BreathName, AttackAngle, AttackRatio, BreathSize, EnlargeTime, IsEndAfterAttack, IsDeleteBreath, AttackIntervalIntensity, GlobalNoAtkTime, IsUpdateNoticeState, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.HeadNodeName = HeadNodeName
		self.AttackInterval = AttackInterval
		self.EndShaderASFrame = EndShaderASFrame
		self.LoopShaderASName = LoopShaderASName
		self.EndShaderASName = EndShaderASName
		self.PreLaunchEffectName = PreLaunchEffectName
		self.IsChangeable = IsChangeable
		self.IsFinalBattle = IsFinalBattle
		self.InDirAngle = InDirAngle
		self.FluctuationRange = FluctuationRange
		self.FluctuationSpan = FluctuationSpan
		self.TargetOffsetY = TargetOffsetY
		self.NodeName = NodeName
		self.IsValidGuide = IsValidGuide
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.AimEffectName = AimEffectName
		self.BreathName = BreathName
		self.AttackAngle = AttackAngle
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.IsEndAfterAttack = IsEndAfterAttack
		self.IsDeleteBreath = IsDeleteBreath
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class GuardianMiniBlownOff:
	ChildNames = ["ふっとび"]

	def __init__(self, Name, RotNeckAngle, RotNeckSpeed, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotNeckAngle = RotNeckAngle
		self.RotNeckSpeed = RotNeckSpeed
		self.Child0 = Child0


class GuardianMiniChangeWeapon:
	ChildNames = ["切替終了", "切替開始", "武器切替"]

	def __init__(self, Name, RotSpeed, RotValue, RootNodeName, DamageNodeName, DamageASName, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.RotValue = RotValue
		self.RootNodeName = RootNodeName
		self.DamageNodeName = DamageNodeName
		self.DamageASName = DamageASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniFinalBattle:
	ChildNames = ["戦闘予兆点滅", "戦闘予兆移動", "戦闘予兆開始", "戦闘攻撃", "戦闘準備", "戦闘開始"]

	def __init__(self, Name, ASSlotRight, ASSlotLeft, ASSlotBack, AttackHitNum, IsPreAttackMove, RotNeckRate, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.AttackHitNum = AttackHitNum
		self.IsPreAttackMove = IsPreAttackMove
		self.RotNeckRate = RotNeckRate
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class GuardianMiniFindPlayer:
	ChildNames = ["ケミカル仲間招来", "ナビメッシュ無し", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "武器ケミカル付与", "武器投げ", "気づき", "速攻"]

	def __init__(self, Name, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, ChemicalSearchDist, NoSearchDist, Voltage, ChemicalActionDist, ThrowWeaponPer, ThrowWeaponDist, NoChemSearchWpIdx, NoBurnWaterDepth, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.ChemicalSearchDist = ChemicalSearchDist
		self.NoSearchDist = NoSearchDist
		self.Voltage = Voltage
		self.ChemicalActionDist = ChemicalActionDist
		self.ThrowWeaponPer = ThrowWeaponPer
		self.ThrowWeaponDist = ThrowWeaponDist
		self.NoChemSearchWpIdx = NoChemSearchWpIdx
		self.NoBurnWaterDepth = NoBurnWaterDepth
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class GuardianMiniGroggy:
	ChildNames = ["チャンス", "終了"]

	def __init__(self, Name, ChanceTime, RestartASName, DefaultASName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChanceTime = ChanceTime
		self.RestartASName = RestartASName
		self.DefaultASName = DefaultASName
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniGuardSelect:
	ChildNames = ["ノーガード", "右腕ガード", "左腕ガード"]

	def __init__(self, Name, ASSlotRight, ASSlotLeft, ASSlotBack, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniNoWeaponSelect:
	ChildNames = ["武器がある", "武器がない", "盾はある"]

	def __init__(self, Name, IsSelectFirstTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSelectFirstTime = IsSelectFirstTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianMiniOnNoNavMesh:
	ChildNames = ["アイスメーカー上", "ナビメッシュなし"]

	def __init__(self, Name, ChangeToIceTimer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeToIceTimer = ChangeToIceTimer
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniRangeKeepMove:
	ChildNames = ["強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動"]

	def __init__(self, Name, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class GuardianMiniReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "チャンス", "凍結", "大落下", "小ダメージ", "崩れ落ち", "左手ショック", "左手弾かれ", "左手超ショック", "弾かれ", "後ろ手ショック", "後ろ手弾かれ", "後ろ手超ショック", "武器切替", "死亡", "瀕死", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, RootNodeName, Arm1NodeName, Arm2NodeName, Arm3NodeName, ASSlotRight, ASSlotLeft, ASSlotBack, PreAttackASRight, PreAttackASLeft, JustGuardNumForBreak, IsChangeWeapon, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Child19, Child20, Child21, Child22, Child23, Child24, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RootNodeName = RootNodeName
		self.Arm1NodeName = Arm1NodeName
		self.Arm2NodeName = Arm2NodeName
		self.Arm3NodeName = Arm3NodeName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.PreAttackASRight = PreAttackASRight
		self.PreAttackASLeft = PreAttackASLeft
		self.JustGuardNumForBreak = JustGuardNumForBreak
		self.IsChangeWeapon = IsChangeWeapon
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18
		self.Child19 = Child19
		self.Child20 = Child20
		self.Child21 = Child21
		self.Child22 = Child22
		self.Child23 = Child23
		self.Child24 = Child24


class GuardianMiniRecognizeTarget:
	ChildNames = ["未発見", "発見"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniRollingAttackMove:
	ChildNames = ["チャンス", "バックステップ", "回転予兆", "回転待機", "回転後退", "回転後退終了", "回転終了", "強制後退", "戦闘待機", "戦闘後ずさり", "戦闘歩行", "横移動", "突進停止", "突進前ターン", "追加攻撃"]

	def __init__(self, Name, RootNodeName, AttackNodeName, AttackASName, RollingNumMin, RollingNumMax, RollingWaitTime, RollingIntervalTime, StopRollingNum, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, AttackType, RotSpeed, RushRotSpeedRatio, BackWalkRotSpeedRatio, BackWalkMinTime, BackWalkRollingStartTime, BackWalkDist, RushAttackImpulse, RollingStopTime, IsValidChanceTime, CrashDamage, BreakPillarTime, CloseDist, FarDist, WeaponIdx, OutDist, BaseDist, SpaceDist, SpaceAngle, BackTimeMin, BackTimeMax, LeaveTimerMin, LeaveTimerMax, IsCheckBack, IsCheckReachable, PosVibrateFrame, RotVelVibrateFrame, NoMoveDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RootNodeName = RootNodeName
		self.AttackNodeName = AttackNodeName
		self.AttackASName = AttackASName
		self.RollingNumMin = RollingNumMin
		self.RollingNumMax = RollingNumMax
		self.RollingWaitTime = RollingWaitTime
		self.RollingIntervalTime = RollingIntervalTime
		self.StopRollingNum = StopRollingNum
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.AttackType = AttackType
		self.RotSpeed = RotSpeed
		self.RushRotSpeedRatio = RushRotSpeedRatio
		self.BackWalkRotSpeedRatio = BackWalkRotSpeedRatio
		self.BackWalkMinTime = BackWalkMinTime
		self.BackWalkRollingStartTime = BackWalkRollingStartTime
		self.BackWalkDist = BackWalkDist
		self.RushAttackImpulse = RushAttackImpulse
		self.RollingStopTime = RollingStopTime
		self.IsValidChanceTime = IsValidChanceTime
		self.CrashDamage = CrashDamage
		self.BreakPillarTime = BreakPillarTime
		self.CloseDist = CloseDist
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.SpaceDist = SpaceDist
		self.SpaceAngle = SpaceAngle
		self.BackTimeMin = BackTimeMin
		self.BackTimeMax = BackTimeMax
		self.LeaveTimerMin = LeaveTimerMin
		self.LeaveTimerMax = LeaveTimerMax
		self.IsCheckBack = IsCheckBack
		self.IsCheckReachable = IsCheckReachable
		self.PosVibrateFrame = PosVibrateFrame
		self.RotVelVibrateFrame = RotVelVibrateFrame
		self.NoMoveDist = NoMoveDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class GuardianMiniRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, NeckRotRatio, JustGuardNumForBreak, RotStopSpeed, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NeckRotRatio = NeckRotRatio
		self.JustGuardNumForBreak = JustGuardNumForBreak
		self.RotStopSpeed = RotStopSpeed
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class GuardianMiniTargetOnScalffold:
	ChildNames = ["行動", "遠距離行動"]

	def __init__(self, Name, FarDist, NearDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.NearDist = NearDist
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniTransformSelect:
	ChildNames = ["変形前", "変形後"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianMiniViewWait:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, RootNodeName, Arm1NodeName, Arm2NodeName, Arm3NodeName, ASSlotRight, ASSlotLeft, ASSlotBack, IsPartialBind, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RootNodeName = RootNodeName
		self.Arm1NodeName = Arm1NodeName
		self.Arm2NodeName = Arm2NodeName
		self.Arm3NodeName = Arm3NodeName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.IsPartialBind = IsPartialBind
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianRoam:
	ChildNames = ["移動", "見回す"]

	def __init__(self, Name, MoveRadius, MoveTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveRadius = MoveRadius
		self.MoveTime = MoveTime
		self.Child0 = Child0
		self.Child1 = Child1


class GuardianRoot:
	ChildNames = ["ダウン", "マグネ", "リアクション", "仮死", "待機", "落雷スタン", "見失い", "視覚反応", "起動", "追跡", "退避", "音反応"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class GuardianTargetLost:
	ChildNames = ["周囲を見る", "移動", "音反応"]

	def __init__(self, Name, MoveRange, BackOffset, AirThreshold, LostCountMax, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveRange = MoveRange
		self.BackOffset = BackOffset
		self.AirThreshold = AirThreshold
		self.LostCountMax = LostCountMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class GuardianWait:
	ChildNames = ["ランダム移動", "レール移動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class GyroActivateTerminal:
	ChildNames = ["待機", "起動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class HangedLamp:
	ChildNames = ["待機", "発火"]

	def __init__(self, Name, DisableImpulseByArrow, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisableImpulseByArrow = DisableImpulseByArrow
		self.Child0 = Child0
		self.Child1 = Child1


class HasPreActorSelect:
	ChildNames = ["存在しない", "存在する"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class HaveNoWeaponSelector:
	ChildNames = ["所持", "非所持"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class HeightSelectTwoAction:
	ChildNames = ["レンジ内", "レンジ外"]

	def __init__(self, Name, HeightMin, HeightMax, SelectCheckInterval, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeightMin = HeightMin
		self.HeightMax = HeightMax
		self.SelectCheckInterval = SelectCheckInterval
		self.Child0 = Child0
		self.Child1 = Child1


class HeroSoulGiftRoot:
	ChildNames = ["待機", "発動", "退場"]

	def __init__(self, Name, PosOffset, RotOffset, UseInitMtxForBasePos, UseInitMtxForBaseRot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosOffset = PosOffset
		self.RotOffset = RotOffset
		self.UseInitMtxForBasePos = UseInitMtxForBasePos
		self.UseInitMtxForBaseRot = UseInitMtxForBaseRot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HiddenKorokRoot:
	ChildNames = ["ひるむ", "振り向く", "未出現", "遁走"]

	def __init__(self, Name, PainTalkHitSpeed, PainTalkDistance, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PainTalkHitSpeed = PainTalkHitSpeed
		self.PainTalkDistance = PainTalkDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class HiddenOctarockFindPlayer:
	ChildNames = ["戦闘", "気づき", "近づき", "隠れる"]

	def __init__(self, Name, FarDist, WeaponIdx, ActorRadius, LostTimer, LostDistOffset, NoticeDelayTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.ActorRadius = ActorRadius
		self.LostTimer = LostTimer
		self.LostDistOffset = LostDistOffset
		self.NoticeDelayTime = NoticeDelayTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class HiddenOctarockNormal:
	ChildNames = ["カツラ反応", "プレイヤー発見", "リロード", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "隠れる", "音気づき", "飛び出す"]

	def __init__(self, Name, IsSitDown, IsHitGround, OptionHitReactionDelay, IsReactionByWigHit, IsHide, IsIvalidateSight, IsSealHearing, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSitDown = IsSitDown
		self.IsHitGround = IsHitGround
		self.OptionHitReactionDelay = OptionHitReactionDelay
		self.IsReactionByWigHit = IsReactionByWigHit
		self.IsHide = IsHide
		self.IsIvalidateSight = IsIvalidateSight
		self.IsSealHearing = IsSealHearing
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class HiddenOctarockSearchTarget:
	ChildNames = ["出現待機", "気づき", "飛び出す"]

	def __init__(self, Name, NoticeTerrorLevel, NoticeWorryRange, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.NoticeWorryRange = NoticeWorryRange
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HomePosDistanceSelector:
	ChildNames = ["レンジ内", "レンジ外"]

	def __init__(self, Name, BoundaryDistance, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoundaryDistance = BoundaryDistance
		self.Child0 = Child0
		self.Child1 = Child1


class Horse:
	ChildNames = ["凍結", "凍結・痺れ終了待ち", "奈落復帰", "死亡", "泳ぐ", "泳ぐ終了待ち", "痺れ", "落下", "落馬終了待ち", "非騎乗", "騎乗"]

	def __init__(self, Name, DistanceFall, DistanceFallDie, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceFall = DistanceFall
		self.DistanceFallDie = DistanceFallDie
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class HorseCheckLineOfSightSelector:
	ChildNames = ["全方向失敗", "前方成功", "後方成功"]

	def __init__(self, Name, DirectionNum, DirectionAngle, Distance, RadiusScale, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DirectionNum = DirectionNum
		self.DirectionAngle = DirectionAngle
		self.Distance = Distance
		self.RadiusScale = RadiusScale
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HorseDamageTypeSelect:
	ChildNames = ["その他", "継続ダメージ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class HorseEscapeRouteRailAI:
	ChildNames = ["指定位置に移動"]

	def __init__(self, Name, UpdatePosDistance, Count, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpdatePosDistance = UpdatePosDistance
		self.Count = Count
		self.Child0 = Child0


class HorseFollow:
	ChildNames = ["うろうろする", "追いかける(近い)", "追いかける(遠い)"]

	def __init__(self, Name, DistanceSuccessEnd, DistanceMovingToward, DistanceRequestingPath, DistanceGivingUp, DistanceThresholdCry, DistanceCheckAvoidance, TargetVelocitySuccessEnd, UpdateTargetPosFrames, UpdateTargetPosFramesNear, SuccessEndDelays, SelfPositionOffsetLocal, SideDistance, TargetVelocityDistanceSec, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, CanIgnorePlayer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceSuccessEnd = DistanceSuccessEnd
		self.DistanceMovingToward = DistanceMovingToward
		self.DistanceRequestingPath = DistanceRequestingPath
		self.DistanceGivingUp = DistanceGivingUp
		self.DistanceThresholdCry = DistanceThresholdCry
		self.DistanceCheckAvoidance = DistanceCheckAvoidance
		self.TargetVelocitySuccessEnd = TargetVelocitySuccessEnd
		self.UpdateTargetPosFrames = UpdateTargetPosFrames
		self.UpdateTargetPosFramesNear = UpdateTargetPosFramesNear
		self.SuccessEndDelays = SuccessEndDelays
		self.SelfPositionOffsetLocal = SelfPositionOffsetLocal
		self.SideDistance = SideDistance
		self.TargetVelocityDistanceSec = TargetVelocityDistanceSec
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.CanIgnorePlayer = CanIgnorePlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HorseGoToEatAI:
	ChildNames = ["移動", "食べる"]

	def __init__(self, Name, TimeoutFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TimeoutFrame = TimeoutFrame
		self.Child0 = Child0
		self.Child1 = Child1


class HorseLoopTargetAndWaitAI:
	ChildNames = ["待機", "指定位置に移動"]

	def __init__(self, Name, ChangeWaitRate, MaxWaitTime, MinWaitTime, TargetName, IsFlip, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeWaitRate = ChangeWaitRate
		self.MaxWaitTime = MaxWaitTime
		self.MinWaitTime = MinWaitTime
		self.TargetName = TargetName
		self.IsFlip = IsFlip
		self.Child0 = Child0
		self.Child1 = Child1


class HorseMoveToPlayer:
	ChildNames = ["うろうろする", "旋回", "追いかける(近い)", "追いかける(遠い)"]

	def __init__(self, Name, DistanceSuccessEndIfInterrupted, DistanceResetGearInput, DistanceSuccessEnd, DistanceMovingToward, DistanceRequestingPath, DistanceGivingUp, DistanceThresholdCry, DistanceCheckAvoidance, TargetVelocitySuccessEnd, UpdateTargetPosFrames, UpdateTargetPosFramesNear, SuccessEndDelays, SelfPositionOffsetLocal, SideDistance, TargetVelocityDistanceSec, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, CanIgnorePlayer, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceSuccessEndIfInterrupted = DistanceSuccessEndIfInterrupted
		self.DistanceResetGearInput = DistanceResetGearInput
		self.DistanceSuccessEnd = DistanceSuccessEnd
		self.DistanceMovingToward = DistanceMovingToward
		self.DistanceRequestingPath = DistanceRequestingPath
		self.DistanceGivingUp = DistanceGivingUp
		self.DistanceThresholdCry = DistanceThresholdCry
		self.DistanceCheckAvoidance = DistanceCheckAvoidance
		self.TargetVelocitySuccessEnd = TargetVelocitySuccessEnd
		self.UpdateTargetPosFrames = UpdateTargetPosFrames
		self.UpdateTargetPosFramesNear = UpdateTargetPosFramesNear
		self.SuccessEndDelays = SuccessEndDelays
		self.SelfPositionOffsetLocal = SelfPositionOffsetLocal
		self.SideDistance = SideDistance
		self.TargetVelocityDistanceSec = TargetVelocityDistanceSec
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.CanIgnorePlayer = CanIgnorePlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class HorseNatureSelectAI:
	ChildNames = ["おとなしい", "気性が荒い", "臆病"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HorseNotRidden:
	ChildNames = ["うろつく", "うろつく(逃走直後)", "ダメージリアクション", "プレイヤの場所へ移動", "前攻撃", "前攻撃(静止のまま)", "待機(静止)", "後攻撃", "後攻撃(静止のまま)", "逃走", "逃走(小)", "逃走(火)", "逃走失敗後", "食べに行く", "食べる(手持ち)"]

	def __init__(self, Name, NearHorseAssociationDistance, EscapeCountThreshold, EscapeDelayFramesMin, EscapeDelayFramesMax, CallDelayFrames, AttackFrontDistance, AttackFrontAngleCos, AttackBackDistance, AttackBackAngleCos, AttackDefinitelyDistance, AttackIntervalFrames, MoveAttackCLOSDistanceByRadius, CarriedItemPosRTYOffset, CarriedItemPosRTYWidth, CarriedItemCosThresholdForEat, StaggerVelocityThreshold, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearHorseAssociationDistance = NearHorseAssociationDistance
		self.EscapeCountThreshold = EscapeCountThreshold
		self.EscapeDelayFramesMin = EscapeDelayFramesMin
		self.EscapeDelayFramesMax = EscapeDelayFramesMax
		self.CallDelayFrames = CallDelayFrames
		self.AttackFrontDistance = AttackFrontDistance
		self.AttackFrontAngleCos = AttackFrontAngleCos
		self.AttackBackDistance = AttackBackDistance
		self.AttackBackAngleCos = AttackBackAngleCos
		self.AttackDefinitelyDistance = AttackDefinitelyDistance
		self.AttackIntervalFrames = AttackIntervalFrames
		self.MoveAttackCLOSDistanceByRadius = MoveAttackCLOSDistanceByRadius
		self.CarriedItemPosRTYOffset = CarriedItemPosRTYOffset
		self.CarriedItemPosRTYWidth = CarriedItemPosRTYWidth
		self.CarriedItemCosThresholdForEat = CarriedItemCosThresholdForEat
		self.StaggerVelocityThreshold = StaggerVelocityThreshold
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class HorsePrevRiddenStatusSelector:
	ChildNames = ["NPC騎乗", "プレイヤー騎乗", "敵騎乗", "騎乗無し"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class HorseReins:
	ChildNames = ["再生"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class HorseRiddenAI:
	ChildNames = ["NPCが騎乗", "従う", "敵が騎乗", "暴れる", "落馬させる"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class HorseRiddenByEnemyAI:
	ChildNames = ["待機", "指定位置に移動", "指定方向を向く", "突進", "落馬させる", "追跡・並走", "通常"]

	def __init__(self, Name, AngryASPeriods, FramesRetryNormalActionAtFailed, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngryASPeriods = AngryASPeriods
		self.FramesRetryNormalActionAtFailed = FramesRetryNormalActionAtFailed
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class HorseRiddenByNPC:
	ChildNames = ["ついていく", "待機", "徘徊", "指定位置に移動", "指定位置に移動(正確)", "指定方向を向く", "泳ぐ", "泳ぐ(待機)", "逃走"]

	def __init__(self, Name, NavMeshCharacterScaleAtPrecise, IsEscapeFromSameActorType, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NavMeshCharacterScaleAtPrecise = NavMeshCharacterScaleAtPrecise
		self.IsEscapeFromSameActorType = IsEscapeFromSameActorType
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class HorseRideChargeAttack:
	ChildNames = ["待機", "指令"]

	def __init__(self, Name, UpperBodyASSlot, LowerBodyASSlot, WeaponIdx, AttackableAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot
		self.WeaponIdx = WeaponIdx
		self.AttackableAngle = AttackableAngle
		self.Child0 = Child0
		self.Child1 = Child1


class HorseRideChaseBattleAttackMove:
	ChildNames = ["攻撃", "追跡指令"]

	def __init__(self, Name, SlowDownDist, SpeedUpDist, BaseDist, OutDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlowDownDist = SlowDownDist
		self.SpeedUpDist = SpeedUpDist
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.Child0 = Child0
		self.Child1 = Child1


class HorseRideChaseBattleMove:
	ChildNames = ["ギア指令", "待機", "追跡指令"]

	def __init__(self, Name, SlowDownDist, SpeedUpDist, BaseDist, OutDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlowDownDist = SlowDownDist
		self.SpeedUpDist = SpeedUpDist
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HorseRideDamagedSelector:
	ChildNames = ["それ以外", "騎乗"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class HorseRideEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "攻撃待機"]

	def __init__(self, Name, AttackRadius, WeaponIdx, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRadius = AttackRadius
		self.WeaponIdx = WeaponIdx
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class HorseRideEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class HorseRideEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, SightAwarenessScale, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SightAwarenessScale = SightAwarenessScale
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class HorseRideMoveTo:
	ChildNames = ["待機", "指令"]

	def __init__(self, Name, UpperBodyASSlot, LowerBodyASSlot, FinRadius, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class HorseRideRangeKeepMove:
	ChildNames = ["待機", "指令"]

	def __init__(self, Name, OutDist, BaseDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.Child0 = Child0
		self.Child1 = Child1


class HorseRideShooterFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, ShootBaseDist, ShootDistRatio, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootBaseDist = ShootBaseDist
		self.ShootDistRatio = ShootDistRatio
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class HorseRideShootingEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "減速指令", "画面外攻撃", "追跡指令"]

	def __init__(self, Name, TrackTime, TrackTimeRand, SlowTime, SlowTimeRand, OutScreenDist, OutScreenAttackNum, OutScrnAtkOffset, OutScrnAtkOffsetY, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TrackTime = TrackTime
		self.TrackTimeRand = TrackTimeRand
		self.SlowTime = SlowTime
		self.SlowTimeRand = SlowTimeRand
		self.OutScreenDist = OutScreenDist
		self.OutScreenAttackNum = OutScreenAttackNum
		self.OutScrnAtkOffset = OutScrnAtkOffset
		self.OutScrnAtkOffsetY = OutScrnAtkOffsetY
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class HorseRideTurn:
	ChildNames = ["待機", "指令"]

	def __init__(self, Name, FinAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinAngle = FinAngle
		self.Child0 = Child0
		self.Child1 = Child1


class HorseWanderAI:
	ChildNames = ["移動", "移動(パスあり)", "移動(リーダーあり)"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class IAIAttack:
	ChildNames = ["斬り付け", "駆け寄り"]

	def __init__(self, Name, OffsetLR, WeaponIdx, CloseDistLR, ClsoeDistFB, TiredAngle, IsAbleSkipNear, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetLR = OffsetLR
		self.WeaponIdx = WeaponIdx
		self.CloseDistLR = CloseDistLR
		self.ClsoeDistFB = ClsoeDistFB
		self.TiredAngle = TiredAngle
		self.IsAbleSkipNear = IsAbleSkipNear
		self.Child0 = Child0
		self.Child1 = Child1


class IbutsuWaterFallRoot:
	ChildNames = ["停止中", "完全停止", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class IceEnemyFeintBattle:
	ChildNames = ["フェイント", "戦闘攻撃", "戦闘準備", "追撃ち攻撃"]

	def __init__(self, Name, IsAttackEnd, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAttackEnd = IsAttackEnd
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class IceMakerBlock:
	ChildNames = ["生成中", "通常"]

	def __init__(self, Name, SubRigidStartOffset, SubRigidEndOffset, SubRigidExOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubRigidStartOffset = SubRigidStartOffset
		self.SubRigidEndOffset = SubRigidEndOffset
		self.SubRigidExOffset = SubRigidExOffset
		self.Child0 = Child0
		self.Child1 = Child1


class InDemoSelect:
	ChildNames = ["デモ中", "デモ終了", "非参加デモ"]

	def __init__(self, Name, DemoFile, DemoEntryPoint, OtherDemoNoRun, ForceChangeDemo, DemoRetDelayMax, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DemoFile = DemoFile
		self.DemoEntryPoint = DemoEntryPoint
		self.OtherDemoNoRun = OtherDemoNoRun
		self.ForceChangeDemo = ForceChangeDemo
		self.DemoRetDelayMax = DemoRetDelayMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class InForceEnemyLostAreaSelect:
	ChildNames = ["エリア内", "エリア外"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class InTerritorySelector:
	ChildNames = ["範囲内", "範囲外"]

	def __init__(self, Name, TerritoryArea, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryArea = TerritoryArea
		self.Child0 = Child0
		self.Child1 = Child1


class InWaterKeepSelect:
	ChildNames = ["水上", "水中"]

	def __init__(self, Name, InWaterDepth, IsCheckEveryFrame, IsForceChange, OutWaterDepth, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.IsForceChange = IsForceChange
		self.OutWaterDepth = OutWaterDepth
		self.Child0 = Child0
		self.Child1 = Child1


class InWaterSelect:
	ChildNames = ["水上", "水中"]

	def __init__(self, Name, InWaterDepth, IsCheckEveryFrame, IsForceChange, OutWaterDepth, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.IsForceChange = IsForceChange
		self.OutWaterDepth = OutWaterDepth
		self.Child0 = Child0
		self.Child1 = Child1


class IncredibleAction:
	ChildNames = ["インクレディブル"]

	def __init__(self, Name, IsInvincible, IsUnmoving, IsNoCollide, IsUseIncredibleActionDCCallback, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsInvincible = IsInvincible
		self.IsUnmoving = IsUnmoving
		self.IsNoCollide = IsNoCollide
		self.IsUseIncredibleActionDCCallback = IsUseIncredibleActionDCCallback
		self.Child0 = Child0


class InitFromInCarryBoxSelect:
	ChildNames = ["抱持あり", "抱持なし"]

	def __init__(self, Name, IsResetInCarryBoxFlag, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsResetInCarryBoxFlag = IsResetInCarryBoxFlag
		self.Child0 = Child0
		self.Child1 = Child1


class InsectEscape:
	ChildNames = ["移動"]

	def __init__(self, Name, InWater, RunAwayDistanceMax, RunAwayDistanceMin, RunAwayHeightOffset, AllowRandAngleVertical, AllowRandAngleHorizontal, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWater = InWater
		self.RunAwayDistanceMax = RunAwayDistanceMax
		self.RunAwayDistanceMin = RunAwayDistanceMin
		self.RunAwayHeightOffset = RunAwayHeightOffset
		self.AllowRandAngleVertical = AllowRandAngleVertical
		self.AllowRandAngleHorizontal = AllowRandAngleHorizontal
		self.Child0 = Child0


class InsectFairyRoot:
	ChildNames = ["ロケーターわき出し", "死亡", "解凍後", "逃走", "通常行動"]

	def __init__(self, Name, IsEscapeInWater, IsDeleteWhenDead, IsDeadWhenPut, IsEscapeWhenPut, IsDeadWhenDrop, InvalidTgtTimerVal, InvalidEscapeTimerVal, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEscapeInWater = IsEscapeInWater
		self.IsDeleteWhenDead = IsDeleteWhenDead
		self.IsDeadWhenPut = IsDeadWhenPut
		self.IsEscapeWhenPut = IsEscapeWhenPut
		self.IsDeadWhenDrop = IsDeadWhenDrop
		self.InvalidTgtTimerVal = InvalidTgtTimerVal
		self.InvalidEscapeTimerVal = InvalidEscapeTimerVal
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class InsectRoam:
	ChildNames = ["徘徊待機", "徘徊歩行"]

	def __init__(self, Name, TerritoryRadius, TerritoryRadiusRnd, MoveDist, MoveSpeed, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryRadius = TerritoryRadius
		self.TerritoryRadiusRnd = TerritoryRadiusRnd
		self.MoveDist = MoveDist
		self.MoveSpeed = MoveSpeed
		self.Child0 = Child0
		self.Child1 = Child1


class InsectRoot:
	ChildNames = ["ロケーターわき出し", "死亡", "逃走", "通常行動"]

	def __init__(self, Name, IsEscapeInWater, IsDeleteWhenDead, IsDeadWhenPut, IsEscapeWhenPut, IsDeadWhenDrop, InvalidTgtTimerVal, InvalidEscapeTimerVal, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEscapeInWater = IsEscapeInWater
		self.IsDeleteWhenDead = IsDeleteWhenDead
		self.IsDeadWhenPut = IsDeadWhenPut
		self.IsEscapeWhenPut = IsEscapeWhenPut
		self.IsDeadWhenDrop = IsDeadWhenDrop
		self.InvalidTgtTimerVal = InvalidTgtTimerVal
		self.InvalidEscapeTimerVal = InvalidEscapeTimerVal
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class InvincibleHiddenOctarock:
	ChildNames = ["リアクション", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class InvisibleKorokRailMove:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "移動"]

	def __init__(self, Name, IsIgnoreNoWaitStopPoint, OnRailDistance, FarDistance, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class IsPlacementAreaEnemy:
	ChildNames = ["禁止", "許可"]

	def __init__(self, Name, CheckType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckType = CheckType
		self.Child0 = Child0
		self.Child1 = Child1


class ItemAmiiboRoot:
	ChildNames = ["ウルフリンク検出", "エポナ対応対象のリンク検出", "ドロップテーブルからアクタ生成"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ItemConductor:
	ChildNames = ["持たれる", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ItemOnTree:
	ChildNames = ["もげる", "通常"]

	def __init__(self, Name, AttOnTree, AttOnGround, FallPowerMin, FallPowerMax, FallOddsMin, FallOddsMax, FallIntervalRange, FallCheckSpeedTh, AtHitImpulseRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttOnTree = AttOnTree
		self.AttOnGround = AttOnGround
		self.FallPowerMin = FallPowerMin
		self.FallPowerMax = FallPowerMax
		self.FallOddsMin = FallOddsMin
		self.FallOddsMax = FallOddsMax
		self.FallIntervalRange = FallIntervalRange
		self.FallCheckSpeedTh = FallCheckSpeedTh
		self.AtHitImpulseRate = AtHitImpulseRate
		self.Child0 = Child0
		self.Child1 = Child1


class ItemRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, AtHitImpulseRate, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtHitImpulseRate = AtHitImpulseRate
		self.Child0 = Child0


class JumpAttack:
	ChildNames = ["攻撃", "攻撃準備"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class JustAvoidFinishWait:
	ChildNames = ["メイン", "待機"]

	def __init__(self, Name, IsUseWaitAfterMain, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseWaitAfterMain = IsUseWaitAfterMain
		self.Child0 = Child0
		self.Child1 = Child1


class KakarikoKokkoTimeline:
	ChildNames = ["Action1", "Action2", "Action3", "Action4", "Idle"]

	def __init__(self, Name, ForceChangeChildKeyName, StartForceChangeFlagName, EndForceChangeFlagName, IntervalToCheckSchedule, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceChangeChildKeyName = ForceChangeChildKeyName
		self.StartForceChangeFlagName = StartForceChangeFlagName
		self.EndForceChangeFlagName = EndForceChangeFlagName
		self.IntervalToCheckSchedule = IntervalToCheckSchedule
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class KeepBackSelect:
	ChildNames = ["角度内", "角度外"]

	def __init__(self, Name, BackAngle, KeepTime, NodeName, BaseAxis, LocalOffset, XZOnly, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BackAngle = BackAngle
		self.KeepTime = KeepTime
		self.NodeName = NodeName
		self.BaseAxis = BaseAxis
		self.LocalOffset = LocalOffset
		self.XZOnly = XZOnly
		self.Child0 = Child0
		self.Child1 = Child1


class KeeseDieSelect:
	ChildNames = ["ぶら下がり死亡", "ショック死", "凍死", "凍特効死", "凍結砕き", "感電死", "死亡", "消滅", "溺死", "濡死", "焼死", "焼特効死", "自然死", "落下死", "被暗殺", "被特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class KeeseHangOnCeil:
	ChildNames = ["張り付き", "待機", "視界気づき", "降下", "音気づき"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class KeeseNormal:
	ChildNames = ["ぶらさがり", "プレイヤー発見", "不審者発見", "不調仲間発見", "天井近づき", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "連携", "音気づき"]

	def __init__(self, Name, RoamHeightFromGlowObj, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RoamHeightFromGlowObj = RoamHeightFromGlowObj
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class KeeseRoam:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, MinOffsetY, MaxOffsetY, RoamRadius, MinMoveDist, MaxMoveDist, NoWaitRatio, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinOffsetY = MinOffsetY
		self.MaxOffsetY = MaxOffsetY
		self.RoamRadius = RoamRadius
		self.MinMoveDist = MinMoveDist
		self.MaxMoveDist = MaxMoveDist
		self.NoWaitRatio = NoWaitRatio
		self.Child0 = Child0
		self.Child1 = Child1


class KeeseSwarmNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class KeeseSwarmRoam:
	ChildNames = ["移動", "近づき", "遠ざかり"]

	def __init__(self, Name, Radius, RadiusMargin, Speed, Direction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.RadiusMargin = RadiusMargin
		self.Speed = Speed
		self.Direction = Direction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class KeyLockedShutter:
	ChildNames = ["オープン", "オープン待機", "クローズ待機", "プリオープン"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class KokkoAngry:
	ChildNames = ["子ノード"]

	def __init__(self, Name, BaseOffset, CreateRandArea, ProhibitedCreateArea, CreateNewActorInterval, CreateContinueTime, CreateBasePosNum, CreateActorName, AfterWaitTime, IsAllowCreateNoSafeArea, IsRotateTargetDir, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseOffset = BaseOffset
		self.CreateRandArea = CreateRandArea
		self.ProhibitedCreateArea = ProhibitedCreateArea
		self.CreateNewActorInterval = CreateNewActorInterval
		self.CreateContinueTime = CreateContinueTime
		self.CreateBasePosNum = CreateBasePosNum
		self.CreateActorName = CreateActorName
		self.AfterWaitTime = AfterWaitTime
		self.IsAllowCreateNoSafeArea = IsAllowCreateNoSafeArea
		self.IsRotateTargetDir = IsRotateTargetDir
		self.Child0 = Child0


class KokkoAngryTargetSelect:
	ChildNames = ["プレイヤー", "敵"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class KokkoEscapeAI:
	ChildNames = ["地形嵌り", "最後の手段", "逃走", "逃走前"]

	def __init__(self, Name, ContinueDistance, ShouldEscapeDistance, ShouldEscapeDistanceRand, PenaltyScale, NavMeshRadiusScale, FramesStuckOnTerrainAction, NumTimesAllowStuck, IsSendGoalPos, IsUseBeforeAction, IsDynamicallyOffsetNavChar, SearchNextPathRadius, RadiusLimit, ForwardDirDistCoefficient, DirRandomMinRatio, DirRangeAngle, RejectDistRatio, ContinueAddSearchAngle, ContinueReduceDistRatio, ContinueReduceRejectDistRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ContinueDistance = ContinueDistance
		self.ShouldEscapeDistance = ShouldEscapeDistance
		self.ShouldEscapeDistanceRand = ShouldEscapeDistanceRand
		self.PenaltyScale = PenaltyScale
		self.NavMeshRadiusScale = NavMeshRadiusScale
		self.FramesStuckOnTerrainAction = FramesStuckOnTerrainAction
		self.NumTimesAllowStuck = NumTimesAllowStuck
		self.IsSendGoalPos = IsSendGoalPos
		self.IsUseBeforeAction = IsUseBeforeAction
		self.IsDynamicallyOffsetNavChar = IsDynamicallyOffsetNavChar
		self.SearchNextPathRadius = SearchNextPathRadius
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomMinRatio = DirRandomMinRatio
		self.DirRangeAngle = DirRangeAngle
		self.RejectDistRatio = RejectDistRatio
		self.ContinueAddSearchAngle = ContinueAddSearchAngle
		self.ContinueReduceDistRatio = ContinueReduceDistRatio
		self.ContinueReduceRejectDistRatio = ContinueReduceRejectDistRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class KokkoRoot:
	ChildNames = ["スクリプト用", "リアクション", "上機嫌", "怒り", "所持", "水中行動", "落下", "通常行動", "騎乗中"]

	def __init__(self, Name, StartSpecialAttackCount, AvoidCountActorName, InWaterDepth, IsCheckFreeFall, IsCheckStuckConsiderY, IsUseWeakForcePushOutside, IsEnableEscapeForceEndCheck, EscapeForceEndTime, AfterEscapeForceEndState, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartSpecialAttackCount = StartSpecialAttackCount
		self.AvoidCountActorName = AvoidCountActorName
		self.InWaterDepth = InWaterDepth
		self.IsCheckFreeFall = IsCheckFreeFall
		self.IsCheckStuckConsiderY = IsCheckStuckConsiderY
		self.IsUseWeakForcePushOutside = IsUseWeakForcePushOutside
		self.IsEnableEscapeForceEndCheck = IsEnableEscapeForceEndCheck
		self.EscapeForceEndTime = EscapeForceEndTime
		self.AfterEscapeForceEndState = AfterEscapeForceEndState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class KorokAnswerResponceRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokFlowerColorRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokFlowerRoot:
	ChildNames = ["コログ花出現", "コログ花待機", "コログ花消滅"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class KorokGoalTimerRootAI:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokPinWheelRoot:

	def __init__(self, Name, RotSpd, Length, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.Length = Length


class KorokPotRootAI:

	def __init__(self, Name, CrayLaunchSpeedRate, CrayLaunchAngularSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CrayLaunchSpeedRate = CrayLaunchSpeedRate
		self.CrayLaunchAngularSpeed = CrayLaunchAngularSpeed


class KorokStartStandRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokStoneLift:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class KorokTargetRailMove:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "完全停止", "移動"]

	def __init__(self, Name, RotSpd, IsIgnoreNoWaitStopPoint, OnRailDistance, FarDistance, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class LOSFurthestHitPointFinder:
	ChildNames = ["行動A", "行動B"]

	def __init__(self, Name, CheckDistance, OnlyCheckBehind, MaxNumCheck, UseActionB, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDistance = CheckDistance
		self.OnlyCheckBehind = OnlyCheckBehind
		self.MaxNumCheck = MaxNumCheck
		self.UseActionB = UseActionB
		self.Child0 = Child0
		self.Child1 = Child1


class LandHumEnemyFindBait:
	ChildNames = ["ジャンプ", "回転", "怒り", "気づき", "疑似餌発見", "直進", "移動", "見まわす", "餌発見"]

	def __init__(self, Name, RepathTime, IsDropWeapon, IsValidForceNeck, WeaponIdx, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RepathTime = RepathTime
		self.IsDropWeapon = IsDropWeapon
		self.IsValidForceNeck = IsValidForceNeck
		self.WeaponIdx = WeaponIdx
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class LandHumEnemyFindBaitWeapon:
	ChildNames = ["喜ぶ", "怪しむ", "拾う", "捨てる", "食べる"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class LandHumEnemyFindPlayer:
	ChildNames = ["ケミカル仲間招来", "ナビメッシュ無し", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "武器ケミカル付与", "武器投げ", "気づき", "速攻"]

	def __init__(self, Name, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, ChemicalSearchDist, NoSearchDist, Voltage, ChemicalActionDist, ThrowWeaponPer, ThrowWeaponDist, NoChemSearchWpIdx, NoBurnWaterDepth, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.ChemicalSearchDist = ChemicalSearchDist
		self.NoSearchDist = NoSearchDist
		self.Voltage = Voltage
		self.ChemicalActionDist = ChemicalActionDist
		self.ThrowWeaponPer = ThrowWeaponPer
		self.ThrowWeaponDist = ThrowWeaponDist
		self.NoChemSearchWpIdx = NoChemSearchWpIdx
		self.NoBurnWaterDepth = NoBurnWaterDepth
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class LandHumEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "危険回避", "待機", "怒り", "攻撃反応", "気配気づき", "浮遊物発見", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, TerrorIgnoreDist, ExplosivesSearchDist, ExplosivesSearchSpeed, ExplosivesSearchAng, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerrorIgnoreDist = TerrorIgnoreDist
		self.ExplosivesSearchDist = ExplosivesSearchDist
		self.ExplosivesSearchSpeed = ExplosivesSearchSpeed
		self.ExplosivesSearchAng = ExplosivesSearchAng
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class LandHumEnemyThrowWeapon:
	ChildNames = ["待機", "怒り", "武器取得", "武器投げ"]

	def __init__(self, Name, WeaponIdx, WaitTimeMax, ThrowWeaponNearDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.WaitTimeMax = WaitTimeMax
		self.ThrowWeaponNearDist = ThrowWeaponNearDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class LandHumEnemyUnarmedBattle:
	ChildNames = ["アイテム発見", "ジャンプ", "危険回避", "回転", "怒り", "戦闘", "武器拾い待ち", "武器発見", "直進", "移動", "見まわす"]

	def __init__(self, Name, EquipItemSearchIdx, SearchBaseWeaponDist, SearchWeaponDist, SearchObjectDist, SearchWeaponTargetDist, SearchBowTargetDist, ItemChaseableSpd, CanGrabHeavy, GrabCheckRadius, AttOffset, RepathTime, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, LostVMin, LostVMax, LostTimer, LostRange, OnCoHitAllowGrabAngle, WeaponIdx, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EquipItemSearchIdx = EquipItemSearchIdx
		self.SearchBaseWeaponDist = SearchBaseWeaponDist
		self.SearchWeaponDist = SearchWeaponDist
		self.SearchObjectDist = SearchObjectDist
		self.SearchWeaponTargetDist = SearchWeaponTargetDist
		self.SearchBowTargetDist = SearchBowTargetDist
		self.ItemChaseableSpd = ItemChaseableSpd
		self.CanGrabHeavy = CanGrabHeavy
		self.GrabCheckRadius = GrabCheckRadius
		self.AttOffset = AttOffset
		self.RepathTime = RepathTime
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.OnCoHitAllowGrabAngle = OnCoHitAllowGrabAngle
		self.WeaponIdx = WeaponIdx
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class LandHumGourmandEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "危険回避", "待機", "怒り", "攻撃反応", "気配気づき", "浮遊物発見", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき", "餌発見"]

	def __init__(self, Name, RefindBaitTime, EatArea, EatNavType, TerrorIgnoreDist, ExplosivesSearchDist, ExplosivesSearchSpeed, ExplosivesSearchAng, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RefindBaitTime = RefindBaitTime
		self.EatArea = EatArea
		self.EatNavType = EatNavType
		self.TerrorIgnoreDist = TerrorIgnoreDist
		self.ExplosivesSearchDist = ExplosivesSearchDist
		self.ExplosivesSearchSpeed = ExplosivesSearchSpeed
		self.ExplosivesSearchAng = ExplosivesSearchAng
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class LandingChemicalBall:
	ChildNames = ["着弾前", "着弾後"]

	def __init__(self, Name, ExpandActorName, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, CheckColConInfo, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExpandActorName = ExpandActorName
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.CheckColConInfo = CheckColConInfo
		self.Child0 = Child0
		self.Child1 = Child1


class LargeCannonAttackRoot:
	ChildNames = ["ビーム攻撃", "攻撃待機"]

	def __init__(self, Name, AttackWaitTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackWaitTime = AttackWaitTime
		self.Child0 = Child0
		self.Child1 = Child1


class LastAttackerSelect:
	ChildNames = ["未発見", "発見"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LastAttackerSpecialActionSelect:
	ChildNames = ["特殊相手", "通常相手"]

	def __init__(self, Name, IsAngerActorSpecial, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAngerActorSpecial = IsAngerActorSpecial
		self.Child0 = Child0
		self.Child1 = Child1


class LastBossBeamAttackRoot:
	ChildNames = ["チャージ", "照準", "発射"]

	def __init__(self, Name, WaitTime, IsMove, KeepDistance, MoveSpeed, InitSpeed, Accel, KeepDistanceRand, RandKeepFrame, BrakeStartFrame, MoveYSpeed, IsChangeable, ReflectOffset, AttackPowerForPlayer, AttackPower, AtMinDamage, IsCreateGuardEffect, AddAttackPower, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.IsMove = IsMove
		self.KeepDistance = KeepDistance
		self.MoveSpeed = MoveSpeed
		self.InitSpeed = InitSpeed
		self.Accel = Accel
		self.KeepDistanceRand = KeepDistanceRand
		self.RandKeepFrame = RandKeepFrame
		self.BrakeStartFrame = BrakeStartFrame
		self.MoveYSpeed = MoveYSpeed
		self.IsChangeable = IsChangeable
		self.ReflectOffset = ReflectOffset
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.AttackPower = AttackPower
		self.AtMinDamage = AtMinDamage
		self.IsCreateGuardEffect = IsCreateGuardEffect
		self.AddAttackPower = AddAttackPower
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossDemoWarpMove:
	ChildNames = ["ワープ消失", "ワープ移動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LastBossDemoWarpRoot:
	ChildNames = ["ワープ", "ワープ前", "ワープ後"]

	def __init__(self, Name, IsPartsActorTgOn, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsPartsActorTgOn = IsPartsActorTgOn
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossNormalWarpRoot:
	ChildNames = ["ワープ", "ワープ前行動", "ワープ後行動"]

	def __init__(self, Name, SleepPartsActorName, IsKeepDisableDraw, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SleepPartsActorName = SleepPartsActorName
		self.IsKeepDisableDraw = IsKeepDisableDraw
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossRailWarpRoot:
	ChildNames = ["ワープ", "ワープ前行動", "ワープ後行動"]

	def __init__(self, Name, SleepPartsActorName, IsKeepDisableDraw, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SleepPartsActorName = SleepPartsActorName
		self.IsKeepDisableDraw = IsKeepDisableDraw
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossRoot:
	ChildNames = ["リアクション", "特殊リアクション", "通常"]

	def __init__(self, Name, ForceRecoverHitMax, ForceRecoverDamageMax, AddForceRecoverHitNum, AddForceRecoverDamage, AuraDemoName, AuraEntryName, AuraWallEntry, AuraHPRate, AuraDemoDownEntry, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceRecoverHitMax = ForceRecoverHitMax
		self.ForceRecoverDamageMax = ForceRecoverDamageMax
		self.AddForceRecoverHitNum = AddForceRecoverHitNum
		self.AddForceRecoverDamage = AddForceRecoverDamage
		self.AuraDemoName = AuraDemoName
		self.AuraEntryName = AuraEntryName
		self.AuraWallEntry = AuraWallEntry
		self.AuraHPRate = AuraHPRate
		self.AuraDemoDownEntry = AuraDemoDownEntry
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossShieldBash:
	ChildNames = ["ジャンプ斬り", "盾突き攻撃"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LastBossShootGaleArrowRoot:
	ChildNames = ["弾発射", "準備", "終了"]

	def __init__(self, Name, ArrowNum, ArrowName, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, BattleNodeOffsetLR, BattleNodeOffsetUD, PartsName, IsPrepreNextArrow, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.ArrowName = ArrowName
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD
		self.PartsName = PartsName
		self.IsPrepreNextArrow = IsPrepreNextArrow
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossShootNormalArrowRoot:
	ChildNames = ["弾発射", "準備", "終了"]

	def __init__(self, Name, ArrowNum, ArrowName, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, BattleNodeOffsetLR, BattleNodeOffsetUD, PartsName, IsPrepreNextArrow, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.ArrowName = ArrowName
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD
		self.PartsName = PartsName
		self.IsPrepreNextArrow = IsPrepreNextArrow
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossSwordWhirlSlash:
	ChildNames = ["攻撃", "溜め", "溜め無し攻撃"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossThunderRoot:
	ChildNames = ["予兆", "削除", "攻撃発生"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LastBossWeaponAttackRoot:
	ChildNames = ["ダメージ反応", "待機", "発見中"]

	def __init__(self, Name, ChaseDist, ChaseDistOffset, IsStartBossBgm, ReappearanceDist, ReappearanceDistOffset, EnemyType, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.IsStartBossBgm = IsStartBossBgm
		self.ReappearanceDist = ReappearanceDist
		self.ReappearanceDistOffset = ReappearanceDistOffset
		self.EnemyType = EnemyType
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LeadToTarget:
	ChildNames = ["待機", "誘導", "誘導(騎乗)"]

	def __init__(self, Name, SuccessRadius, WaitDistance, ResumeLeadDistance, OkPathFailRange, DontWaitIfLeaderIsAhead, WaitFramesAfterArrive, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SuccessRadius = SuccessRadius
		self.WaitDistance = WaitDistance
		self.ResumeLeadDistance = ResumeLeadDistance
		self.OkPathFailRange = OkPathFailRange
		self.DontWaitIfLeaderIsAhead = DontWaitIfLeaderIsAhead
		self.WaitFramesAfterArrive = WaitFramesAfterArrive
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LeaderDistanceSelector:
	ChildNames = ["内側", "外側"]

	def __init__(self, Name, BoundaryDistance, OverlapDistance, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoundaryDistance = BoundaryDistance
		self.OverlapDistance = OverlapDistance
		self.Child0 = Child0
		self.Child1 = Child1


class LeaveFromTarget:
	ChildNames = ["後ずさり", "逃走"]

	def __init__(self, Name, LeaveDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LeaveDist = LeaveDist
		self.Child0 = Child0
		self.Child1 = Child1


class LifeChangeDemoCaller:
	ChildNames = ["行動"]

	def __init__(self, Name, OnlyOnce, DemoName, DemoEntryPoint, LifeRatio, IsIgnorePlayerLand, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnlyOnce = OnlyOnce
		self.DemoName = DemoName
		self.DemoEntryPoint = DemoEntryPoint
		self.LifeRatio = LifeRatio
		self.IsIgnorePlayerLand = IsIgnorePlayerLand
		self.Child0 = Child0


class Lifted:
	ChildNames = ["待機", "所持", "投擲", "設置"]

	def __init__(self, Name, IsGetItem, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsGetItem = IsGetItem
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class LimitedTimeredActorCreator:
	ChildNames = ["待機", "生成"]

	def __init__(self, Name, CreateTimer, CreateTimerRand, CreateActorName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateTimer = CreateTimer
		self.CreateTimerRand = CreateTimerRand
		self.CreateActorName = CreateActorName
		self.Child0 = Child0
		self.Child1 = Child1


class LineCheckTag:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LinkTagCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, IsNotConnectOn, SignalType, SetEnableJobTimerTiming, IsCheckChildEnd, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsNotConnectOn = IsNotConnectOn
		self.SignalType = SignalType
		self.SetEnableJobTimerTiming = SetEnableJobTimerTiming
		self.IsCheckChildEnd = IsCheckChildEnd
		self.Child0 = Child0
		self.Child1 = Child1


class LinkageEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "連携", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class LizalfosBreathAttack:
	ChildNames = ["ブレス攻撃", "疲れる"]

	def __init__(self, Name, MinAttackTimeForTired, MinTiredTime, TiredTimeRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinAttackTimeForTired = MinAttackTimeForTired
		self.MinTiredTime = MinTiredTime
		self.TiredTimeRate = TiredTimeRate
		self.Child0 = Child0
		self.Child1 = Child1


class LumberjackFallenTree:
	ChildNames = ["丸太化", "通常"]

	def __init__(self, Name, ToLogAngVel, MaxCheckAng, CheckDis, IsCheckHeight, CheckHeightRate, TerrorOffsetPos4Falling, TerrorRegistAng, TerrorUnregistTimelimit, NoiseLevel, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ToLogAngVel = ToLogAngVel
		self.MaxCheckAng = MaxCheckAng
		self.CheckDis = CheckDis
		self.IsCheckHeight = IsCheckHeight
		self.CheckHeightRate = CheckHeightRate
		self.TerrorOffsetPos4Falling = TerrorOffsetPos4Falling
		self.TerrorRegistAng = TerrorRegistAng
		self.TerrorUnregistTimelimit = TerrorUnregistTimelimit
		self.NoiseLevel = NoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1


class LumberjackTree:
	ChildNames = ["伐採", "通常"]

	def __init__(self, Name, FallInterval, FellImpRate, FellRotRate, CutOffsetLower, CutOffsetUpper, AlphaLower, AlphaSpeed, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FallInterval = FallInterval
		self.FellImpRate = FellImpRate
		self.FellRotRate = FellRotRate
		self.CutOffsetLower = CutOffsetLower
		self.CutOffsetUpper = CutOffsetUpper
		self.AlphaLower = AlphaLower
		self.AlphaSpeed = AlphaSpeed
		self.Child0 = Child0
		self.Child1 = Child1


class LynelArrowAttackSelect:
	ChildNames = ["上空撃ち", "通常撃ち"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LynelArrowAttackSelectOnce:
	ChildNames = ["上空撃ち", "通常撃ち"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LynelArrowBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, WeaponIdx, AttackCount, FrontCheckBoneName, FrontDirFromBone, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.AttackCount = AttackCount
		self.FrontCheckBoneName = FrontCheckBoneName
		self.FrontDirFromBone = FrontDirFromBone
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class LynelAttackThroughMove:
	ChildNames = ["近づき", "通り過ぎ"]

	def __init__(self, Name, SideOffsetDirType, SideOffset, ThroughDist, CliffFailTime, AcceptableRadius, WeaponIdx, FrontAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SideOffsetDirType = SideOffsetDirType
		self.SideOffset = SideOffset
		self.ThroughDist = ThroughDist
		self.CliffFailTime = CliffFailTime
		self.AcceptableRadius = AcceptableRadius
		self.WeaponIdx = WeaponIdx
		self.FrontAngle = FrontAngle
		self.Child0 = Child0
		self.Child1 = Child1


class LynelBackStepFromTarget:
	ChildNames = ["バックステップ", "後退不能"]

	def __init__(self, Name, MoveDistMin, MoveDist, AddCheckAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveDistMin = MoveDistMin
		self.MoveDist = MoveDist
		self.AddCheckAngle = AddCheckAngle
		self.Child0 = Child0
		self.Child1 = Child1


class LynelBattle:
	ChildNames = ["6足攻撃", "ブレス", "咆哮攻撃", "弓装備", "斬り抜け", "突進切り", "近接戦闘"]

	def __init__(self, Name, CloseBattleStartDist, CloseBattleStartAngle, WeaponIdx, HornAttackRate, RoarRate, BreathStartLifeRate, RoarStartLifeRate, BattleEndDist, RoarFlamePartsKey, BreathPartsKey0, BreathPartsKey1, BreathPartsKey2, CloseBattleRepeatMax, ThroughAttackRepeatNum, SkipBreathRoarRate, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseBattleStartDist = CloseBattleStartDist
		self.CloseBattleStartAngle = CloseBattleStartAngle
		self.WeaponIdx = WeaponIdx
		self.HornAttackRate = HornAttackRate
		self.RoarRate = RoarRate
		self.BreathStartLifeRate = BreathStartLifeRate
		self.RoarStartLifeRate = RoarStartLifeRate
		self.BattleEndDist = BattleEndDist
		self.RoarFlamePartsKey = RoarFlamePartsKey
		self.BreathPartsKey0 = BreathPartsKey0
		self.BreathPartsKey1 = BreathPartsKey1
		self.BreathPartsKey2 = BreathPartsKey2
		self.CloseBattleRepeatMax = CloseBattleRepeatMax
		self.ThroughAttackRepeatNum = ThroughAttackRepeatNum
		self.SkipBreathRoarRate = SkipBreathRoarRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class LynelChaseBattleMove:
	ChildNames = ["近づき", "追跡"]

	def __init__(self, Name, SlowDownDist, SpeedUpDist, BaseDist, OutDist, CloseStartDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlowDownDist = SlowDownDist
		self.SpeedUpDist = SpeedUpDist
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.CloseStartDist = CloseStartDist
		self.Child0 = Child0
		self.Child1 = Child1


class LynelCloseBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, BackAngle, BackAngleAction, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BackAngle = BackAngle
		self.BackAngleAction = BackAngleAction
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class LynelDirSelect:
	ChildNames = ["前", "右", "左", "後"]

	def __init__(self, Name, BasePosOffsetFront, BasePosOffsetBack, FrontAngle, BackAngle, IsCheckOnlyXZ, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BasePosOffsetFront = BasePosOffsetFront
		self.BasePosOffsetBack = BasePosOffsetBack
		self.FrontAngle = FrontAngle
		self.BackAngle = BackAngle
		self.IsCheckOnlyXZ = IsCheckOnlyXZ
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class LynelDistanceLostCheck:
	ChildNames = ["発見行動"]

	def __init__(self, Name, LostTimer, LostRange, AddAwarenessRangeType, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.AddAwarenessRangeType = AddAwarenessRangeType
		self.Child0 = Child0


class LynelEscapeFromTarget:
	ChildNames = ["後退移動", "逃走不能", "逃走移動"]

	def __init__(self, Name, SpaceDistMin, SpaceDist, KeepTime, MoveDistMin, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpaceDistMin = SpaceDistMin
		self.SpaceDist = SpaceDist
		self.KeepTime = KeepTime
		self.MoveDistMin = MoveDistMin
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class LynelLineMoveAttack:
	ChildNames = ["攻撃", "準備"]

	def __init__(self, Name, GoalRadius, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GoalRadius = GoalRadius
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class LynelNavMoveNoStop:
	ChildNames = ["直進", "移動"]

	def __init__(self, Name, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.Child0 = Child0
		self.Child1 = Child1


class LynelNavMoveTarget:
	ChildNames = ["ブレーキ", "回転", "直進", "移動", "見まわす"]

	def __init__(self, Name, StopGear, CliffCheckDist, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopGear = StopGear
		self.CliffCheckDist = CliffCheckDist
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class LynelNormal:
	ChildNames = ["プレイヤー発見", "プレイヤー見失い", "不審者発見", "不調仲間発見", "危険回避", "待機", "怒り", "攻撃反応", "気配気づき", "浮遊物発見", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, TerrorIgnoreDist, ExplosivesSearchDist, ExplosivesSearchSpeed, ExplosivesSearchAng, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerrorIgnoreDist = TerrorIgnoreDist
		self.ExplosivesSearchDist = ExplosivesSearchDist
		self.ExplosivesSearchSpeed = ExplosivesSearchSpeed
		self.ExplosivesSearchAng = ExplosivesSearchAng
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class LynelNoticeAttacked:
	ChildNames = ["強制帰還", "未発見", "発見"]

	def __init__(self, Name, ForceReturnDistFromHomePos, RepeatMax, RepeatResetTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceReturnDistFromHomePos = ForceReturnDistFromHomePos
		self.RepeatMax = RepeatMax
		self.RepeatResetTime = RepeatResetTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelNoticeTerror:
	ChildNames = ["気づき", "眺める", "逃走"]

	def __init__(self, Name, NoWarnDist, WaitTime, NoWarnHeightMin, NoWarnHeightMax, NoTerrorDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoWarnDist = NoWarnDist
		self.WaitTime = WaitTime
		self.NoWarnHeightMin = NoWarnHeightMin
		self.NoWarnHeightMax = NoWarnHeightMax
		self.NoTerrorDist = NoTerrorDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelOnNoNavMeshPos:
	ChildNames = ["ジャンプ", "戦闘", "超ジャンプ"]

	def __init__(self, Name, HeavySlopeAngle, JumpTimer, NoJumpDist, HyperJumpDist, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeavySlopeAngle = HeavySlopeAngle
		self.JumpTimer = JumpTimer
		self.NoJumpDist = NoJumpDist
		self.HyperJumpDist = HyperJumpDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelRecognizeTarget:
	ChildNames = ["帰還", "強制戦闘開始", "戦闘", "戦闘開始", "気づき", "観察", "警戒"]

	def __init__(self, Name, AttensionStartPoint, ObserveEndPoint, DrawnWeaponPoint, WeaponAimPoint, AttackPoint, DashPoint, NearDistance, FarDistance, AppPoint, HorseRidePoint, DamagePoint, TrickedMaskPoint, BombPoint, AimPoint, AimAngle, NearDistPoint, MiddleDistPoint, TiredTime, TiredPoint, ForceBattleStartTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttensionStartPoint = AttensionStartPoint
		self.ObserveEndPoint = ObserveEndPoint
		self.DrawnWeaponPoint = DrawnWeaponPoint
		self.WeaponAimPoint = WeaponAimPoint
		self.AttackPoint = AttackPoint
		self.DashPoint = DashPoint
		self.NearDistance = NearDistance
		self.FarDistance = FarDistance
		self.AppPoint = AppPoint
		self.HorseRidePoint = HorseRidePoint
		self.DamagePoint = DamagePoint
		self.TrickedMaskPoint = TrickedMaskPoint
		self.BombPoint = BombPoint
		self.AimPoint = AimPoint
		self.AimAngle = AimAngle
		self.NearDistPoint = NearDistPoint
		self.MiddleDistPoint = MiddleDistPoint
		self.TiredTime = TiredTime
		self.TiredPoint = TiredPoint
		self.ForceBattleStartTime = ForceBattleStartTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class LynelRepeatAttack:
	ChildNames = ["ラスト", "初撃", "連撃"]

	def __init__(self, Name, AttackNum, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackNum = AttackNum
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelRoam:
	ChildNames = ["回転", "待機", "暇つぶし", "移動", "索敵"]

	def __init__(self, Name, FreeIntervalMin, FreeIntervalMax, FreePer, MoveIntervalMin, MoveIntervalMax, Territory, TargetDistMin, TargetDistMax, NoMoveTime, NoSpAttackMoveTime, SpAttackServiceDist, SpAttackServiceTime, SpAttackServiceAngle, RepathTime, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FreeIntervalMin = FreeIntervalMin
		self.FreeIntervalMax = FreeIntervalMax
		self.FreePer = FreePer
		self.MoveIntervalMin = MoveIntervalMin
		self.MoveIntervalMax = MoveIntervalMax
		self.Territory = Territory
		self.TargetDistMin = TargetDistMin
		self.TargetDistMax = TargetDistMax
		self.NoMoveTime = NoMoveTime
		self.NoSpAttackMoveTime = NoSpAttackMoveTime
		self.SpAttackServiceDist = SpAttackServiceDist
		self.SpAttackServiceTime = SpAttackServiceTime
		self.SpAttackServiceAngle = SpAttackServiceAngle
		self.RepathTime = RepathTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class LynelRodeo:
	ChildNames = ["振り落す", "暴れる"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class LynelRoot:
	ChildNames = ["リアクション", "ロデオ", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, RoarFlameActorName, RoarFlamePartsKey, BreathActorName, BreathPartsKey0, BreathPartsKey1, BreathPartsKey2, StandBoneName, BoneStandAddRatio, StartRotBoostAngle, MaxRotBoostAngle, RotBoostScale, RotBoostScaleGearTop, MoveStraightAngle, FrontCheckStartOffset, SideCheckAngle, FrontCheckNavRadius, FrontCheckDist, BowIdx, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RoarFlameActorName = RoarFlameActorName
		self.RoarFlamePartsKey = RoarFlamePartsKey
		self.BreathActorName = BreathActorName
		self.BreathPartsKey0 = BreathPartsKey0
		self.BreathPartsKey1 = BreathPartsKey1
		self.BreathPartsKey2 = BreathPartsKey2
		self.StandBoneName = StandBoneName
		self.BoneStandAddRatio = BoneStandAddRatio
		self.StartRotBoostAngle = StartRotBoostAngle
		self.MaxRotBoostAngle = MaxRotBoostAngle
		self.RotBoostScale = RotBoostScale
		self.RotBoostScaleGearTop = RotBoostScaleGearTop
		self.MoveStraightAngle = MoveStraightAngle
		self.FrontCheckStartOffset = FrontCheckStartOffset
		self.SideCheckAngle = SideCheckAngle
		self.FrontCheckNavRadius = FrontCheckNavRadius
		self.FrontCheckDist = FrontCheckDist
		self.BowIdx = BowIdx
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class LynelTackleMove:
	ChildNames = ["近づき", "通り過ぎ"]

	def __init__(self, Name, ThroughDist, CloseEndAngle, CloseEndDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThroughDist = ThroughDist
		self.CloseEndAngle = CloseEndAngle
		self.CloseEndDist = CloseEndDist
		self.Child0 = Child0
		self.Child1 = Child1


class LynelThreeBreathAttack:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, NearRange, FarRange, IsCheckXZ, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearRange = NearRange
		self.FarRange = FarRange
		self.IsCheckXZ = IsCheckXZ
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class LynelWarp:
	ChildNames = ["ワープ", "出現", "消失"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MagneGearRoot:
	ChildNames = ["はめ込まれた", "マグネ捕まり中", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MagneGrabSelect:
	ChildNames = ["掴まれ", "離れ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MagneGrabbedPartsRangeSelector:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, PartsName, IsSelectEveryFrame, FarDist, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class MagneShaftRoot:
	ChildNames = ["はめ込まれた", "通常"]

	def __init__(self, Name, DefaultConnectionDistance, CollideRadiusFactor, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DefaultConnectionDistance = DefaultConnectionDistance
		self.CollideRadiusFactor = CollideRadiusFactor
		self.Child0 = Child0
		self.Child1 = Child1


class MagneSliderBlockRootThunder:
	ChildNames = ["はめ込まれた", "通常"]

	def __init__(self, Name, DefaultConnectionDistance, CollideRadiusFactor, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DefaultConnectionDistance = DefaultConnectionDistance
		self.CollideRadiusFactor = CollideRadiusFactor
		self.Child0 = Child0
		self.Child1 = Child1


class MagneStickRoot:
	ChildNames = ["はめ込まれた", "通常"]

	def __init__(self, Name, DefaultConnectionDistance, CollideRadiusFactor, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DefaultConnectionDistance = DefaultConnectionDistance
		self.CollideRadiusFactor = CollideRadiusFactor
		self.Child0 = Child0
		self.Child1 = Child1


class Magnetglove:
	ChildNames = ["マグネフォース発生", "所持", "消滅"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MainFieldDungeonSelect:
	ChildNames = ["その他", "水の遺物", "火の遺物", "電気の遺物", "風の遺物"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class MasquaradeSubTargetSelect:
	ChildNames = ["マスクだった", "マスクではなかった"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MasterSwordBase100EnemyRoot:
	ChildNames = ["アテンションなし待機", "待機", "起動"]

	def __init__(self, Name, KillAttentionWaitFrame, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KillAttentionWaitFrame = KillAttentionWaitFrame
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MasterSwordRoot:
	ChildNames = ["Fixed配置", "マスターソードチャレンジ", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class MergedDungeonPartsRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class MessageReceiveCheck:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, MsgType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MsgType = MsgType
		self.Child0 = Child0
		self.Child1 = Child1


class MessageReceiveCheckBasic:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MessageReceiveCheckEveryFrame:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, MsgType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MsgType = MsgType
		self.Child0 = Child0
		self.Child1 = Child1


class MetalObjectBuried:
	ChildNames = ["地上", "地中"]

	def __init__(self, Name, PullOutSpeed, IsIgnoreResistanceArea, CheckGroundRadiusScale, IsCheckGrabYPosFix, IsCheckSelfY, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PullOutSpeed = PullOutSpeed
		self.IsIgnoreResistanceArea = IsIgnoreResistanceArea
		self.CheckGroundRadiusScale = CheckGroundRadiusScale
		self.IsCheckGrabYPosFix = IsCheckGrabYPosFix
		self.IsCheckSelfY = IsCheckSelfY
		self.Child0 = Child0
		self.Child1 = Child1


class MetalObjectFixed:
	ChildNames = ["固定中", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MimicCliffStopEnemyNormal:
	ChildNames = ["待機", "擬態解除", "気づき", "音気づき"]

	def __init__(self, Name, JumpDistXZ, NoticeSoundTime, OffsetHand, OffsetTail, OffsetHandRotBase, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpDistXZ = JumpDistXZ
		self.NoticeSoundTime = NoticeSoundTime
		self.OffsetHand = OffsetHand
		self.OffsetTail = OffsetTail
		self.OffsetHandRotBase = OffsetHandRotBase
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class MimicEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, PlayerForceFindDist, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerForceFindDist = PlayerForceFindDist
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class MimicEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "擬態解除", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, PlayerForceFindDist, RideHorseMaskPlayerFindDist, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerForceFindDist = PlayerForceFindDist
		self.RideHorseMaskPlayerFindDist = RideHorseMaskPlayerFindDist
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class MimicFlagSelect:
	ChildNames = ["擬態", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MimicryResetCheck:
	ChildNames = ["行動"]

	def __init__(self, Name, ResetRate, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ResetRate = ResetRate
		self.Child0 = Child0


class MiniGolemLifted:
	ChildNames = ["所持", "投擲", "着地", "落下", "設置"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class MiniGolemReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class MiniGolemRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "逆さま", "逆さまリアクション", "通常", "騎乗"]

	def __init__(self, Name, LiftDeadTime, UpperArmL_PartsKey, LowerArmL_PartsKey, UpperArmR_PartsKey, LowerArmR_PartsKey, ChemicalFieldKey, BodyDeactiveAS, ArmRDeactiveAS, ArmLDeactiveAS, BodyActiveAS, ArmRActiveAS, ArmLActiveAS, BodyMimicAS, ArmRMimicAS, ArmLMimicAS, ShaderASTargetBone, BodyShaderSeqBank, ArmRShaderSeqBank, ArmLShaderSeqBank, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LiftDeadTime = LiftDeadTime
		self.UpperArmL_PartsKey = UpperArmL_PartsKey
		self.LowerArmL_PartsKey = LowerArmL_PartsKey
		self.UpperArmR_PartsKey = UpperArmR_PartsKey
		self.LowerArmR_PartsKey = LowerArmR_PartsKey
		self.ChemicalFieldKey = ChemicalFieldKey
		self.BodyDeactiveAS = BodyDeactiveAS
		self.ArmRDeactiveAS = ArmRDeactiveAS
		self.ArmLDeactiveAS = ArmLDeactiveAS
		self.BodyActiveAS = BodyActiveAS
		self.ArmRActiveAS = ArmRActiveAS
		self.ArmLActiveAS = ArmLActiveAS
		self.BodyMimicAS = BodyMimicAS
		self.ArmRMimicAS = ArmRMimicAS
		self.ArmLMimicAS = ArmLMimicAS
		self.ShaderASTargetBone = ShaderASTargetBone
		self.BodyShaderSeqBank = BodyShaderSeqBank
		self.ArmRShaderSeqBank = ArmRShaderSeqBank
		self.ArmLShaderSeqBank = ArmLShaderSeqBank
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class MiniGolemSleep:
	ChildNames = ["待機", "横になる", "睡眠", "起き上がる"]

	def __init__(self, Name, IsAwakenByHearing, IsWaitAfterAwaken, AwakeDelayTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAwakenByHearing = IsAwakenByHearing
		self.IsWaitAfterAwaken = IsWaitAfterAwaken
		self.AwakeDelayTime = AwakeDelayTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class MoonAI:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class MoonNameTag:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class MoriblinSpearBattle:
	ChildNames = ["中距離", "強制小攻撃", "待機", "近距離"]

	def __init__(self, Name, FarDist, OutDist, NearDist, BaseDist, WeaponIdx, AttackStartRotate, ForceAttackDist, AttackIntervalIntensity, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.OutDist = OutDist
		self.NearDist = NearDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.AttackStartRotate = AttackStartRotate
		self.ForceAttackDist = ForceAttackDist
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class MoriblinSpearNearBattle:
	ChildNames = ["バックステップ", "大攻撃", "後退"]

	def __init__(self, Name, BackWalkPer, BackStepPer, NearDist, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BackWalkPer = BackWalkPer
		self.BackStepPer = BackStepPer
		self.NearDist = NearDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MoriblinUnarmedBattle:
	ChildNames = ["待機", "攻撃", "追撃ち攻撃"]

	def __init__(self, Name, FarDist, OutDist, BaseDist, WeaponIdx, AttackStartRotate, PursuingAttackInterval, PursuingAttackStartAng, AttackIntervalIntensity, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.OutDist = OutDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.AttackStartRotate = AttackStartRotate
		self.PursuingAttackInterval = PursuingAttackInterval
		self.PursuingAttackStartAng = PursuingAttackStartAng
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MotorcycleRoot:
	ChildNames = ["NPC騎乗", "プレイヤー騎乗", "出現", "敵騎乗", "消失", "転倒", "騎乗無し"]

	def __init__(self, Name, InWaterRateForDisappear, DistanceToPlayerForDisappear, CloseSaddleFramesSincePut, FinishCookFramesSincePut, AdditionalFramesForFairy, NoiseEnergyEmpty, NoiseNotRidden, NoiseThrottleClose, NoiseThrottleOpen, ForestFogRatioForDisappear, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterRateForDisappear = InWaterRateForDisappear
		self.DistanceToPlayerForDisappear = DistanceToPlayerForDisappear
		self.CloseSaddleFramesSincePut = CloseSaddleFramesSincePut
		self.FinishCookFramesSincePut = FinishCookFramesSincePut
		self.AdditionalFramesForFairy = AdditionalFramesForFairy
		self.NoiseEnergyEmpty = NoiseEnergyEmpty
		self.NoiseNotRidden = NoiseNotRidden
		self.NoiseThrottleClose = NoiseThrottleClose
		self.NoiseThrottleOpen = NoiseThrottleOpen
		self.ForestFogRatioForDisappear = ForestFogRatioForDisappear
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class MoveAndFreeFallGondola:
	ChildNames = ["停止", "停止点移動", "移動"]

	def __init__(self, Name, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MoveAroundTarget:
	ChildNames = ["移動"]

	def __init__(self, Name, StartRange, EndRange, ChangeRangeRate, TurnTimeBase, TurnTimeRand, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartRange = StartRange
		self.EndRange = EndRange
		self.ChangeRangeRate = ChangeRangeRate
		self.TurnTimeBase = TurnTimeBase
		self.TurnTimeRand = TurnTimeRand
		self.Child0 = Child0


class MoveLOSFeedback:
	ChildNames = ["移動", "衝突"]

	def __init__(self, Name, FramesCooldownFeedback, LOSCheckLength, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FramesCooldownFeedback = FramesCooldownFeedback
		self.LOSCheckLength = LOSCheckLength
		self.Child0 = Child0
		self.Child1 = Child1


class MoveRemainsElectric:
	ChildNames = ["一時停止", "停止", "再稼働", "移動"]

	def __init__(self, Name, ReactiveRange, DemoCallWaitTime, CannonOffset, WeakPointOffset, ReactivateTime, FrontCheckMinDist, FrontDirUpdateInterval, SpeedScale, InitPosByRailRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactiveRange = ReactiveRange
		self.DemoCallWaitTime = DemoCallWaitTime
		self.CannonOffset = CannonOffset
		self.WeakPointOffset = WeakPointOffset
		self.ReactivateTime = ReactivateTime
		self.FrontCheckMinDist = FrontCheckMinDist
		self.FrontDirUpdateInterval = FrontDirUpdateInterval
		self.SpeedScale = SpeedScale
		self.InitPosByRailRatio = InitPosByRailRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class MoveToCameraFrontXZ:
	ChildNames = ["プレイヤー回避移動", "反転", "移動"]

	def __init__(self, Name, DistFromPlayer, MinDistFromPlayer, ReverseTimer, ReverseCount, AvoidPlayerDist, AddLineCheckNavRadius, IsSuccessByLineReachable, ReachableRadius, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistFromPlayer = DistFromPlayer
		self.MinDistFromPlayer = MinDistFromPlayer
		self.ReverseTimer = ReverseTimer
		self.ReverseCount = ReverseCount
		self.AvoidPlayerDist = AvoidPlayerDist
		self.AddLineCheckNavRadius = AddLineCheckNavRadius
		self.IsSuccessByLineReachable = IsSuccessByLineReachable
		self.ReachableRadius = ReachableRadius
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class MoveToTargetCollisionFeedback:
	ChildNames = ["移動"]

	def __init__(self, Name, UseMoveAwayFromPos, CooldownFramesTargetAdjust, RetryOriginalPos, FramesUntilRetryOriginalPos, IsAdjustDepthOnCollision, IdealDepthMin, IdealDepthMax, IgnoreYComponentThreshold, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseMoveAwayFromPos = UseMoveAwayFromPos
		self.CooldownFramesTargetAdjust = CooldownFramesTargetAdjust
		self.RetryOriginalPos = RetryOriginalPos
		self.FramesUntilRetryOriginalPos = FramesUntilRetryOriginalPos
		self.IsAdjustDepthOnCollision = IsAdjustDepthOnCollision
		self.IdealDepthMin = IdealDepthMin
		self.IdealDepthMax = IdealDepthMax
		self.IgnoreYComponentThreshold = IgnoreYComponentThreshold
		self.Child0 = Child0


class NPCAlert:
	ChildNames = ["ひるむ", "反応する", "振り向く", "気付く", "警戒"]

	def __init__(self, Name, MinReactionTime, ReleaseDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinReactionTime = MinReactionTime
		self.ReleaseDist = ReleaseDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class NPCArtistRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCAttack:
	ChildNames = ["ガード", "勝利", "待機", "後退", "接近", "攻撃", "移動"]

	def __init__(self, Name, ActionBaseTime, ActionTimePlay, ActionRate, AttackRate, AttackModeTime, GuardModeTime, EnemyChanceTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActionBaseTime = ActionBaseTime
		self.ActionTimePlay = ActionTimePlay
		self.ActionRate = ActionRate
		self.AttackRate = AttackRate
		self.AttackModeTime = AttackModeTime
		self.GuardModeTime = GuardModeTime
		self.EnemyChanceTime = EnemyChanceTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class NPCAttentionAI:
	ChildNames = ["振り向く", "注目"]

	def __init__(self, Name, ReleaseDistance, DurationTime, IsUseSight, TurnAngleDiff, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReleaseDistance = ReleaseDistance
		self.DurationTime = DurationTime
		self.IsUseSight = IsUseSight
		self.TurnAngleDiff = TurnAngleDiff
		self.Child0 = Child0
		self.Child1 = Child1


class NPCAvoid:
	ChildNames = ["アラート", "屈む", "泳いで逃げる", "浮き上がる", "潜る", "立ち上がる", "納刀", "脅威解除", "逃走"]

	def __init__(self, Name, TargetTerrorLevel, ReleaseCrouchTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetTerrorLevel = TargetTerrorLevel
		self.ReleaseCrouchTime = ReleaseCrouchTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class NPCChasePlayerBlueFire:
	ChildNames = ["Wander", "接近待機", "見失い", "追跡"]

	def __init__(self, Name, NearDist, LeaveDist, LostDist, LostTimer, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDist = NearDist
		self.LeaveDist = LeaveDist
		self.LostDist = LostDist
		self.LostTimer = LostTimer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NPCClerkRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCConfront:
	ChildNames = ["アラート", "ガード", "反応する", "反撃", "抜刀", "振り向く", "気付く", "納刀", "警戒"]

	def __init__(self, Name, ReleaseDistance, ReleaseTime, CounterGuardCount, CounterRate, DirectTurnAngle, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReleaseDistance = ReleaseDistance
		self.ReleaseTime = ReleaseTime
		self.CounterGuardCount = CounterGuardCount
		self.CounterRate = CounterRate
		self.DirectTurnAngle = DirectTurnAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class NPCConfrontEnemy:
	ChildNames = ["お礼", "アラート", "一時待機", "戦闘", "抜刀", "気絶", "気絶前振り向き", "立ち上がる", "納刀", "退く"]

	def __init__(self, Name, ReleaseDistance, ReleaseTime, RewardDistance, TerrorDistAfterPlayerRescue, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReleaseDistance = ReleaseDistance
		self.ReleaseTime = ReleaseTime
		self.RewardDistance = RewardDistance
		self.TerrorDistAfterPlayerRescue = TerrorDistAfterPlayerRescue
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class NPCGerudoQueenRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCHeartsRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCHorseRide:
	ChildNames = ["乗る", "待機", "雨宿り中", "雨宿り地点に移動"]

	def __init__(self, Name, GearLevel, GearResetPathNum, PlayerNearDistance, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GearLevel = GearLevel
		self.GearResetPathNum = GearResetPathNum
		self.PlayerNearDistance = PlayerNearDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NPCHorseRideWait:
	ChildNames = ["到着", "移動"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NPCMamonoShopRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCMove:
	ChildNames = ["うろつく", "アンカー接近", "ベッドから起きる", "一時停止", "何もしない", "到着", "振り返る", "減速", "移動", "起きる", "身体を起こす", "近傍移動", "遷移待機", "雨宿り地点に到着", "雨宿り地点に移動"]

	def __init__(self, Name, Destination, TerritoryRange, MoveEndASName, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Destination = Destination
		self.TerritoryRange = TerritoryRange
		self.MoveEndASName = MoveEndASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14


class NPCMoveToRailPoint:
	ChildNames = ["アンカー接近", "振り向く", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NPCReaction:
	ChildNames = ["よろける", "吹き出し", "注視する"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NPCReturnAnchor:
	ChildNames = ["到着", "姿勢変更", "振り向く"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NPCReturnRestPosRoot:
	ChildNames = ["Move", "Turn"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NPCRoam:
	ChildNames = ["待機", "減速", "移動"]

	def __init__(self, Name, Radius, WaitFrame, WaitFrameRand, WalkDistMin, WalkDistMax, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.WalkDistMin = WalkDistMin
		self.WalkDistMax = WalkDistMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NPCRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NPCRunaway:
	ChildNames = ["お礼", "待機", "救出待ち", "気絶", "気絶前振り向き", "立ち上がる", "起き上がる", "追い詰められる", "逃走", "驚く"]

	def __init__(self, Name, ReleaseDistance, CorneredDistance, StandRateTime, StandingTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReleaseDistance = ReleaseDistance
		self.CorneredDistance = CorneredDistance
		self.StandRateTime = StandRateTime
		self.StandingTime = StandingTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class NPCSearch:
	ChildNames = ["プレイヤー発見", "音気づき"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NPCSurprised:
	ChildNames = ["納刀", "驚く"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NPCSuspend:
	ChildNames = ["停止", "移動"]

	def __init__(self, Name, WaitTime, EndMoveTime, SearchRadius, RetryCount, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.EndMoveTime = EndMoveTime
		self.SearchRadius = SearchRadius
		self.RetryCount = RetryCount
		self.Child0 = Child0
		self.Child1 = Child1


class NPCTalkBalloon:
	ChildNames = ["振り向く", "注目"]

	def __init__(self, Name, DurationTime, DelayFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DurationTime = DurationTime
		self.DelayFrame = DelayFrame
		self.Child0 = Child0
		self.Child1 = Child1


class NPCTerrorAI:
	ChildNames = ["全力逃走", "敵遭遇", "身構える", "逃走", "驚く"]

	def __init__(self, Name, TerrorEndTime, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerrorEndTime = TerrorEndTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class NPCTimeline:
	ChildNames = ["Action1", "Action10", "Action2", "Action3", "Action4", "Action5", "Action6", "Action7", "Action8", "Action9", "Idle", "Meeting", "Sleep", "Sleep2", "Wander", "Wander2"]

	def __init__(self, Name, IntervalToCheckSchedule, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IntervalToCheckSchedule = IntervalToCheckSchedule
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class NPCTravel:
	ChildNames = ["一時停止", "何もしない", "待機", "急いで指定位置に移動", "指定フレーム待機", "指定位置に移動", "振り返る", "減速", "雨宿り中", "雨宿り地点に移動", "馬を待つ"]

	def __init__(self, Name, WaitHorseReturnDist, GiveUpWaitHorseTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitHorseReturnDist = WaitHorseReturnDist
		self.GiveUpWaitHorseTime = GiveUpWaitHorseTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class NPCTravelerRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Rest", "ReturnRestPos", "Ride", "Search", "Terror", "Timeline"]

	def __init__(self, Name, IsRiderChangableAction, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsRiderChangableAction = IsRiderChangableAction
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class NPCWander:
	ChildNames = ["アンカー接近", "ベッドから起きる", "レール点に移動", "一時停止", "何もしない", "待機", "指定フレーム待機", "振り向く", "減速", "移動", "起きる", "身体を起こす", "雨宿り", "雨宿り地点に移動"]

	def __init__(self, Name, RainDestination, RainWaitTime, NormalASKeyName, RainASKeyName, GoalDistance, RailUpdateDistRate, RailUniqueName, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RainDestination = RainDestination
		self.RainWaitTime = RainWaitTime
		self.NormalASKeyName = NormalASKeyName
		self.RainASKeyName = RainASKeyName
		self.GoalDistance = GoalDistance
		self.RailUpdateDistRate = RailUpdateDistRate
		self.RailUniqueName = RailUniqueName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class NavMeshTurnAwayFromHitPos:
	ChildNames = ["回転", "移動"]

	def __init__(self, Name, MoveToSafePosAfterTurn, LOSCheckLength, NumLOSCheckMax, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveToSafePosAfterTurn = MoveToSafePosAfterTurn
		self.LOSCheckLength = LOSCheckLength
		self.NumLOSCheckMax = NumLOSCheckMax
		self.Child0 = Child0
		self.Child1 = Child1


class NavMoveNearTarget:
	ChildNames = ["ジャンプ", "直進", "移動", "見まわす"]

	def __init__(self, Name, TargetVMax, TargetVMin, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, UseCharacterRadius, VibrateCheckTime, RotVibrateCheckTime, IsLastLineReachCheck, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetVMax = TargetVMax
		self.TargetVMin = TargetVMin
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.UseCharacterRadius = UseCharacterRadius
		self.VibrateCheckTime = VibrateCheckTime
		self.RotVibrateCheckTime = RotVibrateCheckTime
		self.IsLastLineReachCheck = IsLastLineReachCheck
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NavMoveTarget:
	ChildNames = ["ジャンプ", "直進", "移動", "見まわす"]

	def __init__(self, Name, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, UseCharacterRadius, VibrateCheckTime, RotVibrateCheckTime, IsLastLineReachCheck, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.UseCharacterRadius = UseCharacterRadius
		self.VibrateCheckTime = VibrateCheckTime
		self.RotVibrateCheckTime = RotVibrateCheckTime
		self.IsLastLineReachCheck = IsLastLineReachCheck
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NavMoveTargetClosestPoint:
	ChildNames = ["ジャンプ", "直進", "移動", "見まわす"]

	def __init__(self, Name, SearchRadius, TargetVMax, TargetVMin, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, UseCharacterRadius, VibrateCheckTime, RotVibrateCheckTime, IsLastLineReachCheck, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchRadius = SearchRadius
		self.TargetVMax = TargetVMax
		self.TargetVMin = TargetVMin
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.UseCharacterRadius = UseCharacterRadius
		self.VibrateCheckTime = VibrateCheckTime
		self.RotVibrateCheckTime = RotVibrateCheckTime
		self.IsLastLineReachCheck = IsLastLineReachCheck
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NavMoveTargetWithJumpWater:
	ChildNames = ["ジャンプ", "直進", "移動", "見まわす"]

	def __init__(self, Name, JumpDist, InWaterDepth, WaterCheckDist, IsCheckDamage, ReachTargetArea, RepathTime, WeaponIdx, TooFarDist, UseCharacterRadius, VibrateCheckTime, RotVibrateCheckTime, IsLastLineReachCheck, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpDist = JumpDist
		self.InWaterDepth = InWaterDepth
		self.WaterCheckDist = WaterCheckDist
		self.IsCheckDamage = IsCheckDamage
		self.ReachTargetArea = ReachTargetArea
		self.RepathTime = RepathTime
		self.WeaponIdx = WeaponIdx
		self.TooFarDist = TooFarDist
		self.UseCharacterRadius = UseCharacterRadius
		self.VibrateCheckTime = VibrateCheckTime
		self.RotVibrateCheckTime = RotVibrateCheckTime
		self.IsLastLineReachCheck = IsLastLineReachCheck
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class NavViewMove:
	ChildNames = ["回転", "移動"]

	def __init__(self, Name, SubsAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubsAngle = SubsAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class NearCreateAppearTypeSelect:
	ChildNames = ["空中", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NearCreateSelect:
	ChildNames = ["近接湧き", "通常湧き"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NewMannequinRoot:
	ChildNames = ["装備あり", "装備なし"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class NormalHumanEquipableShield:
	ChildNames = ["盾装備不能", "盾装備可能"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class NoticePartsRangeSelector:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, PartsName, IsSelectEveryFrame, FarDist, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class NpcDemoRoot:
	ChildNames = ["アンカーへ移動", "アンカー到着状態に遷移", "レール点に移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NpcMoveToAnchor:
	ChildNames = ["アンカー接近", "振り向く", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class NpcTebaRoot:
	ChildNames = ["プレイヤーに接近", "飛行"]

	def __init__(self, Name, ApproachPlayerHeight, ShowMessageDoDist, ShowMessageLockonMinInterval, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ApproachPlayerHeight = ApproachPlayerHeight
		self.ShowMessageDoDist = ShowMessageDoDist
		self.ShowMessageLockonMinInterval = ShowMessageLockonMinInterval
		self.Child0 = Child0
		self.Child1 = Child1


class NpcTebaTrainingRoot:
	ChildNames = ["DemoOnly", "EventStartWait", "Reaction", "Search", "Terror", "Timeline"]

	def __init__(self, Name, PlayerHitVelocity, ReleaseInterest2Time, StaggerUpperASName, StaggerUpperRunASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerHitVelocity = PlayerHitVelocity
		self.ReleaseInterest2Time = ReleaseInterest2Time
		self.StaggerUpperASName = StaggerUpperASName
		self.StaggerUpperRunASName = StaggerUpperRunASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class NushiEscapeSelector:
	ChildNames = ["ワープ", "消滅"]

	def __init__(self, Name, NumOfAllowedEscapes, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NumOfAllowedEscapes = NumOfAllowedEscapes
		self.Child0 = Child0
		self.Child1 = Child1


class NushiWarp:
	ChildNames = ["ワープ"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class OctarockBattle:
	ChildNames = ["吐き出し攻撃", "戦闘攻撃", "戦闘準備", "画面外吐き出し攻撃", "画面外攻撃"]

	def __init__(self, Name, ShootActorKey, VacuumPartsKey, IsAttackOnlyOutScreen, ActorDisplayRadius, IsHideMode, AttackDistMin, IsFirstAttackIntervalZero, IsLostAttack, OutScreenDist, OutScreenAttackNum, OutScrnAtkOffset, OutScrnAtkOffsetY, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootActorKey = ShootActorKey
		self.VacuumPartsKey = VacuumPartsKey
		self.IsAttackOnlyOutScreen = IsAttackOnlyOutScreen
		self.ActorDisplayRadius = ActorDisplayRadius
		self.IsHideMode = IsHideMode
		self.AttackDistMin = AttackDistMin
		self.IsFirstAttackIntervalZero = IsFirstAttackIntervalZero
		self.IsLostAttack = IsLostAttack
		self.OutScreenDist = OutScreenDist
		self.OutScreenAttackNum = OutScreenAttackNum
		self.OutScrnAtkOffset = OutScrnAtkOffset
		self.OutScrnAtkOffsetY = OutScrnAtkOffsetY
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class OctarockHideEscape:
	ChildNames = ["移動", "隠れる", "飛び出す"]

	def __init__(self, Name, EscapeDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EscapeDist = EscapeDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class OctarockOptionRoot:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, IsBreakable, IsMimicry, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsBreakable = IsBreakable
		self.IsMimicry = IsMimicry
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class OctarockReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, IsWigBreackByGust, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsWigBreackByGust = IsWigBreackByGust
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class OctarockRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, ItemName, ConnectRigidBodyName, ConnectTgtBodyName, ShootActorName, ShootActorKey1, ShootActorKey2, ShootActorKey3, IsWigBreakable, ExtraShootActorName, ExtraShootActorKey, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ItemName = ItemName
		self.ConnectRigidBodyName = ConnectRigidBodyName
		self.ConnectTgtBodyName = ConnectTgtBodyName
		self.ShootActorName = ShootActorName
		self.ShootActorKey1 = ShootActorKey1
		self.ShootActorKey2 = ShootActorKey2
		self.ShootActorKey3 = ShootActorKey3
		self.IsWigBreakable = IsWigBreakable
		self.ExtraShootActorName = ExtraShootActorName
		self.ExtraShootActorKey = ExtraShootActorKey
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class OctarockServiceHideWait:
	ChildNames = ["出現待機", "待機", "気づき", "隠れる", "飛び出す"]

	def __init__(self, Name, SafeAreaDist, SafeAreaDistRange, MinWaitTime, MinWaitTimeRand, NoticeTerrorLevel, NoticeWorryRange, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SafeAreaDist = SafeAreaDist
		self.SafeAreaDistRange = SafeAreaDistRange
		self.MinWaitTime = MinWaitTime
		self.MinWaitTimeRand = MinWaitTimeRand
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.NoticeWorryRange = NoticeWorryRange
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class OctarockWaterWait:
	ChildNames = ["カツラ反応", "プレイヤー気づき", "待機", "浮上", "浮遊", "浮遊終了", "落下", "音気づき"]

	def __init__(self, Name, NoRiseTime, RiseDelayTimeMin, RiseDelayTimeMax, FinishFloatDelayTimeMin, FinishFloatDelayTimeMax, MinHeightFromWater, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoRiseTime = NoRiseTime
		self.RiseDelayTimeMin = RiseDelayTimeMin
		self.RiseDelayTimeMax = RiseDelayTimeMax
		self.FinishFloatDelayTimeMin = FinishFloatDelayTimeMin
		self.FinishFloatDelayTimeMax = FinishFloatDelayTimeMax
		self.MinHeightFromWater = MinHeightFromWater
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class OnCliffEnemyBattle:
	ChildNames = ["攻撃", "追跡"]

	def __init__(self, Name, AttackDist, AttackAngleH, AttackAngleVMax, AttackAngleVMin, LostCounter, AttackIntervalIntensity, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackDist = AttackDist
		self.AttackAngleH = AttackAngleH
		self.AttackAngleVMax = AttackAngleVMax
		self.AttackAngleVMin = AttackAngleVMin
		self.LostCounter = LostCounter
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1


class OnCliffSurfaceSelect:
	ChildNames = ["初期化待機", "壁張り付き", "解凍後", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class OnCliffViewWait:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class OnEnterEventModeSelect:
	ChildNames = ["デモ中", "非デモ中"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class OnNavFaceSelect:
	ChildNames = ["ナビメッシュ有り", "ナビメッシュ無し"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class OnRagdollSelect:
	ChildNames = ["ラグドール中", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class OneMemoryMagicBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "魔法攻撃"]

	def __init__(self, Name, MemoryPartsName, MagicName, AttackRatio, BreathSize, EnlargeTime, MagicPer, AttackPowDirect, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MemoryPartsName = MemoryPartsName
		self.MagicName = MagicName
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.MagicPer = MagicPer
		self.AttackPowDirect = AttackPowDirect
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class OptionalWeaponAI:
	ChildNames = ["装備", "非装備"]

	def __init__(self, Name, BindNodeName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BindNodeName = BindNodeName
		self.Child0 = Child0
		self.Child1 = Child1


class OutOfScreen:
	ChildNames = ["移動"]

	def __init__(self, Name, UpdateInterval, TagetDistance, DeleteDistance, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpdateInterval = UpdateInterval
		self.TagetDistance = TagetDistance
		self.DeleteDistance = DeleteDistance
		self.Child0 = Child0


class PartHaveSelect:
	ChildNames = ["パーツ有", "パーツ無"]

	def __init__(self, Name, PartsKey, IsCheckEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey = PartsKey
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class PartsNoticeSelect:
	ChildNames = ["パーツ気づき", "パーツ通常"]

	def __init__(self, Name, PartsName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.Child0 = Child0
		self.Child1 = Child1


class PartsSleepSelect:
	ChildNames = ["寝てる", "起きてる"]

	def __init__(self, Name, PartsName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.Child0 = Child0
		self.Child1 = Child1


class PauseMenuPlayerRoot:
	ChildNames = ["アイテム使用", "抱え持ち増加", "通常待機"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PickShootItemRoot:
	ChildNames = ["待機", "所持", "落下"]

	def __init__(self, Name, RemainTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RemainTime = RemainTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PillarCrack:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PipeDrawing:
	ChildNames = ["待機", "鳴らす"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerAttack:
	ChildNames = ["ふいうち", "ガード攻撃", "ジャスト後攻撃", "ダッシュ攻撃", "回転斬り", "大剣回転斬り", "小攻撃", "跳ね返り"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class PlayerBarrierBlow:
	ChildNames = ["ラグドール", "吹き飛び"]

	def __init__(self, Name, BlowRagdollTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlowRagdollTime = BlowRagdollTime
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerBeetle:
	ChildNames = ["ビートル操作", "構え"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerCamera:
	ChildNames = ["自撮り", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerCaught:
	ChildNames = ["掴まれる"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PlayerClimb:
	ChildNames = ["壁登り", "梯子", "武器ペグ"]

	def __init__(self, Name, NoClimbTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoClimbTime = NoClimbTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PlayerCutJump:
	ChildNames = ["ジャンプ斬り", "落下斬り"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerDead:
	ChildNames = ["バリア吹き飛び", "中ダメージ", "凍る", "大ダメージ", "小ダメージ", "復活待ち", "打ち上げ", "死亡デモ開始", "水の遺物咆哮吹き飛び", "痺れる"]

	def __init__(self, Name, RumbleType, RumblePower, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RumbleType = RumbleType
		self.RumblePower = RumblePower
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class PlayerDemoRoot:
	ChildNames = ["目的地に移動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PlayerGrab:
	ChildNames = ["しゃがみ", "待機", "投げ", "持上げ", "準備", "直前で停止", "立ち上がり", "置き", "風の加護ジャンプ溜め"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class PlayerItem:
	ChildNames = ["ビートル", "マグネットグローブ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerLadder:
	ChildNames = ["ジャンプ", "ジャンプ着地", "下り始め", "下り終わり", "壁登り", "梯子から壁登り", "登り始め", "登り終わり", "移動", "落下"]

	def __init__(self, Name, LadderToClimbTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LadderToClimbTime = LadderToClimbTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class PlayerNavDestinationMove:
	ChildNames = ["直進", "移動", "適当移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PlayerNormal:
	ChildNames = ["2段ジャンプ", "しゃがみステップ", "しゃがみダメージ", "しゃがみ待機", "しゃがみ移動", "アイテム", "イベント開始待ち", "ウェイクボード", "カメラ", "ガードスリップ", "ガード崩れ", "コッコ滑空", "サイドステップ", "サイドステップ着地", "シーカーストーンを見る待機", "ジャンプ", "ジャンプ斬り", "スイッチぶら下がり", "ステップガードジャスト", "ステップ攻撃", "スーパージャンプ", "スーパージャンプ溜め", "ゾーラに掴まる", "ドアを引いて開ける", "ドアを押して開ける", "バク転", "バク転着地", "バリア吹き飛び", "パラショール滑空", "中ダメージ", "凍り解除", "凍る", "坂滑り", "坂滑り着地", "壁ジャンプ", "壁滑り", "壁登り", "壁駆け上がり", "大ダメージ", "大ダメージ起き上がり", "奈落", "奈落開始待ち", "寝る", "小ダメージ", "小段差よじ登り壁つかみ", "座る", "弓主観", "待機", "怯む", "打ち上げ", "拾う", "持上げ", "掴まれる", "操作", "攻撃", "木登り", "梯子", "武器投げ", "死亡", "段差登り", "水の遺物咆哮吹き飛び", "水中へ飛び込みジャンプ", "注目待機", "注目移動", "泳ぎ", "泳ぎダメージ", "溺れる", "滑落", "滝登り", "痺れる", "盾サーフィン", "着地", "着地ダメージ", "着地後攻撃", "移動", "空中停止", "素材をとる", "落下", "落下ガードジャスト", "落下中の弓", "装備解除", "跳ね返り", "飛び込み着地", "飾る待機", "馬上ジャンプ", "馬上ジャンプ攻撃", "馬上ジャンプ攻撃着地", "馬乗りジャンプ", "騎乗"]

	def __init__(self, Name, EquipNoiseValue, AttackNoiseValue, ArrowReadyNoiseValue, ParashawlInvalidHeight, ParashawlInvalidHeightSurfing, ForceSlipSpeed, DoForbidTime, NoRideJumpDiffY, DashUpEnableSpeed, EnergyPerChargeLv, EnergyChargeStart, WallSlipEnableSpeed, CutAddSpeedRate, CutAddSpeedMax, CutAddSpeedDec, HorseCallTime, SwordSearchAngle, DoClimbForbidTime, DoClimbForbidAngVel, InWaterTimeForRagdoll, ToFallHeightForJustRush, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Child19, Child20, Child21, Child22, Child23, Child24, Child25, Child26, Child27, Child28, Child29, Child30, Child31, Child32, Child33, Child34, Child35, Child36, Child37, Child38, Child39, Child40, Child41, Child42, Child43, Child44, Child45, Child46, Child47, Child48, Child49, Child50, Child51, Child52, Child53, Child54, Child55, Child56, Child57, Child58, Child59, Child60, Child61, Child62, Child63, Child64, Child65, Child66, Child67, Child68, Child69, Child70, Child71, Child72, Child73, Child74, Child75, Child76, Child77, Child78, Child79, Child80, Child81, Child82, Child83, Child84, Child85, Child86, Child87, Child88, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EquipNoiseValue = EquipNoiseValue
		self.AttackNoiseValue = AttackNoiseValue
		self.ArrowReadyNoiseValue = ArrowReadyNoiseValue
		self.ParashawlInvalidHeight = ParashawlInvalidHeight
		self.ParashawlInvalidHeightSurfing = ParashawlInvalidHeightSurfing
		self.ForceSlipSpeed = ForceSlipSpeed
		self.DoForbidTime = DoForbidTime
		self.NoRideJumpDiffY = NoRideJumpDiffY
		self.DashUpEnableSpeed = DashUpEnableSpeed
		self.EnergyPerChargeLv = EnergyPerChargeLv
		self.EnergyChargeStart = EnergyChargeStart
		self.WallSlipEnableSpeed = WallSlipEnableSpeed
		self.CutAddSpeedRate = CutAddSpeedRate
		self.CutAddSpeedMax = CutAddSpeedMax
		self.CutAddSpeedDec = CutAddSpeedDec
		self.HorseCallTime = HorseCallTime
		self.SwordSearchAngle = SwordSearchAngle
		self.DoClimbForbidTime = DoClimbForbidTime
		self.DoClimbForbidAngVel = DoClimbForbidAngVel
		self.InWaterTimeForRagdoll = InWaterTimeForRagdoll
		self.ToFallHeightForJustRush = ToFallHeightForJustRush
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18
		self.Child19 = Child19
		self.Child20 = Child20
		self.Child21 = Child21
		self.Child22 = Child22
		self.Child23 = Child23
		self.Child24 = Child24
		self.Child25 = Child25
		self.Child26 = Child26
		self.Child27 = Child27
		self.Child28 = Child28
		self.Child29 = Child29
		self.Child30 = Child30
		self.Child31 = Child31
		self.Child32 = Child32
		self.Child33 = Child33
		self.Child34 = Child34
		self.Child35 = Child35
		self.Child36 = Child36
		self.Child37 = Child37
		self.Child38 = Child38
		self.Child39 = Child39
		self.Child40 = Child40
		self.Child41 = Child41
		self.Child42 = Child42
		self.Child43 = Child43
		self.Child44 = Child44
		self.Child45 = Child45
		self.Child46 = Child46
		self.Child47 = Child47
		self.Child48 = Child48
		self.Child49 = Child49
		self.Child50 = Child50
		self.Child51 = Child51
		self.Child52 = Child52
		self.Child53 = Child53
		self.Child54 = Child54
		self.Child55 = Child55
		self.Child56 = Child56
		self.Child57 = Child57
		self.Child58 = Child58
		self.Child59 = Child59
		self.Child60 = Child60
		self.Child61 = Child61
		self.Child62 = Child62
		self.Child63 = Child63
		self.Child64 = Child64
		self.Child65 = Child65
		self.Child66 = Child66
		self.Child67 = Child67
		self.Child68 = Child68
		self.Child69 = Child69
		self.Child70 = Child70
		self.Child71 = Child71
		self.Child72 = Child72
		self.Child73 = Child73
		self.Child74 = Child74
		self.Child75 = Child75
		self.Child76 = Child76
		self.Child77 = Child77
		self.Child78 = Child78
		self.Child79 = Child79
		self.Child80 = Child80
		self.Child81 = Child81
		self.Child82 = Child82
		self.Child83 = Child83
		self.Child84 = Child84
		self.Child85 = Child85
		self.Child86 = Child86
		self.Child87 = Child87
		self.Child88 = Child88


class PlayerRideHorse:
	ChildNames = ["イベント開始待ち", "降りる", "騎乗"]

	def __init__(self, Name, DoForbidTime, ThrowPowerY, ThrowPowerF, BackDismountSpeed, WaistAngleApplyRateFoward, WaistAngleApplyRateBack, MoveNoise, SwordAttackNoise, AimAngleAddApplyAngle, AimAngleAdd, AimAngleAddApplySpeed, LowerAngleWaitTime, LynelRodeoCutNum, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DoForbidTime = DoForbidTime
		self.ThrowPowerY = ThrowPowerY
		self.ThrowPowerF = ThrowPowerF
		self.BackDismountSpeed = BackDismountSpeed
		self.WaistAngleApplyRateFoward = WaistAngleApplyRateFoward
		self.WaistAngleApplyRateBack = WaistAngleApplyRateBack
		self.MoveNoise = MoveNoise
		self.SwordAttackNoise = SwordAttackNoise
		self.AimAngleAddApplyAngle = AimAngleAddApplyAngle
		self.AimAngleAdd = AimAngleAdd
		self.AimAngleAddApplySpeed = AimAngleAddApplySpeed
		self.LowerAngleWaitTime = LowerAngleWaitTime
		self.LynelRodeoCutNum = LynelRodeoCutNum
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PlayerRoot:
	ChildNames = ["ForDemo", "Normal"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PlayerSetTarget:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PlayerSit:
	ChildNames = ["待機", "終了", "開始"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PlayerSwim:
	ChildNames = ["よじ登り上り開始初期化", "スピンアタック", "前転", "小段差よじ登り壁つかみ", "梯子", "段差登り", "泳ぎから上陸", "泳ぎジャンプ", "泳ぎダッシュ", "泳ぎダメージ", "泳ぎ待機", "泳ぎ移動"]

	def __init__(self, Name, CatchHeightL, CatchHeightH, EnableHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CatchHeightL = CatchHeightL
		self.CatchHeightH = CatchHeightH
		self.EnableHeight = EnableHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class PlayerWaterFall:
	ChildNames = ["ジャンプ", "ゾーラ跳ね上げ", "潜水移動", "登り"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PlayerZoraRide:
	ChildNames = ["マグネ", "乗り"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PointWindTagRoot:
	ChildNames = ["Dummy"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PracticeGuardianMiniNormal:
	ChildNames = ["回避の試練Ｈ", "回避の試練Ｖ", "盾はじきの試練", "集中の試練"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PreSleepCheck:
	ChildNames = ["回転", "睡眠"]

	def __init__(self, Name, CheckDist, CheckRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.CheckRadius = CheckRadius
		self.Child0 = Child0
		self.Child1 = Child1


class PrevASEndSeq:
	ChildNames = ["終了", "行動"]

	def __init__(self, Name, PrevASName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PrevASName = PrevASName
		self.Child0 = Child0
		self.Child1 = Child1


class PrevASOR2SelectTwo:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, AS1, AS2, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS1 = AS1
		self.AS2 = AS2
		self.Child0 = Child0
		self.Child1 = Child1


class PrevASSelect:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, ASName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Child0 = Child0
		self.Child1 = Child1


class PrevASSkipSeq:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, PrevASName, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PrevASName = PrevASName
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class PrevSomeASSelect:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, ASName0, ASName1, ASName2, ASName3, ASName4, ASName5, SeqBank, TargetBone, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName0 = ASName0
		self.ASName1 = ASName1
		self.ASName2 = ASName2
		self.ASName3 = ASName3
		self.ASName4 = ASName4
		self.ASName5 = ASName5
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.Child0 = Child0
		self.Child1 = Child1


class PreyChemicalDeadReaction:
	ChildNames = ["凍死", "感電死", "死亡", "焼死"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PreyDead:
	ChildNames = ["倒れ中", "停止"]

	def __init__(self, Name, IsEmitForceEscapeSignal, SendRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.SendRadius = SendRadius
		self.Child0 = Child0
		self.Child1 = Child1


class PreyDeadCauseSelector:
	ChildNames = ["落下", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PreyDefWanderAI:
	ChildNames = ["地形嵌り", "待機", "最後の手段", "移動"]

	def __init__(self, Name, FramesStuckLimit, TimesStuckLimit, ChangeWaitRate, MaxWaitTime, MinWaitTime, FinishChangeCount, CheckWaitIsChangable, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FramesStuckLimit = FramesStuckLimit
		self.TimesStuckLimit = TimesStuckLimit
		self.ChangeWaitRate = ChangeWaitRate
		self.MaxWaitTime = MaxWaitTime
		self.MinWaitTime = MinWaitTime
		self.FinishChangeCount = FinishChangeCount
		self.CheckWaitIsChangable = CheckWaitIsChangable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PreyDropItemRoot:
	ChildNames = ["スクリプト用", "リアクション", "上機嫌", "強制消去", "所持", "水中行動", "落下", "通常行動", "騎乗中"]

	def __init__(self, Name, InitialVelocity, MaxDropCount, ForceDeleteInterval, InWaterDepth, IsCheckFreeFall, IsCheckStuckConsiderY, IsUseWeakForcePushOutside, IsEnableEscapeForceEndCheck, EscapeForceEndTime, AfterEscapeForceEndState, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitialVelocity = InitialVelocity
		self.MaxDropCount = MaxDropCount
		self.ForceDeleteInterval = ForceDeleteInterval
		self.InWaterDepth = InWaterDepth
		self.IsCheckFreeFall = IsCheckFreeFall
		self.IsCheckStuckConsiderY = IsCheckStuckConsiderY
		self.IsUseWeakForcePushOutside = IsUseWeakForcePushOutside
		self.IsEnableEscapeForceEndCheck = IsEnableEscapeForceEndCheck
		self.EscapeForceEndTime = EscapeForceEndTime
		self.AfterEscapeForceEndState = AfterEscapeForceEndState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class PreyLookAtTarget:
	ChildNames = ["ふり向き", "警戒", "連続ふり向き"]

	def __init__(self, Name, LimitAngle, IsUpdateViewPos, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitAngle = LimitAngle
		self.IsUpdateViewPos = IsUpdateViewPos
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PreyNormal:
	ChildNames = ["ふり向き", "ターゲット通知", "ダメージ逃走", "ロケーター待機", "威嚇", "徘徊", "戦闘", "気づき", "注目", "興味対象発見", "逃走"]

	def __init__(self, Name, IsUseEscapeState, IsPositiveAttacker, IsSearchTarget, IsEmitForceEscapeSignal, IsReceivedForceEscapeSignal, IsCheckSandStorm, ChangeBattleStateRadius, CounterAttackRadius, CounterAttackRate, AddCautionLevelVal, AutoReduceCautionLevelVal, LimitOverReduceCautionLevelVal, AwnRangeScaleWhenAttention, TargetLostTime, AllowRoarRadius, EscapeWaterFlowLimit, NewFoodAddTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseEscapeState = IsUseEscapeState
		self.IsPositiveAttacker = IsPositiveAttacker
		self.IsSearchTarget = IsSearchTarget
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.IsReceivedForceEscapeSignal = IsReceivedForceEscapeSignal
		self.IsCheckSandStorm = IsCheckSandStorm
		self.ChangeBattleStateRadius = ChangeBattleStateRadius
		self.CounterAttackRadius = CounterAttackRadius
		self.CounterAttackRate = CounterAttackRate
		self.AddCautionLevelVal = AddCautionLevelVal
		self.AutoReduceCautionLevelVal = AutoReduceCautionLevelVal
		self.LimitOverReduceCautionLevelVal = LimitOverReduceCautionLevelVal
		self.AwnRangeScaleWhenAttention = AwnRangeScaleWhenAttention
		self.TargetLostTime = TargetLostTime
		self.AllowRoarRadius = AllowRoarRadius
		self.EscapeWaterFlowLimit = EscapeWaterFlowLimit
		self.NewFoodAddTime = NewFoodAddTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class PreyReaction:
	ChildNames = ["ダメージ", "凍結", "怨念", "死亡", "気絶", "消滅", "溶岩", "炎上", "痺れ"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class PreyRoot:
	ChildNames = ["スクリプト用", "リアクション", "上機嫌", "所持", "水中行動", "落下", "通常行動", "騎乗中"]

	def __init__(self, Name, InWaterDepth, IsCheckFreeFall, IsCheckStuckConsiderY, IsUseWeakForcePushOutside, IsEnableEscapeForceEndCheck, EscapeForceEndTime, AfterEscapeForceEndState, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.IsCheckFreeFall = IsCheckFreeFall
		self.IsCheckStuckConsiderY = IsCheckStuckConsiderY
		self.IsUseWeakForcePushOutside = IsUseWeakForcePushOutside
		self.IsEnableEscapeForceEndCheck = IsEnableEscapeForceEndCheck
		self.EscapeForceEndTime = EscapeForceEndTime
		self.AfterEscapeForceEndState = AfterEscapeForceEndState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class PreyStun:
	ChildNames = ["復帰", "気絶中"]

	def __init__(self, Name, StunTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StunTime = StunTime
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossActorCloneRoot:
	ChildNames = ["シンクロモード", "バナナモード", "攻撃変更の間", "通常モード"]

	def __init__(self, Name, DisappearXLinkEventKey, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisappearXLinkEventKey = DisappearXLinkEventKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossActorEnemyRoot:
	ChildNames = ["フェイズ終了", "フェイズ開始", "リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, IsReactionOnDead, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReactionOnDead = IsReactionOnDead
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class PriestBossActorGiantFouthRoot:
	ChildNames = ["例外待機", "分身投げ", "地形回転", "大土遁", "待機", "歩き", "目ビーム", "踏みつけ", "転移", "鉄球投げ"]

	def __init__(self, Name, StompAction, StompDistance, StompAlwaysChange, StompInAreaTimer, IsFreeMoving, FreqIronBallAttack, FreqBigEarthReleaseAttack, FreqEyeBeamAttack, FreqStageRotation, FloatDistFromPlayer, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StompAction = StompAction
		self.StompDistance = StompDistance
		self.StompAlwaysChange = StompAlwaysChange
		self.StompInAreaTimer = StompInAreaTimer
		self.IsFreeMoving = IsFreeMoving
		self.FreqIronBallAttack = FreqIronBallAttack
		self.FreqBigEarthReleaseAttack = FreqBigEarthReleaseAttack
		self.FreqEyeBeamAttack = FreqEyeBeamAttack
		self.FreqStageRotation = FreqStageRotation
		self.FloatDistFromPlayer = FloatDistFromPlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class PriestBossActorGiantRoot:
	ChildNames = ["例外待機", "分身投げ", "地形回転", "大土遁", "待機", "歩き", "目ビーム", "踏みつけ", "転移", "鉄球投げ"]

	def __init__(self, Name, IsFreeMoving, FreqIronBallAttack, FreqBigEarthReleaseAttack, FreqEyeBeamAttack, FreqStageRotation, FloatDistFromPlayer, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFreeMoving = IsFreeMoving
		self.FreqIronBallAttack = FreqIronBallAttack
		self.FreqBigEarthReleaseAttack = FreqBigEarthReleaseAttack
		self.FreqEyeBeamAttack = FreqEyeBeamAttack
		self.FreqStageRotation = FreqStageRotation
		self.FloatDistFromPlayer = FloatDistFromPlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class PriestBossActorNormalMode:
	ChildNames = ["分身", "分身投げ着地", "土遁", "弓矢攻撃", "待機", "準備", "移動", "突進攻撃", "転移", "離れる", "頭上突き", "高速移動攻撃"]

	def __init__(self, Name, IsManagedBtlMgr, ApproachStartDistance, ApproachWarpRate, LeaveStartDistance, LeaveStartTime, WaitMinTime, WaitMaxTime, SecondHalfLifePercent, FramesRestrictEarthRelease, WarpPosDistFromPlayer, StageMarginRateForEarthRelease, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsManagedBtlMgr = IsManagedBtlMgr
		self.ApproachStartDistance = ApproachStartDistance
		self.ApproachWarpRate = ApproachWarpRate
		self.LeaveStartDistance = LeaveStartDistance
		self.LeaveStartTime = LeaveStartTime
		self.WaitMinTime = WaitMinTime
		self.WaitMaxTime = WaitMaxTime
		self.SecondHalfLifePercent = SecondHalfLifePercent
		self.FramesRestrictEarthRelease = FramesRestrictEarthRelease
		self.WarpPosDistFromPlayer = WarpPosDistFromPlayer
		self.StageMarginRateForEarthRelease = StageMarginRateForEarthRelease
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class PriestBossActorNormalRoot:
	ChildNames = ["シンクロモード", "バナナモード", "攻撃変更の間", "通常モード"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossActorPhaseSecondStart:
	ChildNames = ["共通"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PriestBossAfterImageRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class PriestBossAttackGrave:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossBananaMode:
	ChildNames = ["バナナ夢中", "解除"]

	def __init__(self, Name, HealAmount, TimeUpFrames, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HealAmount = HealAmount
		self.TimeUpFrames = TimeUpFrames
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossBeamExplode:
	ChildNames = ["後処理", "爆発", "着弾前"]

	def __init__(self, Name, MaxDistanceChangeableBorder, MaxDistanceChangeableRevise, MaxDistance, IsDelete, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistanceChangeableBorder = MaxDistanceChangeableBorder
		self.MaxDistanceChangeableRevise = MaxDistanceChangeableRevise
		self.MaxDistance = MaxDistance
		self.IsDelete = IsDelete
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossBlowoffDamageSelect:
	ChildNames = ["リアクション準備", "接地ふらつき", "接地ダウン", "浮遊ふらつき", "浮遊ダウン"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class PriestBossBlowoffReadyReaction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PriestBossBowEquiped:
	ChildNames = ["射撃", "装備"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossCircleFormationRush:
	ChildNames = ["分身消す", "待機", "攻撃", "攻撃前", "攻撃後", "陣形作成_消える", "陣形作成_現れる", "陣形作成後待機"]

	def __init__(self, Name, HomingAttackTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HomingAttackTime = HomingAttackTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class PriestBossCircleFormationShoot:
	ChildNames = ["分身消す", "待機", "攻撃", "攻撃前", "攻撃後", "陣形作成_消える", "陣形作成_現れる", "陣形作成後待機"]

	def __init__(self, Name, HomingAttackTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HomingAttackTime = HomingAttackTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class PriestBossCloneBananaMode:
	ChildNames = ["バナナ夢中", "解除"]

	def __init__(self, Name, HealAmount, TimeUpFrames, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HealAmount = HealAmount
		self.TimeUpFrames = TimeUpFrames
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossCloneBulletRoot:
	ChildNames = ["受信", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossDamageTypeSelect:
	ChildNames = ["該当", "非該当"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossEyeBeamFourth:
	ChildNames = ["チャージ", "待機", "照準", "発射", "索敵", "速攻照準"]

	def __init__(self, Name, AtDirType, AtAttr, AtType, AtShieldBreakPower, AtImpact, AtPowerReduce, AtPower, AtDamage, SearchEndAngle, IsCreateGuardEffect, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, IsChangeable, ShotOffset, ShotReviseAngleXU, ShotReviseAngleXD, ShotReviseAngleY, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtDirType = AtDirType
		self.AtAttr = AtAttr
		self.AtType = AtType
		self.AtShieldBreakPower = AtShieldBreakPower
		self.AtImpact = AtImpact
		self.AtPowerReduce = AtPowerReduce
		self.AtPower = AtPower
		self.AtDamage = AtDamage
		self.SearchEndAngle = SearchEndAngle
		self.IsCreateGuardEffect = IsCreateGuardEffect
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.IsChangeable = IsChangeable
		self.ShotOffset = ShotOffset
		self.ShotReviseAngleXU = ShotReviseAngleXU
		self.ShotReviseAngleXD = ShotReviseAngleXD
		self.ShotReviseAngleY = ShotReviseAngleY
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class PriestBossEyeBeamStandAim:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, BorderDist, BorderHeight, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BorderDist = BorderDist
		self.BorderHeight = BorderHeight
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossEyeBeamThird:
	ChildNames = ["チャージ", "待機", "照準", "発射"]

	def __init__(self, Name, IsCreateGuardEffect, AtMinDamage, AttackPower, AttackPowerForPlayer, ReflectOffset, IsChangeable, ShotOffset, ShotReviseAngleXU, ShotReviseAngleXD, ShotReviseAngleY, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCreateGuardEffect = IsCreateGuardEffect
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.ReflectOffset = ReflectOffset
		self.IsChangeable = IsChangeable
		self.ShotOffset = ShotOffset
		self.ShotReviseAngleXU = ShotReviseAngleXU
		self.ShotReviseAngleXD = ShotReviseAngleXD
		self.ShotReviseAngleY = ShotReviseAngleY
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossFastWarpAttack:
	ChildNames = ["スロー時移動", "移動", "移動開始"]

	def __init__(self, Name, KeepDistance, MoveWidth, IsCloseMove, BaseOffsetY, PredictMoveFrame, IsPlayRunStartAS, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepDistance = KeepDistance
		self.MoveWidth = MoveWidth
		self.IsCloseMove = IsCloseMove
		self.BaseOffsetY = BaseOffsetY
		self.PredictMoveFrame = PredictMoveFrame
		self.IsPlayRunStartAS = IsPlayRunStartAS
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossGiantDeadSelector:
	ChildNames = ["ダウン状態", "立ち状態"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossGiantDownSeq:
	ChildNames = ["ダウン", "復帰", "空中", "落下"]

	def __init__(self, Name, RecoverIfAlreadyDown, IsUseRecover, HitGroundASName, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RecoverIfAlreadyDown = RecoverIfAlreadyDown
		self.IsUseRecover = IsUseRecover
		self.HitGroundASName = HitGroundASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossGiantEnemyRoot:
	ChildNames = ["フェイズ終了", "フェイズ開始", "リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, InvalidateIronBallDamageFrame, IsReactionOnDead, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InvalidateIronBallDamageFrame = InvalidateIronBallDamageFrame
		self.IsReactionOnDead = IsReactionOnDead
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class PriestBossGiantReaction:
	ChildNames = ["ふっとび", "ウルボザの怒り", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16


class PriestBossGiantStageRotRoot:
	ChildNames = ["ロール前", "地形をロール", "地形を戻す", "鉄球投げ"]

	def __init__(self, Name, CentralAngle, PercentRadiusHeight, IronBallHeightOffset, ArcPercent, ZOffset, ZOffsetIndex, HoldBallsCounterLength, BallsReleaseIntervalFrames, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CentralAngle = CentralAngle
		self.PercentRadiusHeight = PercentRadiusHeight
		self.IronBallHeightOffset = IronBallHeightOffset
		self.ArcPercent = ArcPercent
		self.ZOffset = ZOffset
		self.ZOffsetIndex = ZOffsetIndex
		self.HoldBallsCounterLength = HoldBallsCounterLength
		self.BallsReleaseIntervalFrames = BallsReleaseIntervalFrames
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossGiantStageRotate:
	ChildNames = ["回転終了待機", "開始"]

	def __init__(self, Name, SendCommand, SendOnThrowASEvent, IsUseStartAction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SendCommand = SendCommand
		self.SendOnThrowASEvent = SendOnThrowASEvent
		self.IsUseStartAction = IsUseStartAction
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossIAIAttack:
	ChildNames = ["斬り付け", "駆け寄り"]

	def __init__(self, Name, OffsetLR, WeaponIdx, CloseDistLR, ClsoeDistFB, TiredAngle, IsAbleSkipNear, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetLR = OffsetLR
		self.WeaponIdx = WeaponIdx
		self.CloseDistLR = CloseDistLR
		self.ClsoeDistFB = ClsoeDistFB
		self.TiredAngle = TiredAngle
		self.IsAbleSkipNear = IsAbleSkipNear
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossIronBall:
	ChildNames = ["攻撃", "攻撃後", "攻撃終了", "準備完了待ち"]

	def __init__(self, Name, IronBallWaitThunderTime, IronBallOffsetY, IronBallRadius, IronBallAngle, IronSummonLeftBoneName, IronSummonRightBoneName, IsAfterAttack, IronBallAngleOffset, ChangeEndAnime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallWaitThunderTime = IronBallWaitThunderTime
		self.IronBallOffsetY = IronBallOffsetY
		self.IronBallRadius = IronBallRadius
		self.IronBallAngle = IronBallAngle
		self.IronSummonLeftBoneName = IronSummonLeftBoneName
		self.IronSummonRightBoneName = IronSummonRightBoneName
		self.IsAfterAttack = IsAfterAttack
		self.IronBallAngleOffset = IronBallAngleOffset
		self.ChangeEndAnime = ChangeEndAnime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossIronBallRoot:
	ChildNames = ["待機", "念受信", "落雷"]

	def __init__(self, Name, AttackPower, AttackPowerForPlayer, AtMinDamage, MagneLightningTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPower = AttackPower
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.AtMinDamage = AtMinDamage
		self.MagneLightningTime = MagneLightningTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossIronBallStageRotate:
	ChildNames = ["攻撃", "攻撃後", "攻撃終了", "準備完了待ち"]

	def __init__(self, Name, IronBallSummonRadius, IronBallSummonArchAngle, IronBallSummonOffsetY, IronBallWaitThunderTime, IronBallOffsetY, IronBallRadius, IronBallAngle, IronSummonLeftBoneName, IronSummonRightBoneName, IsAfterAttack, IronBallAngleOffset, ChangeEndAnime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallSummonRadius = IronBallSummonRadius
		self.IronBallSummonArchAngle = IronBallSummonArchAngle
		self.IronBallSummonOffsetY = IronBallSummonOffsetY
		self.IronBallWaitThunderTime = IronBallWaitThunderTime
		self.IronBallOffsetY = IronBallOffsetY
		self.IronBallRadius = IronBallRadius
		self.IronBallAngle = IronBallAngle
		self.IronSummonLeftBoneName = IronSummonLeftBoneName
		self.IronSummonRightBoneName = IronSummonRightBoneName
		self.IsAfterAttack = IsAfterAttack
		self.IronBallAngleOffset = IronBallAngleOffset
		self.ChangeEndAnime = ChangeEndAnime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossLineFormationAppear:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossLineFormationFall:
	ChildNames = ["分身消す", "待機", "攻撃", "攻撃前", "攻撃後", "陣形作成_消える", "陣形作成_現れる"]

	def __init__(self, Name, WarpHightOffset, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpHightOffset = WarpHightOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class PriestBossLineFormationRush:
	ChildNames = ["分身消す", "待機", "攻撃", "攻撃前", "攻撃後", "突進後駆け抜け", "陣形作成_消える", "陣形作成_現れる"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class PriestBossMakeClone:
	ChildNames = ["分身", "後行動", "振り向く", "転移", "離れる"]

	def __init__(self, Name, RespawnFrame, BackStepDistance, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RespawnFrame = RespawnFrame
		self.BackStepDistance = BackStepDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class PriestBossMetaAIRoot:
	ChildNames = ["段階_分身", "段階_巨大化", "段階_祭り", "段階_終了", "段階_通常"]

	def __init__(self, Name, Life, BowActorName, ArrowActorName, WeaponActorName, ThunderActorName, PlayerRecoverFromFallFrames, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Life = Life
		self.BowActorName = BowActorName
		self.ArrowActorName = ArrowActorName
		self.WeaponActorName = WeaponActorName
		self.ThunderActorName = ThunderActorName
		self.PlayerRecoverFromFallFrames = PlayerRecoverFromFallFrames
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class PriestBossNormalMoveSelector:
	ChildNames = ["旋回", "直進"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossNormalQuickRecover:
	ChildNames = ["ダウンから復帰", "ラグドールから復帰"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossNormalReaction:
	ChildNames = ["ふっとび", "ウルボザの怒り", "ガード", "ガードブレイク", "クイック復帰", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, IsUseQuickRecover, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseQuickRecover = IsUseQuickRecover
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17


class PriestBossPhaseFinish:

	def __init__(self, Name, StartDemoDelayFrames, PercentLifeTransition, PercentLifePrevious, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartDemoDelayFrames = StartDemoDelayFrames
		self.PercentLifeTransition = PercentLifeTransition
		self.PercentLifePrevious = PercentLifePrevious


class PriestBossPhaseFirst:

	def __init__(self, Name, PercentLifeTransition, PercentLifePrevious, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PercentLifeTransition = PercentLifeTransition
		self.PercentLifePrevious = PercentLifePrevious


class PriestBossPhaseFourth:

	def __init__(self, Name, RespawnSpan, SimAtkMax, BowEquipMax, PercentLifeTransition, PercentLifePrevious, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RespawnSpan = RespawnSpan
		self.SimAtkMax = SimAtkMax
		self.BowEquipMax = BowEquipMax
		self.PercentLifeTransition = PercentLifeTransition
		self.PercentLifePrevious = PercentLifePrevious


class PriestBossPhaseSecond:

	def __init__(self, Name, ModeChangeLife, ModeChangeBlockTime, RespawnSpan, RespawnBaseSpace, RespawnBaseMoveTime, RespawnBaseInterval, SimAtkMax, BowEquipMax, SyncAtkMax, CircleFormRange, CircleFormRushWait, CircleFormRushInterval, CircleFormShootWait, CircleFormShootInterval, LineFormDistFromPlayer, LineFormSpace, LineFormRushWait, LineFormRushInterval, LineFormFallWait, LineFormFallInterval, PercentLifeTransition, PercentLifePrevious, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ModeChangeLife = ModeChangeLife
		self.ModeChangeBlockTime = ModeChangeBlockTime
		self.RespawnSpan = RespawnSpan
		self.RespawnBaseSpace = RespawnBaseSpace
		self.RespawnBaseMoveTime = RespawnBaseMoveTime
		self.RespawnBaseInterval = RespawnBaseInterval
		self.SimAtkMax = SimAtkMax
		self.BowEquipMax = BowEquipMax
		self.SyncAtkMax = SyncAtkMax
		self.CircleFormRange = CircleFormRange
		self.CircleFormRushWait = CircleFormRushWait
		self.CircleFormRushInterval = CircleFormRushInterval
		self.CircleFormShootWait = CircleFormShootWait
		self.CircleFormShootInterval = CircleFormShootInterval
		self.LineFormDistFromPlayer = LineFormDistFromPlayer
		self.LineFormSpace = LineFormSpace
		self.LineFormRushWait = LineFormRushWait
		self.LineFormRushInterval = LineFormRushInterval
		self.LineFormFallWait = LineFormFallWait
		self.LineFormFallInterval = LineFormFallInterval
		self.PercentLifeTransition = PercentLifeTransition
		self.PercentLifePrevious = PercentLifePrevious


class PriestBossPhaseSelector:
	ChildNames = ["第一段階", "第三段階", "第二段階", "第四段階"]

	def __init__(self, Name, IsSelectOnlyOnce, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSelectOnlyOnce = IsSelectOnlyOnce
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class PriestBossPhaseThird:

	def __init__(self, Name, BreakIronBallCount, PercentLifeTransition, PercentLifePrevious, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BreakIronBallCount = BreakIronBallCount
		self.PercentLifeTransition = PercentLifeTransition
		self.PercentLifePrevious = PercentLifePrevious


class PriestBossShadowCloneEnemyRoot:
	ChildNames = ["フェイズ終了", "フェイズ開始", "リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, IsReactionOnDead, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReactionOnDead = IsReactionOnDead
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class PriestBossShadowCloneThrow:
	ChildNames = ["攻撃", "攻撃後", "準備完了待ち"]

	def __init__(self, Name, ShadowCloneOffsetY, ShadowCloneRadius, ShadowCloneLefeBoneName, ShadowCloneRightBoneName, ShadowCloneAngleOffset, PrepareTimer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShadowCloneOffsetY = ShadowCloneOffsetY
		self.ShadowCloneRadius = ShadowCloneRadius
		self.ShadowCloneLefeBoneName = ShadowCloneLefeBoneName
		self.ShadowCloneRightBoneName = ShadowCloneRightBoneName
		self.ShadowCloneAngleOffset = ShadowCloneAngleOffset
		self.PrepareTimer = PrepareTimer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossShadowClonesReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class PriestBossSlowWarpMove:
	ChildNames = ["回転", "移動"]

	def __init__(self, Name, AfterImage0AppearFrame, AfterImage1AppearFrame, AppearFrame, TurnFirst, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AfterImage0AppearFrame = AfterImage0AppearFrame
		self.AfterImage1AppearFrame = AfterImage1AppearFrame
		self.AppearFrame = AppearFrame
		self.TurnFirst = TurnFirst
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossStageRotationSelector:
	ChildNames = ["回転あり", "回転なし"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class PriestBossSynchroMode:
	ChildNames = ["一列流星", "一列突進", "円陣弓", "円陣突進", "待機"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class PriestBossWalkAttack:
	ChildNames = ["回転", "待機", "移動"]

	def __init__(self, Name, GoalDistanceTolerance, AngleNeedTurn, AtDirType, AtAttr, AtType, AtShieldBreakPower, AtImpact, AtPowerReduce, AtPower, AtDamage, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.AngleNeedTurn = AngleNeedTurn
		self.AtDirType = AtDirType
		self.AtAttr = AtAttr
		self.AtType = AtType
		self.AtShieldBreakPower = AtShieldBreakPower
		self.AtImpact = AtImpact
		self.AtPowerReduce = AtPowerReduce
		self.AtPower = AtPower
		self.AtDamage = AtDamage
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class PriestBossWarpToSafePos:
	ChildNames = ["転移"]

	def __init__(self, Name, OffsetY, OffsetZ, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetY = OffsetY
		self.OffsetZ = OffsetZ
		self.Child0 = Child0


class PriestIronBallAttack:
	ChildNames = ["投擲"]

	def __init__(self, Name, Speed, ShootPitchMin, ShootPitchMax, Noise, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.ShootPitchMin = ShootPitchMin
		self.ShootPitchMax = ShootPitchMax
		self.Noise = Noise
		self.Child0 = Child0


class PullOutTree:
	ChildNames = ["回転", "生成待機", "移動", "装備"]

	def __init__(self, Name, TurnAng, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnAng = TurnAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RailMoveObject:
	ChildNames = ["停止", "移動"]

	def __init__(self, Name, ASKeyName_On, ASKeyName_Off, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName_On = ASKeyName_On
		self.ASKeyName_Off = ASKeyName_Off
		self.Child0 = Child0
		self.Child1 = Child1


class RailMoveObjectOneWay:
	ChildNames = ["停止", "移動"]

	def __init__(self, Name, ASKeyName_On, ASKeyName_Off, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName_On = ASKeyName_On
		self.ASKeyName_Off = ASKeyName_Off
		self.Child0 = Child0
		self.Child1 = Child1


class RailMoveRandomIgnoreStop:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "移動"]

	def __init__(self, Name, StopRate, OnRailDistance, FarDistance, Speed, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopRate = StopRate
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RailMoveRemains:
	ChildNames = ["一時停止", "停止", "再稼働", "移動"]

	def __init__(self, Name, ReactivateTime, FrontCheckMinDist, FrontDirUpdateInterval, SpeedScale, InitPosByRailRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactivateTime = ReactivateTime
		self.FrontCheckMinDist = FrontCheckMinDist
		self.FrontDirUpdateInterval = FrontDirUpdateInterval
		self.SpeedScale = SpeedScale
		self.InitPosByRailRatio = InitPosByRailRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RailMoveRemainsBGCamera:
	ChildNames = ["一時停止", "停止", "再稼働", "移動"]

	def __init__(self, Name, DungeonName, RailName, IsAllowRotAxisX, ReactivateTime, FrontCheckMinDist, FrontDirUpdateInterval, SpeedScale, InitPosByRailRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DungeonName = DungeonName
		self.RailName = RailName
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.ReactivateTime = ReactivateTime
		self.FrontCheckMinDist = FrontCheckMinDist
		self.FrontDirUpdateInterval = FrontDirUpdateInterval
		self.SpeedScale = SpeedScale
		self.InitPosByRailRatio = InitPosByRailRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RailMoveRndIgnrStopPlayAS:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "移動", "ＡＳ再生"]

	def __init__(self, Name, StopRate, OnRailDistance, FarDistance, Speed, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopRate = StopRate
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RailMoveWithClose:
	ChildNames = ["レールに向かう", "停止", "停止点移動", "移動"]

	def __init__(self, Name, OnRailDistance, FarDistance, Speed, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RandomSelectThreeAction:
	ChildNames = ["行動Ａ", "行動Ｂ", "行動Ｃ"]

	def __init__(self, Name, RateActionA, RateActionB, RateActionC, CorrectRatioA, CorrectRatioB, CorrectRatioC, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RateActionA = RateActionA
		self.RateActionB = RateActionB
		self.RateActionC = RateActionC
		self.CorrectRatioA = CorrectRatioA
		self.CorrectRatioB = CorrectRatioB
		self.CorrectRatioC = CorrectRatioC
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RandomSelectTwoAction:
	ChildNames = ["行動Ａ", "行動Ｂ"]

	def __init__(self, Name, TransitionRateToA, CorrectRateToA, CorrectRateToB, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TransitionRateToA = TransitionRateToA
		self.CorrectRateToA = CorrectRateToA
		self.CorrectRateToB = CorrectRateToB
		self.Child0 = Child0
		self.Child1 = Child1


class RangeAttackSelect:
	ChildNames = ["レンジ内", "レンジ外"]

	def __init__(self, Name, RangeDist, WeaponIdx, IsIgnoreSmallHit, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RangeDist = RangeDist
		self.WeaponIdx = WeaponIdx
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.Child0 = Child0
		self.Child1 = Child1


class RangeCheckSeqTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, Range, CheckFar, IsFinishedByFailAction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Range = Range
		self.CheckFar = CheckFar
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.Child0 = Child0
		self.Child1 = Child1


class RangeHeightSelectTwoAction:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, MaxY, MinY, FarDist, BaseDist, WeaponIdx, IsSelectEveryFrame, IsRangeXZ, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxY = MaxY
		self.MinY = MinY
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.IsRangeXZ = IsRangeXZ
		self.Child0 = Child0
		self.Child1 = Child1


class RangeLineReachSelectTwoAction:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, FarDist, BaseDist, WeaponIdx, IsSelectEveryFrame, IsRangeXZ, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.IsRangeXZ = IsRangeXZ
		self.Child0 = Child0
		self.Child1 = Child1


class RangeObstacleCheck:
	ChildNames = ["レンジ内", "レンジ外"]

	def __init__(self, Name, WeaponIdx, RangeDist, HeightMin, HeightMax, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.RangeDist = RangeDist
		self.HeightMin = HeightMin
		self.HeightMax = HeightMax
		self.Child0 = Child0
		self.Child1 = Child1


class RangeSelectThreeAction:
	ChildNames = ["中距離", "近距離", "遠距離"]

	def __init__(self, Name, NearDist, FarDist, BaseDist, WeaponIdx, IsSelectEveryFrame, IsRangeXZ, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDist = NearDist
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.IsRangeXZ = IsRangeXZ
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RangeSelectTwoAction:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, FarDist, BaseDist, WeaponIdx, IsSelectEveryFrame, IsRangeXZ, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FarDist = FarDist
		self.BaseDist = BaseDist
		self.WeaponIdx = WeaponIdx
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.IsRangeXZ = IsRangeXZ
		self.Child0 = Child0
		self.Child1 = Child1


class RapidAttackAllowSelect:
	ChildNames = ["連打不許可", "連打許可"]

	def __init__(self, Name, AttackNum, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackNum = AttackNum
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class ReduceDistanceToTargetPos:
	ChildNames = ["行動"]

	def __init__(self, Name, DistanceScale, MinReduceDist, MaxReduceDist, MinDist, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceScale = DistanceScale
		self.MinReduceDist = MinReduceDist
		self.MaxReduceDist = MaxReduceDist
		self.MinDist = MinDist
		self.Child0 = Child0


class ReferenceNPCViewWithDynAS:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ReflectableBulletThrown:
	ChildNames = ["反射", "投擲"]

	def __init__(self, Name, ReclectSpd, HitColName, IsReflectByGuard, IsReflectByArrow, RefSpeedRatioByJustGuard, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReclectSpd = ReclectSpd
		self.HitColName = HitColName
		self.IsReflectByGuard = IsReflectByGuard
		self.IsReflectByArrow = IsReflectByArrow
		self.RefSpeedRatioByJustGuard = RefSpeedRatioByJustGuard
		self.Child0 = Child0
		self.Child1 = Child1


class ReflectableEscape:
	ChildNames = ["反転", "移動"]

	def __init__(self, Name, EscapeDist, NearDist, EscapeTimer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EscapeDist = EscapeDist
		self.NearDist = NearDist
		self.EscapeTimer = EscapeTimer
		self.Child0 = Child0
		self.Child1 = Child1


class ReflectableIgnitedThrown:
	ChildNames = ["反射", "投擲"]

	def __init__(self, Name, HitColName, IsReflectByGuard, IsReflectByArrow, RefSpeedRatioByJustGuard, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HitColName = HitColName
		self.IsReflectByGuard = IsReflectByGuard
		self.IsReflectByArrow = IsReflectByArrow
		self.RefSpeedRatioByJustGuard = RefSpeedRatioByJustGuard
		self.Child0 = Child0
		self.Child1 = Child1


class RegistedActorNumTwoSelect:
	ChildNames = ["より多い", "以下"]

	def __init__(self, Name, Num, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Num = Num
		self.Child0 = Child0
		self.Child1 = Child1


class RemainElectricCannonBeamAttack:
	ChildNames = ["予兆", "溜め", "発射"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RemainElectricCannonRoot:
	ChildNames = ["待機", "攻撃", "死亡"]

	def __init__(self, Name, SearchMaxDistLoiter, SearchMaxDist, SearchMinDist, SearchDistMargin, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchMaxDistLoiter = SearchMaxDistLoiter
		self.SearchMaxDist = SearchMaxDist
		self.SearchMinDist = SearchMinDist
		self.SearchDistMargin = SearchDistMargin
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RemainsElectricBGCamera:
	ChildNames = ["一時停止", "停止", "再稼働", "移動"]

	def __init__(self, Name, ParentActorName, DungeonName, RailName, IsAllowRotAxisX, ReactivateTime, FrontCheckMinDist, FrontDirUpdateInterval, SpeedScale, InitPosByRailRatio, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ParentActorName = ParentActorName
		self.DungeonName = DungeonName
		self.RailName = RailName
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.ReactivateTime = ReactivateTime
		self.FrontCheckMinDist = FrontCheckMinDist
		self.FrontDirUpdateInterval = FrontDirUpdateInterval
		self.SpeedScale = SpeedScale
		self.InitPosByRailRatio = InitPosByRailRatio
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RemainsElectricRoot:
	ChildNames = ["デモ用レール移動", "通常行動"]

	def __init__(self, Name, RemainsTypeID, IsAllowRotAxisX, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RemainsTypeID = RemainsTypeID
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.Child0 = Child0
		self.Child1 = Child1


class RemainsFireBattleMove:
	ChildNames = ["待機", "攻撃", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RemainsFireBattleStepSelector:
	ChildNames = ["1st", "2nd", "3rd", "Idle"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RemainsFireDroneNormal:
	ChildNames = ["停止", "停止点移動", "移動", "警報"]

	def __init__(self, Name, AdjustRadius, LightLengthOffset, IsIgnoreNoWaitStopPoint, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AdjustRadius = AdjustRadius
		self.LightLengthOffset = LightLengthOffset
		self.IsIgnoreNoWaitStopPoint = IsIgnoreNoWaitStopPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RemainsFireRoot:
	ChildNames = ["待機", "通常行動", "遺物チャレンジ中"]

	def __init__(self, Name, TargetBoneName, RemainsTypeID, IsAllowRotAxisX, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBoneName = TargetBoneName
		self.RemainsTypeID = RemainsTypeID
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RemainsLithograph:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機", "動作完了"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RemainsWaterBattleRoot:
	ChildNames = ["へたれ中", "ダメージ", "パオーン", "攻撃中", "正常化", "生成中"]

	def __init__(self, Name, CallClearDemoTimer, AfterDamageTimer, AfterPaooonTimer, AfterHellTimer, FirstBulletTimer, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CallClearDemoTimer = CallClearDemoTimer
		self.AfterDamageTimer = AfterDamageTimer
		self.AfterPaooonTimer = AfterPaooonTimer
		self.AfterHellTimer = AfterHellTimer
		self.FirstBulletTimer = FirstBulletTimer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class RemainsWaterBulletController:
	ChildNames = ["冷却中", "射出前待機", "射出後待機", "誘導弾発射", "魚雷発射"]

	def __init__(self, Name, InsideAreaCenter, InsideAreaWidth, InsideAreaRadius, FirstBulletTimer, SecondBulletTimer, ChaseBulletNum, ExplodeBulletNum, ChaseBulletActorName, ExplodeBulletActorName, NextBulletTimerSuccess, NextBulletTimerFail, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InsideAreaCenter = InsideAreaCenter
		self.InsideAreaWidth = InsideAreaWidth
		self.InsideAreaRadius = InsideAreaRadius
		self.FirstBulletTimer = FirstBulletTimer
		self.SecondBulletTimer = SecondBulletTimer
		self.ChaseBulletNum = ChaseBulletNum
		self.ExplodeBulletNum = ExplodeBulletNum
		self.ChaseBulletActorName = ChaseBulletActorName
		self.ExplodeBulletActorName = ExplodeBulletActorName
		self.NextBulletTimerSuccess = NextBulletTimerSuccess
		self.NextBulletTimerFail = NextBulletTimerFail
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RemainsWaterChaseBulletRoot:
	ChildNames = ["ダメージ", "待機", "復活", "消滅", "爆発", "通常"]

	def __init__(self, Name, AtkMinDamage, CheckPower, HighDamageAddSpd, LowDamageAddSpd, ShootAddSpd, ResetASName, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkMinDamage = AtkMinDamage
		self.CheckPower = CheckPower
		self.HighDamageAddSpd = HighDamageAddSpd
		self.LowDamageAddSpd = LowDamageAddSpd
		self.ShootAddSpd = ShootAddSpd
		self.ResetASName = ResetASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class RemainsWaterNormal:
	ChildNames = ["パオーン", "待機"]

	def __init__(self, Name, InsideAreaWidth, InsideAreaCenter, InsideAreaWidth02, InsideAreaCenter02, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InsideAreaWidth = InsideAreaWidth
		self.InsideAreaCenter = InsideAreaCenter
		self.InsideAreaWidth02 = InsideAreaWidth02
		self.InsideAreaCenter02 = InsideAreaCenter02
		self.Child0 = Child0
		self.Child1 = Child1


class RemainsWaterRoot:
	ChildNames = ["水上待機", "水中待機", "通常行動", "遺物戦中"]

	def __init__(self, Name, RemainsTypeID, IsAllowRotAxisX, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RemainsTypeID = RemainsTypeID
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RemainsWaterWeakPointRoot:
	ChildNames = ["待機", "戦闘終了", "格納中", "機能停止", "起動中"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RemainsWindBatteryAttack:
	ChildNames = ["チャージ", "待機", "照準", "照準準備", "発射"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RemainsWindBatteryRoot:
	ChildNames = ["リアクション", "待機", "落雷スタン", "見回す", "視覚反応", "追跡", "退避", "音反応"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class RemainsWindRoot:
	ChildNames = ["デモ用レール移動", "通常行動", "遺物チャレンジ中"]

	def __init__(self, Name, RemainsTypeID, IsAllowRotAxisX, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RemainsTypeID = RemainsTypeID
		self.IsAllowRotAxisX = IsAllowRotAxisX
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RememberMesOneActorEnemyRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, RememberKey, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RememberKey = RememberKey
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class RemoteBomb:
	ChildNames = ["待機", "所持", "投擲生成", "爆発", "爆発予約"]

	def __init__(self, Name, WindRatio, XLinkKey, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WindRatio = WindRatio
		self.XLinkKey = XLinkKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class RepeatByLargeDamage:
	ChildNames = ["吹っ飛び"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class RestLifeSelect:
	ChildNames = ["元気", "瀕死"]

	def __init__(self, Name, LifeRatio, IsTrgOnly, IsEnter, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LifeRatio = LifeRatio
		self.IsTrgOnly = IsTrgOnly
		self.IsEnter = IsEnter
		self.Child0 = Child0
		self.Child1 = Child1


class RestreintTired:
	ChildNames = ["帰還", "注意"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ReturnFromReactionSelect:
	ChildNames = ["ガード復帰", "ダメージ復帰", "弾かれ復帰", "通常"]

	def __init__(self, Name, IsChangeToNormalByFinish, IsEnableRetFromDamage, IsEnableRetFromGuard, IsEnableRetFromRebound, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeToNormalByFinish = IsChangeToNormalByFinish
		self.IsEnableRetFromDamage = IsEnableRetFromDamage
		self.IsEnableRetFromGuard = IsEnableRetFromGuard
		self.IsEnableRetFromRebound = IsEnableRetFromRebound
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ReuseBulletPartsRoot:
	ChildNames = ["投擲生成", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class RideHorseAI:
	ChildNames = ["なだめる", "乗る"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class RitoHeroSoulGiftRoot:
	ChildNames = ["待機", "発動", "退場"]

	def __init__(self, Name, Scale, ActorName, PosOffset, RotOffset, UseInitMtxForBasePos, UseInitMtxForBaseRot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Scale = Scale
		self.ActorName = ActorName
		self.PosOffset = PosOffset
		self.RotOffset = RotOffset
		self.UseInitMtxForBasePos = UseInitMtxForBasePos
		self.UseInitMtxForBaseRot = UseInitMtxForBaseRot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class RodEnemyFindPlayer:
	ChildNames = ["ケミカル仲間招来", "ナビメッシュ無し", "ロッド攻撃", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "武器ケミカル付与", "武器投げ", "気づき", "速攻"]

	def __init__(self, Name, MagicPer, MagicAttackDir, MagicCheckInterval, RodWeaponIdx, MagicIntervalIntensity, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, ChemicalSearchDist, NoSearchDist, Voltage, ChemicalActionDist, ThrowWeaponPer, ThrowWeaponDist, NoChemSearchWpIdx, NoBurnWaterDepth, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MagicPer = MagicPer
		self.MagicAttackDir = MagicAttackDir
		self.MagicCheckInterval = MagicCheckInterval
		self.RodWeaponIdx = RodWeaponIdx
		self.MagicIntervalIntensity = MagicIntervalIntensity
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.ChemicalSearchDist = ChemicalSearchDist
		self.NoSearchDist = NoSearchDist
		self.Voltage = Voltage
		self.ChemicalActionDist = ChemicalActionDist
		self.ThrowWeaponPer = ThrowWeaponPer
		self.ThrowWeaponDist = ThrowWeaponDist
		self.NoChemSearchWpIdx = NoChemSearchWpIdx
		self.NoBurnWaterDepth = NoBurnWaterDepth
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13


class RodRoot:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class RopeRoot:
	ChildNames = ["つかまられ中", "切断", "燃え尽き", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class RuinGuardianRoot:

	def __init__(self, Name, SweepFrame, DropThreshold, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SweepFrame = SweepFrame
		self.DropThreshold = DropThreshold


class RupeeRabbitNormal:
	ChildNames = ["ふり向き", "ターゲット通知", "ダメージ逃走", "ロケーター待機", "威嚇", "徘徊", "戦闘", "気づき", "注目", "興味対象発見", "逃走"]

	def __init__(self, Name, IsUseEscapeState, IsPositiveAttacker, IsSearchTarget, IsEmitForceEscapeSignal, IsReceivedForceEscapeSignal, IsCheckSandStorm, ChangeBattleStateRadius, CounterAttackRadius, CounterAttackRate, AddCautionLevelVal, AutoReduceCautionLevelVal, LimitOverReduceCautionLevelVal, AwnRangeScaleWhenAttention, TargetLostTime, AllowRoarRadius, EscapeWaterFlowLimit, NewFoodAddTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseEscapeState = IsUseEscapeState
		self.IsPositiveAttacker = IsPositiveAttacker
		self.IsSearchTarget = IsSearchTarget
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.IsReceivedForceEscapeSignal = IsReceivedForceEscapeSignal
		self.IsCheckSandStorm = IsCheckSandStorm
		self.ChangeBattleStateRadius = ChangeBattleStateRadius
		self.CounterAttackRadius = CounterAttackRadius
		self.CounterAttackRate = CounterAttackRate
		self.AddCautionLevelVal = AddCautionLevelVal
		self.AutoReduceCautionLevelVal = AutoReduceCautionLevelVal
		self.LimitOverReduceCautionLevelVal = LimitOverReduceCautionLevelVal
		self.AwnRangeScaleWhenAttention = AwnRangeScaleWhenAttention
		self.TargetLostTime = TargetLostTime
		self.AllowRoarRadius = AllowRoarRadius
		self.EscapeWaterFlowLimit = EscapeWaterFlowLimit
		self.NewFoodAddTime = NewFoodAddTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class SafeMoveAroundTarget:
	ChildNames = ["移動"]

	def __init__(self, Name, StartRange, EndRange, ChangeRangeRate, ForceTurnTimeBase, ForceTurnTimeRand, ForceTurnStopTimeBase, ForceTurnStopTimeRand, UpdateTargetPosTime, TargetOffsetDegree, LOSFailOffsetDegree, UpdateNumCalc, MinOffsetLength, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartRange = StartRange
		self.EndRange = EndRange
		self.ChangeRangeRate = ChangeRangeRate
		self.ForceTurnTimeBase = ForceTurnTimeBase
		self.ForceTurnTimeRand = ForceTurnTimeRand
		self.ForceTurnStopTimeBase = ForceTurnStopTimeBase
		self.ForceTurnStopTimeRand = ForceTurnStopTimeRand
		self.UpdateTargetPosTime = UpdateTargetPosTime
		self.TargetOffsetDegree = TargetOffsetDegree
		self.LOSFailOffsetDegree = LOSFailOffsetDegree
		self.UpdateNumCalc = UpdateNumCalc
		self.MinOffsetLength = MinOffsetLength
		self.Child0 = Child0


class SandfallWithSound:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SandwormAttackMove:
	ChildNames = ["攻撃移動", "離脱"]

	def __init__(self, Name, SecessionDist, AttackAngle, DamageBaseNode, DamageAngle, LostDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SecessionDist = SecessionDist
		self.AttackAngle = AttackAngle
		self.DamageBaseNode = DamageBaseNode
		self.DamageAngle = DamageAngle
		self.LostDist = LostDist
		self.Child0 = Child0
		self.Child1 = Child1


class SandwormBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, AttackAngle, AttackInterval, AttackIntervalRand, BattleFailTimer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackAngle = AttackAngle
		self.AttackInterval = AttackInterval
		self.AttackIntervalRand = AttackIntervalRand
		self.BattleFailTimer = BattleFailTimer
		self.Child0 = Child0
		self.Child1 = Child1


class SandwormBlownOff:
	ChildNames = ["ぴより中", "ぴより終了", "ぴより開始", "先行動", "後攻撃"]

	def __init__(self, Name, BlownOffTimer, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlownOffTimer = BlownOffTimer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class SandwormCircleMoveTarget:
	ChildNames = ["移動", "近づき", "遠ざかり"]

	def __init__(self, Name, Radius, RadiusMargin, Speed, Direction, FrontCheckLength, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.RadiusMargin = RadiusMargin
		self.Speed = Speed
		self.Direction = Direction
		self.FrontCheckLength = FrontCheckLength
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SandwormFindTarget:
	ChildNames = ["威嚇", "戦闘", "移動"]

	def __init__(self, Name, LostVMin, LostVMax, LostTimer, LostRange, AttackRange, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.AttackRange = AttackRange
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SandwormLost:
	ChildNames = ["強制帰還", "潜る", "行動"]

	def __init__(self, Name, DiveSandOffset, RailCheckInterval, SealForceReturn, ForceReturnNoCameraRad, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DiveSandOffset = DiveSandOffset
		self.RailCheckInterval = RailCheckInterval
		self.SealForceReturn = SealForceReturn
		self.ForceReturnNoCameraRad = ForceReturnNoCameraRad
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SandwormNavSearchWait:
	ChildNames = ["移動", "見まわす"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SandwormNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, SealedSight, SealedHearing, SealedTerror, SealedWorry, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SealedSight = SealedSight
		self.SealedHearing = SealedHearing
		self.SealedTerror = SealedTerror
		self.SealedWorry = SealedWorry
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SandwormNoticeSound:
	ChildNames = ["振り向き", "攻撃", "攻撃後始末", "移動", "見失い"]

	def __init__(self, Name, LockOnDist, RetryDist, TargetActorLockOnDist, TargetPosLockOnDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LockOnDist = LockOnDist
		self.RetryDist = RetryDist
		self.TargetActorLockOnDist = TargetActorLockOnDist
		self.TargetPosLockOnDist = TargetPosLockOnDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class SandwormRNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, SealedSight, SealedHearing, SealedTerror, SealedWorry, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SealedSight = SealedSight
		self.SealedHearing = SealedHearing
		self.SealedTerror = SealedTerror
		self.SealedWorry = SealedWorry
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SandwormRRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, SandOffset, WeakPointDamageRate, WeakChimicalDamageRate, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SandOffset = SandOffset
		self.WeakPointDamageRate = WeakPointDamageRate
		self.WeakChimicalDamageRate = WeakChimicalDamageRate
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class SandwormReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class SandwormRoam:
	ChildNames = ["ジャンプ", "レール移動", "待ち伏せ"]

	def __init__(self, Name, JumpTimerBase, JumpTimerRand, JumpDistanceXZ, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpTimerBase = JumpTimerBase
		self.JumpTimerRand = JumpTimerRand
		self.JumpDistanceXZ = JumpDistanceXZ
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SandwormRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, SandOffset, WeakPointDamageRate, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SandOffset = SandOffset
		self.WeakPointDamageRate = WeakPointDamageRate
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class SandwormStun:
	ChildNames = ["復帰", "気絶"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SelfXRotSelector:
	ChildNames = ["以上", "未満"]

	def __init__(self, Name, Angle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Angle = Angle
		self.Child0 = Child0
		self.Child1 = Child1


class SeqAnimalAttack:
	ChildNames = ["攻撃", "攻撃ハズレ後", "攻撃ヒット後", "攻撃前"]

	def __init__(self, Name, IsUseAfterAttackState, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseAfterAttackState = IsUseAfterAttackState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SeqAtHitAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqCloseDistTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, CloseDist, WeaponIdx, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.WeaponIdx = WeaponIdx
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqDynamicTimeredTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, FirstActionTime, SecondActionTime, AllActionTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FirstActionTime = FirstActionTime
		self.SecondActionTime = SecondActionTime
		self.AllActionTime = AllActionTime
		self.Child0 = Child0
		self.Child1 = Child1


class SeqFirstPointTwo:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.Child0 = Child0
		self.Child1 = Child1


class SeqGroundHit:
	ChildNames = ["地上", "空中"]

	def __init__(self, Name, IsCheckChangeable, IsNoHitEnd, CheckType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckChangeable = IsCheckChangeable
		self.IsNoHitEnd = IsNoHitEnd
		self.CheckType = CheckType
		self.Child0 = Child0
		self.Child1 = Child1


class SeqGroundHitAssassinBoss:
	ChildNames = ["地上", "空中"]

	def __init__(self, Name, IsCheckChangeable, IsNoHitEnd, CheckType, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckChangeable = IsCheckChangeable
		self.IsNoHitEnd = IsNoHitEnd
		self.CheckType = CheckType
		self.Child0 = Child0
		self.Child1 = Child1


class SeqHiddenOctarockSearch:
	ChildNames = ["サーチ", "未発見", "発見"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqIfElseAction:
	ChildNames = ["先行動", "先行動失敗", "後行動"]

	def __init__(self, Name, FailType, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FailType = FailType
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqIfFailAction:
	ChildNames = ["先行動", "先行動失敗"]

	def __init__(self, Name, IsEndChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEndChangeable = IsEndChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqNextMessage:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, DelayTimeMax, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DelayTimeMax = DelayTimeMax
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqOctarockAttack:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqOctarockWigReaction:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqPredictOctarockAttack:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqPursuit:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, PursuitPer, PursuitDist, WeaponIdx, IsEndPursuit, IsGuardNoPursuit, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PursuitPer = PursuitPer
		self.PursuitDist = PursuitDist
		self.WeaponIdx = WeaponIdx
		self.IsEndPursuit = IsEndPursuit
		self.IsGuardNoPursuit = IsGuardNoPursuit
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqRandomRepeat:
	ChildNames = ["行動"]

	def __init__(self, Name, MinActionNum, MaxActionNum, IsEndChangeable, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinActionNum = MinActionNum
		self.MaxActionNum = MaxActionNum
		self.IsEndChangeable = IsEndChangeable
		self.Child0 = Child0


class SeqTargetTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.Child0 = Child0
		self.Child1 = Child1


class SeqThreeAction:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SeqTimeredAction:
	ChildNames = ["行動"]

	def __init__(self, Name, ActionTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActionTime = ActionTime
		self.Child0 = Child0


class SeqTimeredPlusRandomTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, FirstActionRandMax, SecondActionRandMax, FirstActionTime, SecondActionTime, AllActionTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FirstActionRandMax = FirstActionRandMax
		self.SecondActionRandMax = SecondActionRandMax
		self.FirstActionTime = FirstActionTime
		self.SecondActionTime = SecondActionTime
		self.AllActionTime = AllActionTime
		self.Child0 = Child0
		self.Child1 = Child1


class SeqTimeredTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, FirstActionTime, SecondActionTime, AllActionTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FirstActionTime = FirstActionTime
		self.SecondActionTime = SecondActionTime
		self.AllActionTime = AllActionTime
		self.Child0 = Child0
		self.Child1 = Child1


class SeqTrgPartsNotice:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, PartsName, IsFinishByNoNoticeActionEnd, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.IsFinishByNoNoticeActionEnd = IsFinishByNoNoticeActionEnd
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqTwoAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SeqTwoLineReachableTargetAction:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, ReachableCheckType1, ReachableCheckType2, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReachableCheckType1 = ReachableCheckType1
		self.ReachableCheckType2 = ReachableCheckType2
		self.Child0 = Child0
		self.Child1 = Child1


class SeqTwoWeakPointOnFirstDo:
	ChildNames = ["先行動", "後行動"]

	def __init__(self, Name, IsFinishedByFailAction, IsEndChangeable, IsNoChangeable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFinishedByFailAction = IsFinishedByFailAction
		self.IsEndChangeable = IsEndChangeable
		self.IsNoChangeable = IsNoChangeable
		self.Child0 = Child0
		self.Child1 = Child1


class SetPartBind:
	ChildNames = ["行動"]

	def __init__(self, Name, BaseNodeName, PartialNodeName, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseNodeName = BaseNodeName
		self.PartialNodeName = PartialNodeName
		self.Child0 = Child0


class SetTargetPosForAngryKokko:
	ChildNames = ["子アクション"]

	def __init__(self, Name, AddLength, HeightOffset, RandRange, RandRate, UpdateTargetInterval, MaxUpdateNum, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddLength = AddLength
		self.HeightOffset = HeightOffset
		self.RandRange = RandRange
		self.RandRate = RandRate
		self.UpdateTargetInterval = UpdateTargetInterval
		self.MaxUpdateNum = MaxUpdateNum
		self.Child0 = Child0


class SetTargetPosForFlyThroughMove:
	ChildNames = ["移動", "通過移動"]

	def __init__(self, Name, TargetPosFixDist, ThroughDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetPosFixDist = TargetPosFixDist
		self.ThroughDist = ThroughDist
		self.Child0 = Child0
		self.Child1 = Child1


class SetTargetPosToPlayer:
	ChildNames = ["子アクション"]

	def __init__(self, Name, AddLength, HeightOffset, RandRange, RandRate, UpdateTargetInterval, MaxUpdateNum, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddLength = AddLength
		self.HeightOffset = HeightOffset
		self.RandRange = RandRange
		self.RandRate = RandRate
		self.UpdateTargetInterval = UpdateTargetInterval
		self.MaxUpdateNum = MaxUpdateNum
		self.Child0 = Child0


class ShootingEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "画面外攻撃"]

	def __init__(self, Name, OutScreenDist, OutScreenAttackNum, OutScrnAtkOffset, OutScrnAtkOffsetY, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OutScreenDist = OutScreenDist
		self.OutScreenAttackNum = OutScreenAttackNum
		self.OutScrnAtkOffset = OutScrnAtkOffset
		self.OutScrnAtkOffsetY = OutScrnAtkOffsetY
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ShootingEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "危険回避", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻", "隠れられない", "隠れる"]

	def __init__(self, Name, ExplosivesAvoidDist, ExplosivesAvoidSpeed, ExplosivesAvoidAng, HideStartDistMin, HideStartDistMax, ReHideTime, ShootBaseDist, ShootDistRatio, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ExplosivesAvoidDist = ExplosivesAvoidDist
		self.ExplosivesAvoidSpeed = ExplosivesAvoidSpeed
		self.ExplosivesAvoidAng = ExplosivesAvoidAng
		self.HideStartDistMin = HideStartDistMin
		self.HideStartDistMax = HideStartDistMax
		self.ReHideTime = ReHideTime
		self.ShootBaseDist = ShootBaseDist
		self.ShootDistRatio = ShootDistRatio
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class ShootingStarRoot:
	ChildNames = ["光の柱を出す", "飛んでいく"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ShutterFence:
	ChildNames = ["オープン", "オープン待機", "クローズ", "クローズ待機", "プリオープン"]

	def __init__(self, Name, ASKeyName_On, ASKeyName_Off, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName_On = ASKeyName_On
		self.ASKeyName_Off = ASKeyName_Off
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class SignalFlowchartRootAI:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SignalSendingMagneStickAcceptor:
	ChildNames = ["刺さった", "抜けた"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SignaledSpotBgmTrigger:
	ChildNames = ["再生", "待機"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SimpleASBridge:
	ChildNames = ["通常"]

	def __init__(self, Name, ASName, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Child0 = Child0


class SimpleEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SimpleEscapeFromTarget:
	ChildNames = ["後退移動"]

	def __init__(self, Name, SpaceDist, KeepTime, WeaponIdx, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpaceDist = SpaceDist
		self.KeepTime = KeepTime
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0


class SimpleKokkoRoot:
	ChildNames = ["子アクション"]

	def __init__(self, Name, AliveTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AliveTime = AliveTime
		self.Child0 = Child0


class SimpleLiftable:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SimpleLiftableDLC:
	ChildNames = ["所持", "投擲生成", "通常"]

	def __init__(self, Name, ScaleToLiftUp, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ScaleToLiftUp = ScaleToLiftUp
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SimpleLineBeam:
	ChildNames = ["待機", "攻撃"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SimpleShootingEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, ShootBaseDist, ShootDistRatio, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootBaseDist = ShootBaseDist
		self.ShootDistRatio = ShootDistRatio
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossApproachRoot:
	ChildNames = ["移動", "遠距離攻撃移動"]

	def __init__(self, Name, CheckWallDist, ApproachTime, EndDist, EndFarDist, DoAttack, AttackStartDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckWallDist = CheckWallDist
		self.ApproachTime = ApproachTime
		self.EndDist = EndDist
		self.EndFarDist = EndFarDist
		self.DoAttack = DoAttack
		self.AttackStartDist = AttackStartDist
		self.Child0 = Child0
		self.Child1 = Child1


class SiteBossArrowRainAttack:
	ChildNames = ["回避", "子機発射", "弾発射", "準備", "溜め", "終了"]

	def __init__(self, Name, ArrowNum, HoldTime, InitHoldTime, ArrowName, IsFinishAtNoDevice, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, AvoidLifeRate, AvoidCountMax, AvoidAngle, AvoidDist, SeqAvoidRate, AvoidDistRand, AvoidWaitCount, AvoidWaitCountRand, ChaseDist, ChaseDistOffset, UpDownAvoidRate, IsKeepDistance, KeepDistance, TrigEventAtHold, SpineControlOffsetAngleLR, SpineControlOffsetAngleUD, ReflectOffset, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.HoldTime = HoldTime
		self.InitHoldTime = InitHoldTime
		self.ArrowName = ArrowName
		self.IsFinishAtNoDevice = IsFinishAtNoDevice
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.AvoidLifeRate = AvoidLifeRate
		self.AvoidCountMax = AvoidCountMax
		self.AvoidAngle = AvoidAngle
		self.AvoidDist = AvoidDist
		self.SeqAvoidRate = SeqAvoidRate
		self.AvoidDistRand = AvoidDistRand
		self.AvoidWaitCount = AvoidWaitCount
		self.AvoidWaitCountRand = AvoidWaitCountRand
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.UpDownAvoidRate = UpDownAvoidRate
		self.IsKeepDistance = IsKeepDistance
		self.KeepDistance = KeepDistance
		self.TrigEventAtHold = TrigEventAtHold
		self.SpineControlOffsetAngleLR = SpineControlOffsetAngleLR
		self.SpineControlOffsetAngleUD = SpineControlOffsetAngleUD
		self.ReflectOffset = ReflectOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class SiteBossAttackRoot:
	ChildNames = ["大剣装備", "小剣装備", "弓装備", "槍装備"]

	def __init__(self, Name, EquipWeapon, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EquipWeapon = EquipWeapon
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossBigFlameBall:
	ChildNames = ["反射後爆発", "強制消滅", "所持", "爆発", "生成待機", "発射", "自然消滅"]

	def __init__(self, Name, DestOffset, DestOffset1, MoveSpeed, MoveOffset, ChemicalIndex, IsInfluence, CountOffset, AtAttr, IsForceDelete, ExplosionTime, ChaseAngleLimit, BindNodeName, IsAdjustHeight, IsSetParentSystemGroupHandler, ReflectSpeedRate, IsSetBindSpeed, IsIgnoreObject, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DestOffset = DestOffset
		self.DestOffset1 = DestOffset1
		self.MoveSpeed = MoveSpeed
		self.MoveOffset = MoveOffset
		self.ChemicalIndex = ChemicalIndex
		self.IsInfluence = IsInfluence
		self.CountOffset = CountOffset
		self.AtAttr = AtAttr
		self.IsForceDelete = IsForceDelete
		self.ExplosionTime = ExplosionTime
		self.ChaseAngleLimit = ChaseAngleLimit
		self.BindNodeName = BindNodeName
		self.IsAdjustHeight = IsAdjustHeight
		self.IsSetParentSystemGroupHandler = IsSetParentSystemGroupHandler
		self.ReflectSpeedRate = ReflectSpeedRate
		self.IsSetBindSpeed = IsSetBindSpeed
		self.IsIgnoreObject = IsIgnoreObject
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossBlowOff:
	ChildNames = ["ふっとび", "大ダメージ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SiteBossBowChildDeviceRoot:
	ChildNames = ["出現", "反射弾", "天空弾", "生成", "生成待機", "疾風弾", "破壊", "自然消滅", "通常待機"]

	def __init__(self, Name, XRotateSpeed, SlowRate, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.XRotateSpeed = XRotateSpeed
		self.SlowRate = SlowRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class SiteBossBowRoot:
	ChildNames = ["リアクション", "出現デモ待ち", "出現デモ終了直後", "通常"]

	def __init__(self, Name, ArrowRainAttackPower, AtMinPower, DemoName, ReflectArrowAttackPower, NormalEntryName, AtDownEntryName, DemoPlayHPRate, OffFlagIndexAtClipping, AddAttackPower, IsPlayed_DemoFlagName, ForceRecoverHitMax, ForceRecoverDamageMax, AddForceRecoverHitNum, AddForceRecoverDamage, IsRemainBoss, BlownOffAtWeakPointHitNum, WeakPointDamageRate, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowRainAttackPower = ArrowRainAttackPower
		self.AtMinPower = AtMinPower
		self.DemoName = DemoName
		self.ReflectArrowAttackPower = ReflectArrowAttackPower
		self.NormalEntryName = NormalEntryName
		self.AtDownEntryName = AtDownEntryName
		self.DemoPlayHPRate = DemoPlayHPRate
		self.OffFlagIndexAtClipping = OffFlagIndexAtClipping
		self.AddAttackPower = AddAttackPower
		self.IsPlayed_DemoFlagName = IsPlayed_DemoFlagName
		self.ForceRecoverHitMax = ForceRecoverHitMax
		self.ForceRecoverDamageMax = ForceRecoverDamageMax
		self.AddForceRecoverHitNum = AddForceRecoverHitNum
		self.AddForceRecoverDamage = AddForceRecoverDamage
		self.IsRemainBoss = IsRemainBoss
		self.BlownOffAtWeakPointHitNum = BlownOffAtWeakPointHitNum
		self.WeakPointDamageRate = WeakPointDamageRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossFlameBall:
	ChildNames = ["反射後爆発", "強制消滅", "所持", "爆発", "生成待機", "発射", "自然消滅"]

	def __init__(self, Name, MoveSpeed, MoveOffset, ChemicalIndex, IsInfluence, CountOffset, AtAttr, IsForceDelete, ExplosionTime, ChaseAngleLimit, BindNodeName, IsAdjustHeight, IsSetParentSystemGroupHandler, ReflectSpeedRate, IsSetBindSpeed, IsIgnoreObject, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed
		self.MoveOffset = MoveOffset
		self.ChemicalIndex = ChemicalIndex
		self.IsInfluence = IsInfluence
		self.CountOffset = CountOffset
		self.AtAttr = AtAttr
		self.IsForceDelete = IsForceDelete
		self.ExplosionTime = ExplosionTime
		self.ChaseAngleLimit = ChaseAngleLimit
		self.BindNodeName = BindNodeName
		self.IsAdjustHeight = IsAdjustHeight
		self.IsSetParentSystemGroupHandler = IsSetParentSystemGroupHandler
		self.ReflectSpeedRate = ReflectSpeedRate
		self.IsSetBindSpeed = IsSetBindSpeed
		self.IsIgnoreObject = IsIgnoreObject
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossGaleArrowRoot:
	ChildNames = ["刺さる", "所持", "爆発", "発射"]

	def __init__(self, Name, Accel, AimSpeed, FallAccel, FallAimSpeed, Gravity, AtRange, AtImpulse, AtImpact, CanReflect, IsReflectToParent, ReflectOffset, RotOffset, IsDelete, AtAttr, IsBreakIceBlock, StickTime, IsAtHitPlayerIgnore, ReflectDamageRate, TransOffset, BindNodeName, IsDeleteAtHit, CallHitSEKey, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Accel = Accel
		self.AimSpeed = AimSpeed
		self.FallAccel = FallAccel
		self.FallAimSpeed = FallAimSpeed
		self.Gravity = Gravity
		self.AtRange = AtRange
		self.AtImpulse = AtImpulse
		self.AtImpact = AtImpact
		self.CanReflect = CanReflect
		self.IsReflectToParent = IsReflectToParent
		self.ReflectOffset = ReflectOffset
		self.RotOffset = RotOffset
		self.IsDelete = IsDelete
		self.AtAttr = AtAttr
		self.IsBreakIceBlock = IsBreakIceBlock
		self.StickTime = StickTime
		self.IsAtHitPlayerIgnore = IsAtHitPlayerIgnore
		self.ReflectDamageRate = ReflectDamageRate
		self.TransOffset = TransOffset
		self.BindNodeName = BindNodeName
		self.IsDeleteAtHit = IsDeleteAtHit
		self.CallHitSEKey = CallHitSEKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossIceSplinterRoot:
	ChildNames = ["反射後爆発", "強制消滅", "所持", "爆発", "生成待機", "発射", "自然消滅"]

	def __init__(self, Name, BindNodeName0, BindNodeName1, BindOffset0, BindOffset1, BindOffset2, ReflectAtkPower, BindOffset3, BindOffset4, BindOffset5, BindOffset6, BindOffset7, BindOffset8, ChaseAngleMin, ChaseParentNode, RotateSpeed, RotateSpeedAtHit, RotateSpeedAtFall, IsForceDelete, ExplosionTime, ChaseAngleLimit, BindNodeName, IsAdjustHeight, IsSetParentSystemGroupHandler, ReflectSpeedRate, IsSetBindSpeed, IsIgnoreObject, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BindNodeName0 = BindNodeName0
		self.BindNodeName1 = BindNodeName1
		self.BindOffset0 = BindOffset0
		self.BindOffset1 = BindOffset1
		self.BindOffset2 = BindOffset2
		self.ReflectAtkPower = ReflectAtkPower
		self.BindOffset3 = BindOffset3
		self.BindOffset4 = BindOffset4
		self.BindOffset5 = BindOffset5
		self.BindOffset6 = BindOffset6
		self.BindOffset7 = BindOffset7
		self.BindOffset8 = BindOffset8
		self.ChaseAngleMin = ChaseAngleMin
		self.ChaseParentNode = ChaseParentNode
		self.RotateSpeed = RotateSpeed
		self.RotateSpeedAtHit = RotateSpeedAtHit
		self.RotateSpeedAtFall = RotateSpeedAtFall
		self.IsForceDelete = IsForceDelete
		self.ExplosionTime = ExplosionTime
		self.ChaseAngleLimit = ChaseAngleLimit
		self.BindNodeName = BindNodeName
		self.IsAdjustHeight = IsAdjustHeight
		self.IsSetParentSystemGroupHandler = IsSetParentSystemGroupHandler
		self.ReflectSpeedRate = ReflectSpeedRate
		self.IsSetBindSpeed = IsSetBindSpeed
		self.IsIgnoreObject = IsIgnoreObject
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossLswordAttackRoot:
	ChildNames = ["ケミカル付与", "ビーム攻撃", "初回ケミカル付与", "回転斬り", "大火球投げ", "大火球投げカウンター", "待機", "攻撃前待機", "横斬り", "火炎渦", "火球投げ", "火球投げカウンター", "縦斬り"]

	def __init__(self, Name, HighSlashRate, WhirlSlashRate, FireBallRate, CrossSlashRate, ChemicalPlusHPRate, IsFarDist, PatternShiftFirstLifeRate, ReturnWaitCount, ForceApproachCount, TornadoAttackRate, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HighSlashRate = HighSlashRate
		self.WhirlSlashRate = WhirlSlashRate
		self.FireBallRate = FireBallRate
		self.CrossSlashRate = CrossSlashRate
		self.ChemicalPlusHPRate = ChemicalPlusHPRate
		self.IsFarDist = IsFarDist
		self.PatternShiftFirstLifeRate = PatternShiftFirstLifeRate
		self.ReturnWaitCount = ReturnWaitCount
		self.ForceApproachCount = ForceApproachCount
		self.TornadoAttackRate = TornadoAttackRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class SiteBossLswordFireBallRoot:
	ChildNames = ["弾生成", "投げる", "準備"]

	def __init__(self, Name, PredictPosRate, BindPosOffset, IsThrowChildDevice, PosReduceRatio, KeepDistance, MoveSpeed, YOffset, IsNeedCreateChildDevice, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PredictPosRate = PredictPosRate
		self.BindPosOffset = BindPosOffset
		self.IsThrowChildDevice = IsThrowChildDevice
		self.PosReduceRatio = PosReduceRatio
		self.KeepDistance = KeepDistance
		self.MoveSpeed = MoveSpeed
		self.YOffset = YOffset
		self.IsNeedCreateChildDevice = IsNeedCreateChildDevice
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SiteBossLswordRoot:
	ChildNames = ["リアクション", "出現デモ待ち", "出現デモ終了直後", "通常"]

	def __init__(self, Name, FireBallAttackPower, FireBallMinDamage, BigFireBallAttackPower, BigFireBallMinDamage, WearFlameAttackPower, WearFlameMinDamage, BigFireBallScaleTime0, BigFireBallPosOffset, BigFireBallScaleMax, BigFireBallScaleTime1, BigFireBallMoveSpeed0, BigFireBallMoveSpeed1, BigFireBallRotOffset, DemoName, NormalEntryName, AtDownEntryName, DemoPlayHPRate, OffFlagIndexAtClipping, AddAttackPower, IsPlayed_DemoFlagName, ForceRecoverHitMax, ForceRecoverDamageMax, AddForceRecoverHitNum, AddForceRecoverDamage, IsRemainBoss, BlownOffAtWeakPointHitNum, WeakPointDamageRate, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FireBallAttackPower = FireBallAttackPower
		self.FireBallMinDamage = FireBallMinDamage
		self.BigFireBallAttackPower = BigFireBallAttackPower
		self.BigFireBallMinDamage = BigFireBallMinDamage
		self.WearFlameAttackPower = WearFlameAttackPower
		self.WearFlameMinDamage = WearFlameMinDamage
		self.BigFireBallScaleTime0 = BigFireBallScaleTime0
		self.BigFireBallPosOffset = BigFireBallPosOffset
		self.BigFireBallScaleMax = BigFireBallScaleMax
		self.BigFireBallScaleTime1 = BigFireBallScaleTime1
		self.BigFireBallMoveSpeed0 = BigFireBallMoveSpeed0
		self.BigFireBallMoveSpeed1 = BigFireBallMoveSpeed1
		self.BigFireBallRotOffset = BigFireBallRotOffset
		self.DemoName = DemoName
		self.NormalEntryName = NormalEntryName
		self.AtDownEntryName = AtDownEntryName
		self.DemoPlayHPRate = DemoPlayHPRate
		self.OffFlagIndexAtClipping = OffFlagIndexAtClipping
		self.AddAttackPower = AddAttackPower
		self.IsPlayed_DemoFlagName = IsPlayed_DemoFlagName
		self.ForceRecoverHitMax = ForceRecoverHitMax
		self.ForceRecoverDamageMax = ForceRecoverDamageMax
		self.AddForceRecoverHitNum = AddForceRecoverHitNum
		self.AddForceRecoverDamage = AddForceRecoverDamage
		self.IsRemainBoss = IsRemainBoss
		self.BlownOffAtWeakPointHitNum = BlownOffAtWeakPointHitNum
		self.WeakPointDamageRate = WeakPointDamageRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossLswordTornadoRoot:
	ChildNames = ["待機", "放出", "火炎渦開始", "移動"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossNormalRoot:
	ChildNames = ["待機", "攻撃"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SiteBossPierceBulletAttack:
	ChildNames = ["回避", "子機発射", "弾発射", "準備", "溜め", "終了"]

	def __init__(self, Name, ArrowNum, HoldTime, InitHoldTime, ArrowName, IsFinishAtNoDevice, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, AvoidLifeRate, AvoidCountMax, AvoidAngle, AvoidDist, SeqAvoidRate, AvoidDistRand, AvoidWaitCount, AvoidWaitCountRand, ChaseDist, ChaseDistOffset, UpDownAvoidRate, IsKeepDistance, KeepDistance, TrigEventAtHold, SpineControlOffsetAngleLR, SpineControlOffsetAngleUD, ReflectOffset, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.HoldTime = HoldTime
		self.InitHoldTime = InitHoldTime
		self.ArrowName = ArrowName
		self.IsFinishAtNoDevice = IsFinishAtNoDevice
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.AvoidLifeRate = AvoidLifeRate
		self.AvoidCountMax = AvoidCountMax
		self.AvoidAngle = AvoidAngle
		self.AvoidDist = AvoidDist
		self.SeqAvoidRate = SeqAvoidRate
		self.AvoidDistRand = AvoidDistRand
		self.AvoidWaitCount = AvoidWaitCount
		self.AvoidWaitCountRand = AvoidWaitCountRand
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.UpDownAvoidRate = UpDownAvoidRate
		self.IsKeepDistance = IsKeepDistance
		self.KeepDistance = KeepDistance
		self.TrigEventAtHold = TrigEventAtHold
		self.SpineControlOffsetAngleLR = SpineControlOffsetAngleLR
		self.SpineControlOffsetAngleUD = SpineControlOffsetAngleUD
		self.ReflectOffset = ReflectOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class SiteBossReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "デモ待ち大ダメージ", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "特効ダメージ", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, IsChangeEffectiveDamage, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeEffectiveDamage = IsChangeEffectiveDamage
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17


class SiteBossRecognizeRoot:
	ChildNames = ["デモ用ワープ出現", "デモ用ワープ移動", "プレイヤー範囲外ワープ", "ワープ移動", "戦闘", "気付く", "自身範囲外ワープ"]

	def __init__(self, Name, ChaseDist, ChaseDistOffset, IsCheckChildDevice, IgnoreWarpDistRetFromDamage, IgnoreWaprDistMax, WarpStartDist, AttackNum, AttackRandNum, ForceWarpRetryDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.IsCheckChildDevice = IsCheckChildDevice
		self.IgnoreWarpDistRetFromDamage = IgnoreWarpDistRetFromDamage
		self.IgnoreWaprDistMax = IgnoreWaprDistMax
		self.WarpStartDist = WarpStartDist
		self.AttackNum = AttackNum
		self.AttackRandNum = AttackRandNum
		self.ForceWarpRetryDist = ForceWarpRetryDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossReflectArrowRoot:
	ChildNames = ["回避", "子機発射", "弾発射", "準備", "溜め", "終了"]

	def __init__(self, Name, ArrowNum, HoldTime, InitHoldTime, ArrowName, IsFinishAtNoDevice, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, AvoidLifeRate, AvoidCountMax, AvoidAngle, AvoidDist, SeqAvoidRate, AvoidDistRand, AvoidWaitCount, AvoidWaitCountRand, ChaseDist, ChaseDistOffset, UpDownAvoidRate, IsKeepDistance, KeepDistance, TrigEventAtHold, SpineControlOffsetAngleLR, SpineControlOffsetAngleUD, ReflectOffset, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.HoldTime = HoldTime
		self.InitHoldTime = InitHoldTime
		self.ArrowName = ArrowName
		self.IsFinishAtNoDevice = IsFinishAtNoDevice
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.AvoidLifeRate = AvoidLifeRate
		self.AvoidCountMax = AvoidCountMax
		self.AvoidAngle = AvoidAngle
		self.AvoidDist = AvoidDist
		self.SeqAvoidRate = SeqAvoidRate
		self.AvoidDistRand = AvoidDistRand
		self.AvoidWaitCount = AvoidWaitCount
		self.AvoidWaitCountRand = AvoidWaitCountRand
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.UpDownAvoidRate = UpDownAvoidRate
		self.IsKeepDistance = IsKeepDistance
		self.KeepDistance = KeepDistance
		self.TrigEventAtHold = TrigEventAtHold
		self.SpineControlOffsetAngleLR = SpineControlOffsetAngleLR
		self.SpineControlOffsetAngleUD = SpineControlOffsetAngleUD
		self.ReflectOffset = ReflectOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class SiteBossShootArrowRoot:
	ChildNames = ["ビーム攻撃", "反射弾", "回避", "天空弾", "子機生成", "待機", "疾風弾", "竜巻生成", "竜巻複数生成", "通常弾"]

	def __init__(self, Name, ChildDeviceMax, ChildDeviceSupplyNum, PatternShiftFirstLifeRate, PatternShiftSecondLifeRate, PatternShiftThirdLifeRate, ChildDeviceSupplyInterval, NoWaitWarpAttackKey, CancelCreateTornadoHeight, AtMinDamage, ArrowRainBaseDamage, ArrowRainAddDamage, AvoidAngle, AvoidLifeRate, AvoidCountMax, AvoidDist, SeqAvoidRate, AvoidDistRand, AvoidWaitCount, AvoidWaitCountRand, ChaseDist, ChaseDistOffset, UpDownAvoidRate, TornadoCreateHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChildDeviceMax = ChildDeviceMax
		self.ChildDeviceSupplyNum = ChildDeviceSupplyNum
		self.PatternShiftFirstLifeRate = PatternShiftFirstLifeRate
		self.PatternShiftSecondLifeRate = PatternShiftSecondLifeRate
		self.PatternShiftThirdLifeRate = PatternShiftThirdLifeRate
		self.ChildDeviceSupplyInterval = ChildDeviceSupplyInterval
		self.NoWaitWarpAttackKey = NoWaitWarpAttackKey
		self.CancelCreateTornadoHeight = CancelCreateTornadoHeight
		self.AtMinDamage = AtMinDamage
		self.ArrowRainBaseDamage = ArrowRainBaseDamage
		self.ArrowRainAddDamage = ArrowRainAddDamage
		self.AvoidAngle = AvoidAngle
		self.AvoidLifeRate = AvoidLifeRate
		self.AvoidCountMax = AvoidCountMax
		self.AvoidDist = AvoidDist
		self.SeqAvoidRate = SeqAvoidRate
		self.AvoidDistRand = AvoidDistRand
		self.AvoidWaitCount = AvoidWaitCount
		self.AvoidWaitCountRand = AvoidWaitCountRand
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.UpDownAvoidRate = UpDownAvoidRate
		self.TornadoCreateHeight = TornadoCreateHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class SiteBossShootNormalArrowRoot:
	ChildNames = ["回避", "子機発射", "弾発射", "準備", "溜め", "終了"]

	def __init__(self, Name, ArrowNum, HoldTime, InitHoldTime, ArrowName, IsFinishAtNoDevice, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, AvoidLifeRate, AvoidCountMax, AvoidAngle, AvoidDist, SeqAvoidRate, AvoidDistRand, AvoidWaitCount, AvoidWaitCountRand, ChaseDist, ChaseDistOffset, UpDownAvoidRate, IsKeepDistance, KeepDistance, TrigEventAtHold, SpineControlOffsetAngleLR, SpineControlOffsetAngleUD, ReflectOffset, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowNum = ArrowNum
		self.HoldTime = HoldTime
		self.InitHoldTime = InitHoldTime
		self.ArrowName = ArrowName
		self.IsFinishAtNoDevice = IsFinishAtNoDevice
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.AvoidLifeRate = AvoidLifeRate
		self.AvoidCountMax = AvoidCountMax
		self.AvoidAngle = AvoidAngle
		self.AvoidDist = AvoidDist
		self.SeqAvoidRate = SeqAvoidRate
		self.AvoidDistRand = AvoidDistRand
		self.AvoidWaitCount = AvoidWaitCount
		self.AvoidWaitCountRand = AvoidWaitCountRand
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.UpDownAvoidRate = UpDownAvoidRate
		self.IsKeepDistance = IsKeepDistance
		self.KeepDistance = KeepDistance
		self.TrigEventAtHold = TrigEventAtHold
		self.SpineControlOffsetAngleLR = SpineControlOffsetAngleLR
		self.SpineControlOffsetAngleUD = SpineControlOffsetAngleUD
		self.ReflectOffset = ReflectOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class SiteBossSmallDamageRoot:
	ChildNames = ["大ダメージ", "小ダメージ"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SiteBossSpearAttackRoot:
	ChildNames = ["なぎ払い", "ビーム攻撃", "待機", "槍壊れ待機", "槍復活", "槍投げ", "氷弾攻撃", "真下攻撃", "突き", "逃走ワープ"]

	def __init__(self, Name, ReturnWaitCount, BeamPatternChangeHP, FarDistanceAttackRange, NearDistanceAttackRange, VerticalAttackRange, OnIceBlockHeight, IsBowAimedCounterOn, IsIceBulletOn, ThrowSpearRate, BeamRate, IceBulletRate, ChaseDist, ChaseDistOffset, SweepRateAtFar, SweepRateAtNear, WarpAnchorFirstSuffix, WarpAnchorAfterSuffix, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReturnWaitCount = ReturnWaitCount
		self.BeamPatternChangeHP = BeamPatternChangeHP
		self.FarDistanceAttackRange = FarDistanceAttackRange
		self.NearDistanceAttackRange = NearDistanceAttackRange
		self.VerticalAttackRange = VerticalAttackRange
		self.OnIceBlockHeight = OnIceBlockHeight
		self.IsBowAimedCounterOn = IsBowAimedCounterOn
		self.IsIceBulletOn = IsIceBulletOn
		self.ThrowSpearRate = ThrowSpearRate
		self.BeamRate = BeamRate
		self.IceBulletRate = IceBulletRate
		self.ChaseDist = ChaseDist
		self.ChaseDistOffset = ChaseDistOffset
		self.SweepRateAtFar = SweepRateAtFar
		self.SweepRateAtNear = SweepRateAtNear
		self.WarpAnchorFirstSuffix = WarpAnchorFirstSuffix
		self.WarpAnchorAfterSuffix = WarpAnchorAfterSuffix
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class SiteBossSpearLifeSelector:
	ChildNames = ["パターン0", "パターン1", "パターン2", "パターン3", "場所移動0", "場所移動1", "場所移動2", "水位上昇"]

	def __init__(self, Name, PatternChangeLife2, PatternChangeLife3, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PatternChangeLife2 = PatternChangeLife2
		self.PatternChangeLife3 = PatternChangeLife3
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class SiteBossSpearRoot:
	ChildNames = ["リアクション", "出現デモ待ち", "出現デモ終了直後", "通常"]

	def __init__(self, Name, ThrowSpearAttackPower, ThrowSpearMinDmage, IceSplinterAttackPower, IceSplinterMinDamage, DemoName, NormalEntryName, AtDownEntryName, DemoPlayHPRate, OffFlagIndexAtClipping, AddAttackPower, IsPlayed_DemoFlagName, ForceRecoverHitMax, ForceRecoverDamageMax, AddForceRecoverHitNum, AddForceRecoverDamage, IsRemainBoss, BlownOffAtWeakPointHitNum, WeakPointDamageRate, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowSpearAttackPower = ThrowSpearAttackPower
		self.ThrowSpearMinDmage = ThrowSpearMinDmage
		self.IceSplinterAttackPower = IceSplinterAttackPower
		self.IceSplinterMinDamage = IceSplinterMinDamage
		self.DemoName = DemoName
		self.NormalEntryName = NormalEntryName
		self.AtDownEntryName = AtDownEntryName
		self.DemoPlayHPRate = DemoPlayHPRate
		self.OffFlagIndexAtClipping = OffFlagIndexAtClipping
		self.AddAttackPower = AddAttackPower
		self.IsPlayed_DemoFlagName = IsPlayed_DemoFlagName
		self.ForceRecoverHitMax = ForceRecoverHitMax
		self.ForceRecoverDamageMax = ForceRecoverDamageMax
		self.AddForceRecoverHitNum = AddForceRecoverHitNum
		self.AddForceRecoverDamage = AddForceRecoverDamage
		self.IsRemainBoss = IsRemainBoss
		self.BlownOffAtWeakPointHitNum = BlownOffAtWeakPointHitNum
		self.WeakPointDamageRate = WeakPointDamageRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossSpearThrow:
	ChildNames = ["投げる", "生成待ち"]

	def __init__(self, Name, AttackPower, AtMnDamage, AddAttackPower, ThrowActorName, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPower = AttackPower
		self.AtMnDamage = AtMnDamage
		self.AddAttackPower = AddAttackPower
		self.ThrowActorName = ThrowActorName
		self.Child0 = Child0
		self.Child1 = Child1


class SiteBossSwordApproachRoot:
	ChildNames = ["スロー時移動", "移動", "移動開始"]

	def __init__(self, Name, KeepDistance, MoveWidth, IsCloseMove, BaseOffsetY, PredictMoveFrame, IsPlayRunStartAS, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepDistance = KeepDistance
		self.MoveWidth = MoveWidth
		self.IsCloseMove = IsCloseMove
		self.BaseOffsetY = BaseOffsetY
		self.PredictMoveFrame = PredictMoveFrame
		self.IsPlayRunStartAS = IsPlayRunStartAS
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SiteBossSwordAttackRoot:
	ChildNames = ["ケミカル付与", "ビーム攻撃", "待機", "盾回復", "盾突き", "落雷攻撃", "落雷攻撃前移動", "近接攻撃", "近接攻撃2", "近接攻撃3", "退避", "遠距離攻撃"]

	def __init__(self, Name, ChemicalPlusHPRate, CloseAttackRate, ChemicalPlusRate, ShieldRepairTime, FirstAttackHPRate, SecondAttackHPRate, BeamAttackHPRate, DemoName, EntryPointName, ThrowActorName, ThrowAttackPower, AddAttackPower, ThrowMinDamage, ElectricBallScaleTime, ElectricBallScale, ElectricBallRange, ThrowRate, ThrowDist, PillarMax, ElectricCounterMax, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChemicalPlusHPRate = ChemicalPlusHPRate
		self.CloseAttackRate = CloseAttackRate
		self.ChemicalPlusRate = ChemicalPlusRate
		self.ShieldRepairTime = ShieldRepairTime
		self.FirstAttackHPRate = FirstAttackHPRate
		self.SecondAttackHPRate = SecondAttackHPRate
		self.BeamAttackHPRate = BeamAttackHPRate
		self.DemoName = DemoName
		self.EntryPointName = EntryPointName
		self.ThrowActorName = ThrowActorName
		self.ThrowAttackPower = ThrowAttackPower
		self.AddAttackPower = AddAttackPower
		self.ThrowMinDamage = ThrowMinDamage
		self.ElectricBallScaleTime = ElectricBallScaleTime
		self.ElectricBallScale = ElectricBallScale
		self.ElectricBallRange = ElectricBallRange
		self.ThrowRate = ThrowRate
		self.ThrowDist = ThrowDist
		self.PillarMax = PillarMax
		self.ElectricCounterMax = ElectricCounterMax
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SiteBossSwordIronPileRoot:
	ChildNames = ["刺さる", "待機", "消滅", "落下"]

	def __init__(self, Name, FallWaitCount, FallSpeed, SlopeRate, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FallWaitCount = FallWaitCount
		self.FallSpeed = FallSpeed
		self.SlopeRate = SlopeRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossSwordRailApproach:
	ChildNames = ["スロー時移動", "移動", "移動開始"]

	def __init__(self, Name, KeepDistance, MoveWidth, IsCloseMove, BaseOffsetY, PredictMoveFrame, IsPlayRunStartAS, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepDistance = KeepDistance
		self.MoveWidth = MoveWidth
		self.IsCloseMove = IsCloseMove
		self.BaseOffsetY = BaseOffsetY
		self.PredictMoveFrame = PredictMoveFrame
		self.IsPlayRunStartAS = IsPlayRunStartAS
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SiteBossSwordRoot:
	ChildNames = ["リアクション", "出現デモ待ち", "出現デモ終了直後", "通常"]

	def __init__(self, Name, DemoName, NormalEntryName, AtDownEntryName, DemoPlayHPRate, OffFlagIndexAtClipping, AddAttackPower, IsPlayed_DemoFlagName, ForceRecoverHitMax, ForceRecoverDamageMax, AddForceRecoverHitNum, AddForceRecoverDamage, IsRemainBoss, BlownOffAtWeakPointHitNum, WeakPointDamageRate, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DemoName = DemoName
		self.NormalEntryName = NormalEntryName
		self.AtDownEntryName = AtDownEntryName
		self.DemoPlayHPRate = DemoPlayHPRate
		self.OffFlagIndexAtClipping = OffFlagIndexAtClipping
		self.AddAttackPower = AddAttackPower
		self.IsPlayed_DemoFlagName = IsPlayed_DemoFlagName
		self.ForceRecoverHitMax = ForceRecoverHitMax
		self.ForceRecoverDamageMax = ForceRecoverDamageMax
		self.AddForceRecoverHitNum = AddForceRecoverHitNum
		self.AddForceRecoverDamage = AddForceRecoverDamage
		self.IsRemainBoss = IsRemainBoss
		self.BlownOffAtWeakPointHitNum = BlownOffAtWeakPointHitNum
		self.WeakPointDamageRate = WeakPointDamageRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SiteBossSwordSeqThreeAI:
	ChildNames = ["中行動", "先行動", "後行動"]

	def __init__(self, Name, IsSkipLastAction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSkipLastAction = IsSkipLastAction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SiteBossSwordWeapon:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SiteBossThrowIceRoot:
	ChildNames = ["弾生成", "弾発射", "準備", "発射後待機"]

	def __init__(self, Name, ThrowActorName, IgnitionNum, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowActorName = ThrowActorName
		self.IgnitionNum = IgnitionNum
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SleepBedRoot:
	ChildNames = ["Wait"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class SleepSelect:
	ChildNames = ["活動中", "睡眠中"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SnowBallNormal:
	ChildNames = ["壊れる", "所持", "投擲生成", "通常"]

	def __init__(self, Name, ScaleRate, ScaleMax, CarryScaleLimit, SendSignalLinearVelTh, SendSignalScaleTh, ScaleMin, DeleteUnderWaterDepth, MaxImpulseMassRate, AttReturnOnOffset, ScaleIncreaseDistance, ItemDropSetScaleOffset, ItemDropDeleteScaleOffset, MinImpulseRatio, CancelFixedScale, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ScaleRate = ScaleRate
		self.ScaleMax = ScaleMax
		self.CarryScaleLimit = CarryScaleLimit
		self.SendSignalLinearVelTh = SendSignalLinearVelTh
		self.SendSignalScaleTh = SendSignalScaleTh
		self.ScaleMin = ScaleMin
		self.DeleteUnderWaterDepth = DeleteUnderWaterDepth
		self.MaxImpulseMassRate = MaxImpulseMassRate
		self.AttReturnOnOffset = AttReturnOnOffset
		self.ScaleIncreaseDistance = ScaleIncreaseDistance
		self.ItemDropSetScaleOffset = ItemDropSetScaleOffset
		self.ItemDropDeleteScaleOffset = ItemDropDeleteScaleOffset
		self.MinImpulseRatio = MinImpulseRatio
		self.CancelFixedScale = CancelFixedScale
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SnowOctarockBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, VacuumPartsKey, ShootActorKey, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VacuumPartsKey = VacuumPartsKey
		self.ShootActorKey = ShootActorKey
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class SoundTriggerTag:
	ChildNames = ["再生", "待機"]

	def __init__(self, Name, Always, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Always = Always
		self.Child0 = Child0
		self.Child1 = Child1


class SpearWeaponSelect:
	ChildNames = ["槍以外", "槍装備"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SpotBgmTrigger:
	ChildNames = ["再生"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class StalEnemyBlownOff:
	ChildNames = ["ふっとび", "ヘッドショット"]

	def __init__(self, Name, DrownDepth, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DrownDepth = DrownDepth
		self.Child0 = Child0
		self.Child1 = Child1


class StalEnemyChasePart:
	ChildNames = ["パーツがエリア外", "プレイヤ持たれパーツ待機", "持たれパーツ待機", "持たれパーツ追跡", "通常パーツ待機", "通常パーツ追跡"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class StalEnemyDoShootPartSelect:
	ChildNames = ["パーツ投げ", "通常"]

	def __init__(self, Name, ShootRate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootRate = ShootRate
		self.Child0 = Child0
		self.Child1 = Child1


class StalEnemyGrabShootOwnPart:
	ChildNames = ["アゴ掴み", "左腕掴み", "投げる", "肋骨掴み"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class StalEnemyNoHeadWait:
	ChildNames = ["活動者有", "生存者有", "生存者無"]

	def __init__(self, Name, RebootDistance, RebootTimer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RebootDistance = RebootDistance
		self.RebootTimer = RebootTimer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class StalEnemyReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "大落下", "小ダメージ", "崩れ落ち", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15


class StalEnemyRoot:
	ChildNames = ["リアクション", "奈落", "待機", "怒り", "所持", "拾い合体", "朝が来た", "水中", "落下", "通常", "頭部無し"]

	def __init__(self, Name, SearchFrame, InWaterDepth, OutOfWaterOffset, DeadCheckFrame, DeadCount, SpreadDist, SmallSpreadDist, SearchDistXZ, SearchDistY, FallHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchFrame = SearchFrame
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.DeadCheckFrame = DeadCheckFrame
		self.DeadCount = DeadCount
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.SearchDistXZ = SearchDistXZ
		self.SearchDistY = SearchDistY
		self.FallHeight = FallHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class StalEnemySleep:
	ChildNames = ["待機", "横になる", "睡眠", "起き上がる"]

	def __init__(self, Name, UseAwarenessWakeUp, UseNoticeActiveWakeUp, IsAwakenByHearing, IsWaitAfterAwaken, AwakeDelayTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseAwarenessWakeUp = UseAwarenessWakeUp
		self.UseNoticeActiveWakeUp = UseNoticeActiveWakeUp
		self.IsAwakenByHearing = IsAwakenByHearing
		self.IsWaitAfterAwaken = IsWaitAfterAwaken
		self.AwakeDelayTime = AwakeDelayTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class StalGiantEnemyReaction:
	ChildNames = ["ふっとび", "ガード", "ガードブレイク", "ショック", "ジャストガード", "凍結", "右腕大ダメージ", "右足ダメージ", "大落下", "小ダメージ", "崩れ落ち", "左足ダメージ", "弱点ダメージ", "弾かれ", "死亡", "炎上", "痺れ", "突風", "落下", "超ショック"]

	def __init__(self, Name, TgLegL, BgLegL, TgLegR, BgLegR, TgArmR, RightLegArmorSlot, LeftLegArmorSlot, JustGuardTimesMin, JustGuardTimesMax, SmallDamageCancelTimes, InComboSmallDamageNoCancel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Child13, Child14, Child15, Child16, Child17, Child18, Child19, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TgLegL = TgLegL
		self.BgLegL = BgLegL
		self.TgLegR = TgLegR
		self.BgLegR = BgLegR
		self.TgArmR = TgArmR
		self.RightLegArmorSlot = RightLegArmorSlot
		self.LeftLegArmorSlot = LeftLegArmorSlot
		self.JustGuardTimesMin = JustGuardTimesMin
		self.JustGuardTimesMax = JustGuardTimesMax
		self.SmallDamageCancelTimes = SmallDamageCancelTimes
		self.InComboSmallDamageNoCancel = InComboSmallDamageNoCancel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12
		self.Child13 = Child13
		self.Child14 = Child14
		self.Child15 = Child15
		self.Child16 = Child16
		self.Child17 = Child17
		self.Child18 = Child18
		self.Child19 = Child19


class StalGiantEnemyRoot:
	ChildNames = ["リアクション", "奈落", "待機", "怒り", "所持", "拾い合体", "朝が来た", "水中", "落下", "通常", "頭部無し"]

	def __init__(self, Name, ActorNameChin, ActorNameRib1, ActorNameRib2, ActorNameRib3, ActorNameRib4, WeakPointNode0, WeakPointNode1, WeakPointNode2, WeakPointNode3, WeakPointNode4, NecklaceTgtName0, NecklaceTgtName1, NecklaceTgtName2, NecklaceWeaponIdx0, NecklaceWeaponIdx1, NecklaceWeaponIdx2, IsDamageToEnemy, SearchFrame, InWaterDepth, OutOfWaterOffset, DeadCheckFrame, DeadCount, SpreadDist, SmallSpreadDist, SearchDistXZ, SearchDistY, FallHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorNameChin = ActorNameChin
		self.ActorNameRib1 = ActorNameRib1
		self.ActorNameRib2 = ActorNameRib2
		self.ActorNameRib3 = ActorNameRib3
		self.ActorNameRib4 = ActorNameRib4
		self.WeakPointNode0 = WeakPointNode0
		self.WeakPointNode1 = WeakPointNode1
		self.WeakPointNode2 = WeakPointNode2
		self.WeakPointNode3 = WeakPointNode3
		self.WeakPointNode4 = WeakPointNode4
		self.NecklaceTgtName0 = NecklaceTgtName0
		self.NecklaceTgtName1 = NecklaceTgtName1
		self.NecklaceTgtName2 = NecklaceTgtName2
		self.NecklaceWeaponIdx0 = NecklaceWeaponIdx0
		self.NecklaceWeaponIdx1 = NecklaceWeaponIdx1
		self.NecklaceWeaponIdx2 = NecklaceWeaponIdx2
		self.IsDamageToEnemy = IsDamageToEnemy
		self.SearchFrame = SearchFrame
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.DeadCheckFrame = DeadCheckFrame
		self.DeadCount = DeadCount
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.SearchDistXZ = SearchDistXZ
		self.SearchDistY = SearchDistY
		self.FallHeight = FallHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class StalGiantSleepNormal:
	ChildNames = ["崩れる", "崩れ待機", "待機", "組みあがる", "退散"]

	def __init__(self, Name, AwakeDelayTime, IsAwakenByHearing, IsWaitAfterAwaken, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AwakeDelayTime = AwakeDelayTime
		self.IsAwakenByHearing = IsAwakenByHearing
		self.IsWaitAfterAwaken = IsWaitAfterAwaken
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class StalHeadLifted:
	ChildNames = ["待機", "所持", "投擲", "設置", "逃走"]

	def __init__(self, Name, EscapeDir, EscapeSpeed, IsGetItem, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EscapeDir = EscapeDir
		self.EscapeSpeed = EscapeSpeed
		self.IsGetItem = IsGetItem
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class StalHeadPartRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "朝が来た", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class StalPartCatch:
	ChildNames = ["腕拾い", "頭拾い"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class StalPartNormal:
	ChildNames = ["ジャンプ", "待機", "気づき", "移動", "行動禁止"]

	def __init__(self, Name, TerritoryArea, CatchArea, WaitTimer, TgtOffset, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryArea = TerritoryArea
		self.CatchArea = CatchArea
		self.WaitTimer = WaitTimer
		self.TgtOffset = TgtOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class StalPartRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, InvincibleTime, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InvincibleTime = InvincibleTime
		self.Child0 = Child0


class StalPartsHasSelect:
	ChildNames = ["ある", "ない"]

	def __init__(self, Name, PartsID, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsID = PartsID
		self.Child0 = Child0
		self.Child1 = Child1


class Stole:
	ChildNames = ["待機", "開く"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class StoneBall_BRoot:

	def __init__(self, Name, WeaponImpulseAmplifyPower, BombImpulseAmplifyPower, DoubleBombImpulseAmplifyPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponImpulseAmplifyPower = WeaponImpulseAmplifyPower
		self.BombImpulseAmplifyPower = BombImpulseAmplifyPower
		self.DoubleBombImpulseAmplifyPower = DoubleBombImpulseAmplifyPower


class StoneOctarockBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備", "画面外攻撃"]

	def __init__(self, Name, OutScreenDist, OutScreenAttackNum, OutScrnAtkOffset, OutScrnAtkOffsetY, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OutScreenDist = OutScreenDist
		self.OutScreenAttackNum = OutScreenAttackNum
		self.OutScrnAtkOffset = OutScrnAtkOffset
		self.OutScrnAtkOffsetY = OutScrnAtkOffsetY
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class StoneOctarockGuardNearTarget:
	ChildNames = ["ガード待機", "ガード終了", "ガード開始", "通常", "高速ガード開始"]

	def __init__(self, Name, NoticeTerrorLevel, GuardStartAngle, GuardEndAngle, GuardEndTime, WeaponIdx, BaseDist, GuardStartDist, GuardEndDist, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.GuardStartAngle = GuardStartAngle
		self.GuardEndAngle = GuardEndAngle
		self.GuardEndTime = GuardEndTime
		self.WeaponIdx = WeaponIdx
		self.BaseDist = BaseDist
		self.GuardStartDist = GuardStartDist
		self.GuardEndDist = GuardEndDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class StoneOctarockWait:
	ChildNames = ["ガード待機", "ガード終了", "通常", "高速ガード開始"]

	def __init__(self, Name, GuardEndTime, NoticeTerrorLevel, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GuardEndTime = GuardEndTime
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class StoneShootEnemyBattle:
	ChildNames = ["戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, ShootItemName, AttackAngle, RetFrmGrdAtkTimer, RetFrmGrdAtkPrcTimer, RetFrmDmgAtkTimer, GlobalNoAtkTime, GlobalNoAtkTimeRnd, AttackIntervalIntensity, DisplayCheckRadius, IsUpdateNoticeState, IsCheckLineReachable, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootItemName = ShootItemName
		self.AttackAngle = AttackAngle
		self.RetFrmGrdAtkTimer = RetFrmGrdAtkTimer
		self.RetFrmGrdAtkPrcTimer = RetFrmGrdAtkPrcTimer
		self.RetFrmDmgAtkTimer = RetFrmDmgAtkTimer
		self.GlobalNoAtkTime = GlobalNoAtkTime
		self.GlobalNoAtkTimeRnd = GlobalNoAtkTimeRnd
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.DisplayCheckRadius = DisplayCheckRadius
		self.IsUpdateNoticeState = IsUpdateNoticeState
		self.IsCheckLineReachable = IsCheckLineReachable
		self.Child0 = Child0
		self.Child1 = Child1


class StoneStickRoot:
	ChildNames = ["固定", "固定開始", "通常"]

	def __init__(self, Name, FixPoint, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FixPoint = FixPoint
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class StopTimerObserver:
	ChildNames = ["ビタロックオブジェクトあり", "ビタロックオブジェクトなし"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class StraightMove:
	ChildNames = ["移動"]

	def __init__(self, Name, AngleLimit, DistanceMax, DistanceMin, IsRetryMove, RetryAngleMax, RetryAngleMin, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngleLimit = AngleLimit
		self.DistanceMax = DistanceMax
		self.DistanceMin = DistanceMin
		self.IsRetryMove = IsRetryMove
		self.RetryAngleMax = RetryAngleMax
		self.RetryAngleMin = RetryAngleMin
		self.Child0 = Child0


class StunBossReaction:
	ChildNames = ["ガード", "スタン", "ダメージ", "死亡", "特効"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class StunWithDamageReaction:
	ChildNames = ["ダメージ", "気絶"]

	def __init__(self, Name, Timer, ForceEndLifeRatio, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Timer = Timer
		self.ForceEndLifeRatio = ForceEndLifeRatio
		self.Child0 = Child0
		self.Child1 = Child1


class SubsAngleSelect:
	ChildNames = ["角度差大", "角度差小"]

	def __init__(self, Name, SubsAngle, CheckOnce, YRotOnly, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubsAngle = SubsAngle
		self.CheckOnce = CheckOnce
		self.YRotOnly = YRotOnly
		self.Child0 = Child0
		self.Child1 = Child1


class SunAI:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class SunazarashiEscapeMove:
	ChildNames = ["地上逃走", "逃走"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SunazarashiNormal:
	ChildNames = ["ふり向き", "ターゲット通知", "ダメージ逃走", "ロケーター待機", "威嚇", "徘徊", "戦闘", "気づき", "注目", "興味対象発見", "逃走"]

	def __init__(self, Name, IsUseEscapeState, IsPositiveAttacker, IsSearchTarget, IsEmitForceEscapeSignal, IsReceivedForceEscapeSignal, IsCheckSandStorm, ChangeBattleStateRadius, CounterAttackRadius, CounterAttackRate, AddCautionLevelVal, AutoReduceCautionLevelVal, LimitOverReduceCautionLevelVal, AwnRangeScaleWhenAttention, TargetLostTime, AllowRoarRadius, EscapeWaterFlowLimit, NewFoodAddTime, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseEscapeState = IsUseEscapeState
		self.IsPositiveAttacker = IsPositiveAttacker
		self.IsSearchTarget = IsSearchTarget
		self.IsEmitForceEscapeSignal = IsEmitForceEscapeSignal
		self.IsReceivedForceEscapeSignal = IsReceivedForceEscapeSignal
		self.IsCheckSandStorm = IsCheckSandStorm
		self.ChangeBattleStateRadius = ChangeBattleStateRadius
		self.CounterAttackRadius = CounterAttackRadius
		self.CounterAttackRate = CounterAttackRate
		self.AddCautionLevelVal = AddCautionLevelVal
		self.AutoReduceCautionLevelVal = AutoReduceCautionLevelVal
		self.LimitOverReduceCautionLevelVal = LimitOverReduceCautionLevelVal
		self.AwnRangeScaleWhenAttention = AwnRangeScaleWhenAttention
		self.TargetLostTime = TargetLostTime
		self.AllowRoarRadius = AllowRoarRadius
		self.EscapeWaterFlowLimit = EscapeWaterFlowLimit
		self.NewFoodAddTime = NewFoodAddTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class SunazarashiReturn:
	ChildNames = ["強制復帰", "待機", "移動"]

	def __init__(self, Name, IsForceReturnHome, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsForceReturnHome = IsForceReturnHome
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SunazarashiRoot:
	ChildNames = ["びっくり", "スクリプト用", "リアクション", "上機嫌", "所持", "水中行動", "牽引", "砂地復帰", "落下", "衝突", "通常行動", "騎乗中"]

	def __init__(self, Name, StunNoiseLevel, EnableHangAlways, ClashSpeed, ClashAngle, InWaterDepth, IsCheckFreeFall, IsCheckStuckConsiderY, IsUseWeakForcePushOutside, IsEnableEscapeForceEndCheck, EscapeForceEndTime, AfterEscapeForceEndState, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StunNoiseLevel = StunNoiseLevel
		self.EnableHangAlways = EnableHangAlways
		self.ClashSpeed = ClashSpeed
		self.ClashAngle = ClashAngle
		self.InWaterDepth = InWaterDepth
		self.IsCheckFreeFall = IsCheckFreeFall
		self.IsCheckStuckConsiderY = IsCheckStuckConsiderY
		self.IsUseWeakForcePushOutside = IsUseWeakForcePushOutside
		self.IsEnableEscapeForceEndCheck = IsEnableEscapeForceEndCheck
		self.EscapeForceEndTime = EscapeForceEndTime
		self.AfterEscapeForceEndState = AfterEscapeForceEndState
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SunazarashiTowing:
	ChildNames = ["NPCを牽引", "プレイヤーを牽引", "敵を牽引", "牽引終了", "牽引開始"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class SwarmBattle:
	ChildNames = ["上昇失敗", "急上昇", "戦闘攻撃", "戦闘準備"]

	def __init__(self, Name, FailedRiseHeight, RiseFailedMoveDist, AttackIntervalIntensity, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FailedRiseHeight = FailedRiseHeight
		self.RiseFailedMoveDist = RiseFailedMoveDist
		self.AttackIntervalIntensity = AttackIntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwarmEscapeDie:
	ChildNames = ["上昇", "逃走", "集合"]

	def __init__(self, Name, Time, RiseHeight, RiseDist, EndDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.RiseHeight = RiseHeight
		self.RiseDist = RiseDist
		self.EndDist = EndDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SwarmRangeKeepCircleMove:
	ChildNames = ["移動"]

	def __init__(self, Name, BaseDist, OutDist, Speed, UpdateCircleMoveDistance, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseDist = BaseDist
		self.OutDist = OutDist
		self.Speed = Speed
		self.UpdateCircleMoveDistance = UpdateCircleMoveDistance
		self.Child0 = Child0


class SwarmReaction:
	ChildNames = ["ケミカルダメージ", "ビタロック", "死亡", "消滅", "矢ダメージ", "範囲ダメージ", "通常ダメージ"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class SwarmRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, ASName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class SwarmStopTimerEscape:
	ChildNames = ["上昇", "逃走", "集合"]

	def __init__(self, Name, StopActorName, Time, RiseHeight, RiseDist, EndDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopActorName = StopActorName
		self.Time = Time
		self.RiseHeight = RiseHeight
		self.RiseDist = RiseDist
		self.EndDist = EndDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SwimEnemyFindPlayer:
	ChildNames = ["ナビメッシュ無し", "不意討ち", "威嚇", "威嚇帰還", "対象壁つかまり", "対象見張り台", "戦闘", "気づき", "速攻"]

	def __init__(self, Name, IsAbleToLand, NearScaffoldDist, ClimbVmin, ClimbVmax, ClimbHmax, SurpriseAttackPer, SurpriseAttackRange, AttackRange, AttackVMin, AttackVMax, SwiftAttackVMin, SwiftAttackVMax, WeaponIdx, LostTimer, SurpriseAttackTime, SurpriseAttackTimeRand, RerouteTimeMin, RerouteTimeMax, RestreintTime, RetTiredFromTime, RestreintTiredDist, ForceFirstAttackDist, RetForceFirstAttackDist, PathTooLongDist, NoSearchFromTiredDist, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAbleToLand = IsAbleToLand
		self.NearScaffoldDist = NearScaffoldDist
		self.ClimbVmin = ClimbVmin
		self.ClimbVmax = ClimbVmax
		self.ClimbHmax = ClimbHmax
		self.SurpriseAttackPer = SurpriseAttackPer
		self.SurpriseAttackRange = SurpriseAttackRange
		self.AttackRange = AttackRange
		self.AttackVMin = AttackVMin
		self.AttackVMax = AttackVMax
		self.SwiftAttackVMin = SwiftAttackVMin
		self.SwiftAttackVMax = SwiftAttackVMax
		self.WeaponIdx = WeaponIdx
		self.LostTimer = LostTimer
		self.SurpriseAttackTime = SurpriseAttackTime
		self.SurpriseAttackTimeRand = SurpriseAttackTimeRand
		self.RerouteTimeMin = RerouteTimeMin
		self.RerouteTimeMax = RerouteTimeMax
		self.RestreintTime = RestreintTime
		self.RetTiredFromTime = RetTiredFromTime
		self.RestreintTiredDist = RestreintTiredDist
		self.ForceFirstAttackDist = ForceFirstAttackDist
		self.RetForceFirstAttackDist = RetForceFirstAttackDist
		self.PathTooLongDist = PathTooLongDist
		self.NoSearchFromTiredDist = NoSearchFromTiredDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class SwimEnemyNormal:
	ChildNames = ["プレイヤー発見", "不審者発見", "不調仲間発見", "待機", "怒り", "攻撃反応", "気配気づき", "脅威感知", "行動中仲間発見", "見失い", "諦め", "音気づき"]

	def __init__(self, Name, WeaponIdx, TerritoryArea, NpcTerritoryArea, NoPlayerTerritoryArea, SpreadDist, EnlargeAwnRatio, NoticeTerrorLevel, SpeadDist2, HomePosRadius, SoundLostTimer, NoActionReactTimeMin, NoActionReactTimeMax, IsMindDoubtTarget, FortressTag, SubsTerritoryArea, LostExtinguishFireDist, ShortRangeTerritoryArea, CloseRangeTerritoryArea, PressBreakObject, TerritoryHeight, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.TerritoryArea = TerritoryArea
		self.NpcTerritoryArea = NpcTerritoryArea
		self.NoPlayerTerritoryArea = NoPlayerTerritoryArea
		self.SpreadDist = SpreadDist
		self.EnlargeAwnRatio = EnlargeAwnRatio
		self.NoticeTerrorLevel = NoticeTerrorLevel
		self.SpeadDist2 = SpeadDist2
		self.HomePosRadius = HomePosRadius
		self.SoundLostTimer = SoundLostTimer
		self.NoActionReactTimeMin = NoActionReactTimeMin
		self.NoActionReactTimeMax = NoActionReactTimeMax
		self.IsMindDoubtTarget = IsMindDoubtTarget
		self.FortressTag = FortressTag
		self.SubsTerritoryArea = SubsTerritoryArea
		self.LostExtinguishFireDist = LostExtinguishFireDist
		self.ShortRangeTerritoryArea = ShortRangeTerritoryArea
		self.CloseRangeTerritoryArea = CloseRangeTerritoryArea
		self.PressBreakObject = PressBreakObject
		self.TerritoryHeight = TerritoryHeight
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11


class SwimEnemyRoam:
	ChildNames = ["徘徊", "徘徊準備"]

	def __init__(self, Name, RoamRadius, RoamRatio, RoamXRadius, RoamZRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RoamRadius = RoamRadius
		self.RoamRatio = RoamRatio
		self.RoamXRadius = RoamXRadius
		self.RoamZRadius = RoamZRadius
		self.Child0 = Child0
		self.Child1 = Child1


class SwitchDistance:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, OnDis, OffsetDis, ChangeSeq, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnDis = OnDis
		self.OffsetDis = OffsetDis
		self.ChangeSeq = ChangeSeq
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchElectric:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, ElecReq, VolReq, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ElecReq = ElecReq
		self.VolReq = VolReq
		self.Child0 = Child0
		self.Child1 = Child1


class SwitchHit:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, WaitTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchHitOnce:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, WaitTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchLinkTagCheck:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, SignalType, SetEnableJobTimerTiming, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SignalType = SignalType
		self.SetEnableJobTimerTiming = SetEnableJobTimerTiming
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchRightAndWrong:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機", "初回オン"]

	def __init__(self, Name, WaitTime, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class SwitchTimeLag:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SwitchTimeLimited:
	ChildNames = ["オフ", "オン"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class SwitchTimer:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchTorch:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class SwitchWheel:
	ChildNames = ["回転", "待機", "逆回転"]

	def __init__(self, Name, RotateStartRad, RotateEndRad, IsAbleToReverse, ReverseEndRad, ReverseStartRad, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateStartRad = RotateStartRad
		self.RotateEndRad = RotateEndRad
		self.IsAbleToReverse = IsAbleToReverse
		self.ReverseEndRad = ReverseEndRad
		self.ReverseStartRad = ReverseStartRad
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class SwitchWindHit:
	ChildNames = ["オフ", "オフ待機", "オン", "オン待機"]

	def __init__(self, Name, WaitTime, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class TargetAbsolutePos:
	ChildNames = ["行動"]

	def __init__(self, Name, TargetPos, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetPos = TargetPos
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetActorDistanceSelect:
	ChildNames = ["内側", "外側"]

	def __init__(self, Name, BoundaryDistance, OverlapDistance, IsUpdateTarget, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoundaryDistance = BoundaryDistance
		self.OverlapDistance = OverlapDistance
		self.IsUpdateTarget = IsUpdateTarget
		self.Child0 = Child0
		self.Child1 = Child1


class TargetActorGrabAdapter:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class TargetAngerSelect:
	ChildNames = ["対象怒り", "怒り移行", "通常"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TargetAttackAttitudeTgtSelect:
	ChildNames = ["対攻撃", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetBaitTypeSelect:
	ChildNames = ["その他", "虫"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetBeatCheck:
	ChildNames = ["撃破", "未撃破"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetBeatGetDrop:
	ChildNames = ["ドロップ取得", "撃破", "未撃破"]

	def __init__(self, Name, SearchDist, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchDist = SearchDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TargetClimbSelect:
	ChildNames = ["対象よじ登り", "対象通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetDirLRInHideSelect:
	ChildNames = ["右側", "左側"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetDirLRSelect:
	ChildNames = ["右側", "左側"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetDistanceSelect:
	ChildNames = ["内側", "外側"]

	def __init__(self, Name, BoundaryDistance, OverlapDistance, IsUpdateTarget, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoundaryDistance = BoundaryDistance
		self.OverlapDistance = OverlapDistance
		self.IsUpdateTarget = IsUpdateTarget
		self.Child0 = Child0
		self.Child1 = Child1


class TargetDynamicActorPos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetElevationGapSelect:
	ChildNames = ["低い", "高い"]

	def __init__(self, Name, ElvGap, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ElvGap = ElvGap
		self.Child0 = Child0
		self.Child1 = Child1


class TargetExistSelect:
	ChildNames = ["いない", "いる"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetHomeDir:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetHomePos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetHomeRangeSelect:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, IsSelectEveryFrame, FarDist, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class TargetInFanAreaSelect:
	ChildNames = ["エリア内", "エリア外"]

	def __init__(self, Name, NearYMax, NearYMin, FarYMax, FarYMin, XZRange, Angle, Option, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearYMax = NearYMax
		self.NearYMin = NearYMin
		self.FarYMax = FarYMax
		self.FarYMin = FarYMin
		self.XZRange = XZRange
		self.Angle = Angle
		self.Option = Option
		self.Child0 = Child0
		self.Child1 = Child1


class TargetIsEquipItemSelector:
	ChildNames = ["武器族", "非武器族"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetKnockBackBasePos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetLastAttackedPos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetLastAttacker:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetLastAttackerPos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetLastDamagedPos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetLostCheck:
	ChildNames = ["発見行動"]

	def __init__(self, Name, LostTimer, IsLostByScaffold, IsLostByTeached, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostTimer = LostTimer
		self.IsLostByScaffold = IsLostByScaffold
		self.IsLostByTeached = IsLostByTeached
		self.Child0 = Child0


class TargetMyUp:
	ChildNames = ["終了", "行動"]

	def __init__(self, Name, EndHeight, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndHeight = EndHeight
		self.Child0 = Child0
		self.Child1 = Child1


class TargetNPCTypeSelector:
	ChildNames = ["一般", "戦士"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TargetOnMovableNavmeshSelect:
	ChildNames = ["ナビメッシュ内", "ナビメッシュ外"]

	def __init__(self, Name, CheckDist, OnStopCheckDist, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDist = CheckDist
		self.OnStopCheckDist = OnStopCheckDist
		self.Child0 = Child0
		self.Child1 = Child1


class TargetPartsPos:
	ChildNames = ["行動"]

	def __init__(self, Name, PartsName, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsName = PartsName
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPickedItem:
	ChildNames = ["サブボタン", "メインボタン", "消滅", "通常"]

	def __init__(self, Name, CanGetOnBurning, GetAttKeyName, IsControlNoticeDo, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CanGetOnBurning = CanGetOnBurning
		self.GetAttKeyName = GetAttKeyName
		self.IsControlNoticeDo = IsControlNoticeDo
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class TargetPlayerPos:
	ChildNames = ["行動"]

	def __init__(self, Name, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosAnchorOffsetSelf:
	ChildNames = ["行動"]

	def __init__(self, Name, Dist, AnchorName, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.AnchorName = AnchorName
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosAnchorOffsetTarget:
	ChildNames = ["行動"]

	def __init__(self, Name, Dist, AnchorName, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.AnchorName = AnchorName
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosDirLRSelect:
	ChildNames = ["右側", "左側"]

	def __init__(self, Name, IsCheckEveryFrame, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckEveryFrame = IsCheckEveryFrame
		self.Child0 = Child0
		self.Child1 = Child1


class TargetPosDynParamRotFromCtrPos:
	ChildNames = ["行動"]

	def __init__(self, Name, MinDist, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinDist = MinDist
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosLostCheck:
	ChildNames = ["発見行動"]

	def __init__(self, Name, LostVMin, LostVMax, LostTimer, LostRange, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.LostTimer = LostTimer
		self.LostRange = LostRange
		self.Child0 = Child0


class TargetPosOffsetFromMyPos:
	ChildNames = ["行動"]

	def __init__(self, Name, Offset, MinDist, Dir, SideDist, IsRandSide, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Offset = Offset
		self.MinDist = MinDist
		self.Dir = Dir
		self.SideDist = SideDist
		self.IsRandSide = IsRandSide
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosOnNavFaceSelect:
	ChildNames = ["ナビメッシュ上", "ナビメッシュ外"]

	def __init__(self, Name, SearchRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchRadius = SearchRadius
		self.Child0 = Child0
		self.Child1 = Child1


class TargetPosRotFromMyPos:
	ChildNames = ["行動"]

	def __init__(self, Name, Angle, IsRandSign, MinDist, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Angle = Angle
		self.IsRandSign = IsRandSign
		self.MinDist = MinDist
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetPosTracking:
	ChildNames = ["追跡行動"]

	def __init__(self, Name, TrackSpeed, IsStoppedByJustAvoid, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TrackSpeed = TrackSpeed
		self.IsStoppedByJustAvoid = IsStoppedByJustAvoid
		self.Child0 = Child0


class TargetPredictRotSpdTargetPos:
	ChildNames = ["行動"]

	def __init__(self, Name, AddSpeed, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddSpeed = AddSpeed
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetRangeSelect:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, IsXZOnly, IsSelectEveryFrame, FarDist, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsXZOnly = IsXZOnly
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class TargetRepeat:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class TargetStateSelect:
	ChildNames = ["対象泳ぎ", "対象通常", "対象騎乗"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TargetTargetPos:
	ChildNames = ["行動"]

	def __init__(self, Name, AddSpeed, OnEnterOnly, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddSpeed = AddSpeed
		self.OnEnterOnly = OnEnterOnly
		self.Child0 = Child0


class TargetTypeSelector:
	ChildNames = ["対象NPC", "対象それ以外", "対象プレイヤー", "対象獲物"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class TemperatureRandSelect:
	ChildNames = ["行動Ａ", "行動Ｂ"]

	def __init__(self, Name, TemperatureChangeRatio, BaseChangeRatio, useBaseRatioTiming, BaseTemperature, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TemperatureChangeRatio = TemperatureChangeRatio
		self.BaseChangeRatio = BaseChangeRatio
		self.useBaseRatioTiming = useBaseRatioTiming
		self.BaseTemperature = BaseTemperature
		self.Child0 = Child0
		self.Child1 = Child1


class TerminalEnduranceWarpRoot:
	ChildNames = ["Off待機", "On待機", "起動"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TimeControlTagRoot:
	ChildNames = ["False", "True"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TimeredViewWait:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Time, TimeRand, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class TimidityEnemyDrawback:
	ChildNames = ["発狂", "警戒", "逃走"]

	def __init__(self, Name, EscapeDist, LostRange, LostVMin, LostVMax, EscapeDistFromHome, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EscapeDist = EscapeDist
		self.LostRange = LostRange
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.EscapeDistFromHome = EscapeDistFromHome
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TiredDistSelect:
	ChildNames = ["近距離", "遠距離"]

	def __init__(self, Name, IsSelectEveryFrame, FarDist, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSelectEveryFrame = IsSelectEveryFrame
		self.FarDist = FarDist
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class TornadoRoot:
	ChildNames = ["削除", "移動"]

	def __init__(self, Name, IsHitOnlyPlayer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsHitOnlyPlayer = IsHitOnlyPlayer
		self.Child0 = Child0
		self.Child1 = Child1


class TowingPlayer:
	ChildNames = ["ダッシュ", "ブレーキ", "通常"]

	def __init__(self, Name, InterruptDef, CheckPlayerStateDef, MaxSpeed, InitSpeed, AddSpeed, StandardSpeed, KeepMaxTime, StopTowingDef, BrakeDecSpeed, AttFrontRate, SandCheckLength, SandCheckAngle, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InterruptDef = InterruptDef
		self.CheckPlayerStateDef = CheckPlayerStateDef
		self.MaxSpeed = MaxSpeed
		self.InitSpeed = InitSpeed
		self.AddSpeed = AddSpeed
		self.StandardSpeed = StandardSpeed
		self.KeepMaxTime = KeepMaxTime
		self.StopTowingDef = StopTowingDef
		self.BrakeDecSpeed = BrakeDecSpeed
		self.AttFrontRate = AttFrontRate
		self.SandCheckLength = SandCheckLength
		self.SandCheckAngle = SandCheckAngle
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TreasureBox:
	ChildNames = ["オープン待機", "クローズ待機", "壊れる"]

	def __init__(self, Name, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TreasureBoxRoot:
	ChildNames = ["地上", "地中"]

	def __init__(self, Name, InGroundOffsetY, InGroundScale, OnGroundOffsetY, OnGroundScale, JumpPower, DebugDraw, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InGroundOffsetY = InGroundOffsetY
		self.InGroundScale = InGroundScale
		self.OnGroundOffsetY = OnGroundOffsetY
		self.OnGroundScale = OnGroundScale
		self.JumpPower = JumpPower
		self.DebugDraw = DebugDraw
		self.Child0 = Child0
		self.Child1 = Child1


class TreasureSpot:
	ChildNames = ["サブボタン", "メインボタン", "消滅", "通常"]

	def __init__(self, Name, GetAttKeyForGuardian, CanGetOnBurning, GetAttKeyName, IsControlNoticeDo, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GetAttKeyForGuardian = GetAttKeyForGuardian
		self.CanGetOnBurning = CanGetOnBurning
		self.GetAttKeyName = GetAttKeyName
		self.IsControlNoticeDo = IsControlNoticeDo
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class TrgTargetChangeToPlayerSelect:
	ChildNames = ["プレイヤーに変更", "通常"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class TrolleyGrabbedByMagnet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TrolleyOnRail:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TrolleyRoot:
	ChildNames = ["マグネ", "レール走行", "転がり"]

	def __init__(self, Name, NearGoalDist, NearGoalLimitSpd, NearGoalReduceRate, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearGoalDist = NearGoalDist
		self.NearGoalLimitSpd = NearGoalLimitSpd
		self.NearGoalReduceRate = NearGoalReduceRate
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class TurnForLookingAround:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, Angle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Angle = Angle
		self.Child0 = Child0
		self.Child1 = Child1


class TurnPreAction:
	ChildNames = ["ターン", "行動"]

	def __init__(self, Name, TurnStartAngle, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.Child0 = Child0
		self.Child1 = Child1


class TwnObjDlcFlightTrainingTarget:
	ChildNames = ["壊れ", "待機", "復活"]

	def __init__(self, Name, LimitTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitTime = LimitTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class UnarmedEnemyNoiseTarget:
	ChildNames = ["ジャンプ", "回転", "待機", "後退", "怒り", "探す", "武器発見", "直進", "移動", "見まわす", "騒ぐ"]

	def __init__(self, Name, LostTime, LostRange, LostVMin, LostVMax, SearchWeaponDist, WeaponIdx, AbsorpDist, FarDist, RepathTime, SearchBaseWeaponDist, SearchWeaponTargetDist, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostTime = LostTime
		self.LostRange = LostRange
		self.LostVMin = LostVMin
		self.LostVMax = LostVMax
		self.SearchWeaponDist = SearchWeaponDist
		self.WeaponIdx = WeaponIdx
		self.AbsorpDist = AbsorpDist
		self.FarDist = FarDist
		self.RepathTime = RepathTime
		self.SearchBaseWeaponDist = SearchBaseWeaponDist
		self.SearchWeaponTargetDist = SearchWeaponTargetDist
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10


class UnarmedWeaponEquipableEnemyAct:
	ChildNames = ["ジャンプ", "回転", "武器拾い", "武器拾い待ち", "直進", "移動", "見まわす"]

	def __init__(self, Name, EquipItemSearchIdx, RepathTime, SearchDist, SearchAng, IsUseSight, LineReachableWeaponDist, WeaponIdx, ReachTargetArea, TurnStartAng, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EquipItemSearchIdx = EquipItemSearchIdx
		self.RepathTime = RepathTime
		self.SearchDist = SearchDist
		self.SearchAng = SearchAng
		self.IsUseSight = IsUseSight
		self.LineReachableWeaponDist = LineReachableWeaponDist
		self.WeaponIdx = WeaponIdx
		self.ReachTargetArea = ReachTargetArea
		self.TurnStartAng = TurnStartAng
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class UnderWaterDepthSelect:
	ChildNames = ["浅瀬", "深瀬"]

	def __init__(self, Name, DeepDepth, OnEnterOnly, ForceDeepChange, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeepDepth = DeepDepth
		self.OnEnterOnly = OnEnterOnly
		self.ForceDeepChange = ForceDeepChange
		self.Child0 = Child0
		self.Child1 = Child1


class UrbosasFuryDamageSelector:
	ChildNames = ["ウルボザの怒り由来である", "ウルボザの怒り由来でない"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class VacuumedBombDamageSelect:
	ChildNames = ["その他", "体内爆発"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class VehicleSelector:
	ChildNames = ["乗り物である", "乗り物ではない"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ViewChaseSound:
	ChildNames = ["回転", "直線追跡", "見まわし", "追跡"]

	def __init__(self, Name, TurnDir, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnDir = TurnDir
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ViewMove:
	ChildNames = ["回転", "移動"]

	def __init__(self, Name, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ViewWait:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ViewWaitEndWhenAimed:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, BoneName, AimedAngle, BowRange, EndTime, Time, TimeRand, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoneName = BoneName
		self.AimedAngle = AimedAngle
		self.BowRange = BowRange
		self.EndTime = EndTime
		self.Time = Time
		self.TimeRand = TimeRand
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ViewWaitRiskAvoid:
	ChildNames = ["回転", "待機", "後ずさり回避", "横移動回避"]

	def __init__(self, Name, FrontAngle, AvoidFrame, SpaceAngle, SpaceDist, TurnStartAngle, CheckOnce, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FrontAngle = FrontAngle
		self.AvoidFrame = AvoidFrame
		self.SpaceAngle = SpaceAngle
		self.SpaceDist = SpaceDist
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ViewWaitWithFaceView:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, UseSimpleOffset, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseSimpleOffset = UseSimpleOffset
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ViewWaitWithInstDynActor:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TurnStartAngle, CheckOnce, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartAngle = TurnStartAngle
		self.CheckOnce = CheckOnce
		self.Child0 = Child0
		self.Child1 = Child1


class ViewfrustumCheckTagRoot:
	ChildNames = ["False", "True"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WaistRotEnemyArrowAttack:
	ChildNames = ["リロード", "攻撃", "準備"]

	def __init__(self, Name, RandomPredictFrame, WeaponIdx, IntervalIntensity, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RandomPredictFrame = RandomPredictFrame
		self.WeaponIdx = WeaponIdx
		self.IntervalIntensity = IntervalIntensity
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WaitAndFaceLeader:
	ChildNames = ["リーダーを向く", "待機"]

	def __init__(self, Name, TurnThreshold, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnThreshold = TurnThreshold
		self.Child0 = Child0
		self.Child1 = Child1


class WaitForCloseOrWaterSide:
	ChildNames = ["待機", "近づき反応"]

	def __init__(self, Name, DistFromWater, Range, FailRange, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistFromWater = DistFromWater
		self.Range = Range
		self.FailRange = FailRange
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class WaitForTargetClose:
	ChildNames = ["待機", "近づき反応"]

	def __init__(self, Name, Range, FailRange, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Range = Range
		self.FailRange = FailRange
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class WaitNearTarget:
	ChildNames = ["待機", "近づき"]

	def __init__(self, Name, WeaponIdx, BaseDist, StartCloseDistOffset, OutDistOffset, IsCheckLineReachableForClose, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.BaseDist = BaseDist
		self.StartCloseDistOffset = StartCloseDistOffset
		self.OutDistOffset = OutDistOffset
		self.IsCheckLineReachableForClose = IsCheckLineReachableForClose
		self.Child0 = Child0
		self.Child1 = Child1


class WaitNearTargetAwarenessRange:
	ChildNames = ["待機", "近づき"]

	def __init__(self, Name, StartCloseDist, AddAwarenessRangeType, OutDist, EndCloseDist, UseNavMeshRequest, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartCloseDist = StartCloseDist
		self.AddAwarenessRangeType = AddAwarenessRangeType
		self.OutDist = OutDist
		self.EndCloseDist = EndCloseDist
		self.UseNavMeshRequest = UseNavMeshRequest
		self.Child0 = Child0
		self.Child1 = Child1


class WaitPartsSleep:
	ChildNames = ["行動"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class WarpActivateTerminal:
	ChildNames = ["再起動準備", "待機", "起動", "起動後待機"]

	def __init__(self, Name, IsAbleToReboot, DoLimitAngle, IsCheckLimit, IsRejectMsgForRemains, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAbleToReboot = IsAbleToReboot
		self.DoLimitAngle = DoLimitAngle
		self.IsCheckLimit = IsCheckLimit
		self.IsRejectMsgForRemains = IsRejectMsgForRemains
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WarpSafeTagRoot:
	ChildNames = ["Dummy"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class WarpTagRoot:
	ChildNames = ["Dummy"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class WaterFallWithSound:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaterSurface:
	ChildNames = ["待機", "水位変更", "水位戻し"]

	def __init__(self, Name, LinkTagType, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WaterSurface4RemainsLava:
	ChildNames = ["待機", "水位変更", "水位戻し"]

	def __init__(self, Name, LinkTagType, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WeakPointRoot:
	ChildNames = ["リアクション", "通常"]

	def __init__(self, Name, OwnerDamage, IsBreakable, IsSyncDamage, IsShowCriticalEffect, IsNoReaction, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OwnerDamage = OwnerDamage
		self.IsBreakable = IsBreakable
		self.IsSyncDamage = IsSyncDamage
		self.IsShowCriticalEffect = IsShowCriticalEffect
		self.IsNoReaction = IsNoReaction
		self.Child0 = Child0
		self.Child1 = Child1


class WeakStateSelecter:
	ChildNames = ["弱点モード", "通常モード"]

	def __init__(self, Name, IsAlwaysUpdate, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAlwaysUpdate = IsAlwaysUpdate
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponEquipEnemyWakeUp:
	ChildNames = ["武器拾い", "盾拾い", "起きる"]

	def __init__(self, Name, WeaponGetRange, WeaponIdx, ShieldIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponGetRange = WeaponGetRange
		self.WeaponIdx = WeaponIdx
		self.ShieldIdx = ShieldIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WeaponEquipedAI:
	ChildNames = ["抜刀", "納刀"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponHoldSelector:
	ChildNames = ["抜刀", "納刀"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponOnetimeUse:
	ChildNames = ["使用", "抜刀", "納刀"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WeaponPrepareSelect:
	ChildNames = ["完了", "未完"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponRangeKindSelect:
	ChildNames = ["素手", "近接武器", "遠隔武器", "非武器装備"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WeaponRootAI:
	ChildNames = ["Fixed配置", "刺さる", "吊るす", "投げ", "抜ける", "装備", "非装備"]

	def __init__(self, Name, BlinkFrame, FallOutSpeed, LandNoiseLevel, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BlinkFrame = BlinkFrame
		self.FallOutSpeed = FallOutSpeed
		self.LandNoiseLevel = LandNoiseLevel
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class WeaponSelector:
	ChildNames = ["剣盾装備", "剣装備", "大剣装備", "弓装備", "槍装備", "盾装備", "素手"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6


class WeaponSubTypeSelect:
	ChildNames = ["うちわ", "通常武器"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponThrowerSelector:
	ChildNames = ["その他が投げた", "プレイヤが投げた"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponTrueFormSelect:
	ChildNames = ["仮の姿", "真の姿"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WeaponUsageSelect:
	ChildNames = ["素手", "近接軽量武器", "近接重量武器", "遠隔武器"]

	def __init__(self, Name, WeaponIdx, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WeatherReactionCheck:
	ChildNames = ["通常", "雨", "雪"]

	def __init__(self, Name, IsReactionRain, IsReactionSnow, IsReturnNormal, RandTime, IsForceChangeable, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReactionRain = IsReactionRain
		self.IsReactionSnow = IsReactionSnow
		self.IsReturnNormal = IsReturnNormal
		self.RandTime = RandTime
		self.IsForceChangeable = IsForceChangeable
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WetSelect:
	ChildNames = ["乾燥", "濡れ"]

	def __init__(self, Name, WetRateThreashold, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WetRateThreashold = WetRateThreashold
		self.Child0 = Child0
		self.Child1 = Child1


class WildHorseDefWanderAI:
	ChildNames = ["待機", "移動"]

	def __init__(self, Name, ChangeWaitRate, MaxWaitTime, MinWaitTime, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeWaitRate = ChangeWaitRate
		self.MaxWaitTime = MaxWaitTime
		self.MinWaitTime = MinWaitTime
		self.Child0 = Child0
		self.Child1 = Child1


class WillBallAttackLevelSelect:
	ChildNames = ["レベル１", "レベル２"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WillBallFollowAttackWithDynAng:
	ChildNames = ["待機", "追尾"]

	def __init__(self, Name, ImmidiateLightningTime, ImmidiateLightningXZ, ImmidiateLightningY, AmplitudeY, CycleY, DelayTimer, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ImmidiateLightningTime = ImmidiateLightningTime
		self.ImmidiateLightningXZ = ImmidiateLightningXZ
		self.ImmidiateLightningY = ImmidiateLightningY
		self.AmplitudeY = AmplitudeY
		self.CycleY = CycleY
		self.DelayTimer = DelayTimer
		self.Child0 = Child0
		self.Child1 = Child1


class WillBallOperated:
	ChildNames = ["ワープ", "予兆", "待機", "意識途切れ", "持ち上げ", "攻撃", "放物攻撃", "消滅", "落下攻撃"]

	def __init__(self, Name, WarpDist, AttakedChangeDist, IsAttackedTimeAffect, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpDist = WarpDist
		self.AttakedChangeDist = AttakedChangeDist
		self.IsAttackedTimeAffect = IsAttackedTimeAffect
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class WillBallRoot:
	ChildNames = ["待機", "念受信", "落雷"]

	def __init__(self, Name, MagneLightningTime, ImmidiateLightningXZ, ImmidiateLightningY, ImmidiateLightningXZTarget, ImmidiateLightningYTarget, IsExplode, LightningTimeMinimizeDist, MinimizedTime, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MagneLightningTime = MagneLightningTime
		self.ImmidiateLightningXZ = ImmidiateLightningXZ
		self.ImmidiateLightningY = ImmidiateLightningY
		self.ImmidiateLightningXZTarget = ImmidiateLightningXZTarget
		self.ImmidiateLightningYTarget = ImmidiateLightningYTarget
		self.IsExplode = IsExplode
		self.LightningTimeMinimizeDist = LightningTimeMinimizeDist
		self.MinimizedTime = MinimizedTime
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WindBoxPlace:
	ChildNames = ["待機"]

	def __init__(self, Name, Radius, MaxSpeed, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.MaxSpeed = MaxSpeed
		self.Child0 = Child0


class WindGenerator:
	ChildNames = ["待機", "風制御"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WindGeneratorSignal:
	ChildNames = ["待機", "風制御"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class WithoutWeaponArrow:
	ChildNames = ["刺さる", "所持", "爆発", "発射"]

	def __init__(self, Name, Accel, AimSpeed, FallAccel, FallAimSpeed, Gravity, AtRange, AtImpulse, AtImpact, CanReflect, IsReflectToParent, ReflectOffset, RotOffset, IsDelete, AtAttr, IsBreakIceBlock, StickTime, IsAtHitPlayerIgnore, ReflectDamageRate, TransOffset, BindNodeName, IsDeleteAtHit, CallHitSEKey, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Accel = Accel
		self.AimSpeed = AimSpeed
		self.FallAccel = FallAccel
		self.FallAimSpeed = FallAimSpeed
		self.Gravity = Gravity
		self.AtRange = AtRange
		self.AtImpulse = AtImpulse
		self.AtImpact = AtImpact
		self.CanReflect = CanReflect
		self.IsReflectToParent = IsReflectToParent
		self.ReflectOffset = ReflectOffset
		self.RotOffset = RotOffset
		self.IsDelete = IsDelete
		self.AtAttr = AtAttr
		self.IsBreakIceBlock = IsBreakIceBlock
		self.StickTime = StickTime
		self.IsAtHitPlayerIgnore = IsAtHitPlayerIgnore
		self.ReflectDamageRate = ReflectDamageRate
		self.TransOffset = TransOffset
		self.BindNodeName = BindNodeName
		self.IsDeleteAtHit = IsDeleteAtHit
		self.CallHitSEKey = CallHitSEKey
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WizzrobeBlownOff:
	ChildNames = ["ふっとび", "チャンスタイム", "チャンス凍結", "チャンス起き上がり", "凍結", "水死", "起き上がり", "起き上がり凍結"]

	def __init__(self, Name, IsForceGetUp, DrownDepth, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsForceGetUp = IsForceGetUp
		self.DrownDepth = DrownDepth
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class WizzrobeCircleMove:
	ChildNames = ["移動", "近づき", "遠ざかり"]

	def __init__(self, Name, IsAttCentral, FinRadius, RadiusTimer, EndTimer, Radius, RadiusMargin, Speed, Direction, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAttCentral = IsAttCentral
		self.FinRadius = FinRadius
		self.RadiusTimer = RadiusTimer
		self.EndTimer = EndTimer
		self.Radius = Radius
		self.RadiusMargin = RadiusMargin
		self.Speed = Speed
		self.Direction = Direction
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WizzrobeCombat:
	ChildNames = ["召喚魔法", "天候魔法", "攻撃魔法", "武器攻撃", "移動"]

	def __init__(self, Name, WeatherMagicRate, SummonRate, AttackLength, SummonBufferKey, SummonBufferSize, HeightOffset, MaxHeightLevel, TargetOffset, SummonCount, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeatherMagicRate = WeatherMagicRate
		self.SummonRate = SummonRate
		self.AttackLength = AttackLength
		self.SummonBufferKey = SummonBufferKey
		self.SummonBufferSize = SummonBufferSize
		self.HeightOffset = HeightOffset
		self.MaxHeightLevel = MaxHeightLevel
		self.TargetOffset = TargetOffset
		self.SummonCount = SummonCount
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class WizzrobeCombatMove:
	ChildNames = ["上昇隠れ", "中行動", "消える", "現れる"]

	def __init__(self, Name, DistY, RetryLength, MoveCountMin, MoveCountMax, MaxDistXZ, MinDistXZ, EscapeLength, IgnoreHideActionASName, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistY = DistY
		self.RetryLength = RetryLength
		self.MoveCountMin = MoveCountMin
		self.MoveCountMax = MoveCountMax
		self.MaxDistXZ = MaxDistXZ
		self.MinDistXZ = MinDistXZ
		self.EscapeLength = EscapeLength
		self.IgnoreHideActionASName = IgnoreHideActionASName
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WizzrobeFindPlayer:
	ChildNames = ["戦闘", "気づき"]

	def __init__(self, Name, HomeTerritoryWidth, HomeTerritoryHeight, BattleTerritoryWidth, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HomeTerritoryWidth = HomeTerritoryWidth
		self.HomeTerritoryHeight = HomeTerritoryHeight
		self.BattleTerritoryWidth = BattleTerritoryWidth
		self.Child0 = Child0
		self.Child1 = Child1


class WizzrobeRoam:
	ChildNames = ["移動", "高度変化"]

	def __init__(self, Name, TerritoryRadius, TerritoryRadiusRnd, RetryLength, MoveCountMin, MoveCountMax, ChangeHeightPer, MexHeightLevel, HeightOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TerritoryRadius = TerritoryRadius
		self.TerritoryRadiusRnd = TerritoryRadiusRnd
		self.RetryLength = RetryLength
		self.MoveCountMin = MoveCountMin
		self.MoveCountMax = MoveCountMax
		self.ChangeHeightPer = ChangeHeightPer
		self.MexHeightLevel = MexHeightLevel
		self.HeightOffset = HeightOffset
		self.Child0 = Child0
		self.Child1 = Child1


class WizzrobeRoot:
	ChildNames = ["リアクション", "呼ばれ", "奈落", "所持", "死亡生成", "水中", "落下", "近接湧出", "通常", "騎乗"]

	def __init__(self, Name, MagicTargetIdx, StartASName, StopASName, InWaterDepth, OutOfWaterOffset, SpreadDist, SmallSpreadDist, FortressTag, FallHeight, IgnoreHell, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MagicTargetIdx = MagicTargetIdx
		self.StartASName = StartASName
		self.StopASName = StopASName
		self.InWaterDepth = InWaterDepth
		self.OutOfWaterOffset = OutOfWaterOffset
		self.SpreadDist = SpreadDist
		self.SmallSpreadDist = SmallSpreadDist
		self.FortressTag = FortressTag
		self.FallHeight = FallHeight
		self.IgnoreHell = IgnoreHell
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9


class WizzrobeWeatherMagic:
	ChildNames = ["準備", "発動", "詠唱"]

	def __init__(self, Name, RiseLength, Timer, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RiseLength = RiseLength
		self.Timer = Timer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WolfLinkAmiibo:
	ChildNames = ["ワープ", "登録"]

	def __init__(self, Name, AreaThreshold, AreaSearchRadius, AreaSearchCharacterRadius, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AreaThreshold = AreaThreshold
		self.AreaSearchRadius = AreaSearchRadius
		self.AreaSearchCharacterRadius = AreaSearchCharacterRadius
		self.Child0 = Child0
		self.Child1 = Child1


class WolfLinkBattleRoot:
	ChildNames = ["ダメージ後", "戦闘攻撃できない", "戦闘攻撃対地", "戦闘準備", "戦闘見失う", "戦闘連鎖攻撃"]

	def __init__(self, Name, AttackIntiationRange, UseChainAttack, ChanceToBarkOnAttackFail, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackIntiationRange = AttackIntiationRange
		self.UseChainAttack = UseChainAttack
		self.ChanceToBarkOnAttackFail = ChanceToBarkOnAttackFail
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class WolfLinkChainAttack:
	ChildNames = ["ターゲットを向く", "攻撃", "攻撃前", "攻撃後", "距離を縮む"]

	def __init__(self, Name, IsInvincible, IsIncrementHitOnMiss, NumAttacks, AnimalUnitRate, BeginEndAnimASPlayRate, TurnAnimPlayRate, AttackAnimPlayRate, AttackAnimMinDistance, AttackDistanceOffset, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsInvincible = IsInvincible
		self.IsIncrementHitOnMiss = IsIncrementHitOnMiss
		self.NumAttacks = NumAttacks
		self.AnimalUnitRate = AnimalUnitRate
		self.BeginEndAnimASPlayRate = BeginEndAnimASPlayRate
		self.TurnAnimPlayRate = TurnAnimPlayRate
		self.AttackAnimPlayRate = AttackAnimPlayRate
		self.AttackAnimMinDistance = AttackAnimMinDistance
		self.AttackDistanceOffset = AttackDistanceOffset
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class WolfLinkFollowPlayerRoot:
	ChildNames = ["うろうろする", "崖である", "追いかける(近い)", "追いかける(遠い)"]

	def __init__(self, Name, LateralDistance, AnteriorDistanceStop, AnteriorDistanceRun, AnteriorDistanceSprint, DistanceSuccessEnd, DistanceMovingToward, DistanceRequestingPath, DistanceGivingUp, DistanceThresholdCry, DistanceCheckAvoidance, TargetVelocitySuccessEnd, UpdateTargetPosFrames, UpdateTargetPosFramesNear, SuccessEndDelays, SelfPositionOffsetLocal, SideDistance, TargetVelocityDistanceSec, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, CanIgnorePlayer, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LateralDistance = LateralDistance
		self.AnteriorDistanceStop = AnteriorDistanceStop
		self.AnteriorDistanceRun = AnteriorDistanceRun
		self.AnteriorDistanceSprint = AnteriorDistanceSprint
		self.DistanceSuccessEnd = DistanceSuccessEnd
		self.DistanceMovingToward = DistanceMovingToward
		self.DistanceRequestingPath = DistanceRequestingPath
		self.DistanceGivingUp = DistanceGivingUp
		self.DistanceThresholdCry = DistanceThresholdCry
		self.DistanceCheckAvoidance = DistanceCheckAvoidance
		self.TargetVelocitySuccessEnd = TargetVelocitySuccessEnd
		self.UpdateTargetPosFrames = UpdateTargetPosFrames
		self.UpdateTargetPosFramesNear = UpdateTargetPosFramesNear
		self.SuccessEndDelays = SuccessEndDelays
		self.SelfPositionOffsetLocal = SelfPositionOffsetLocal
		self.SideDistance = SideDistance
		self.TargetVelocityDistanceSec = TargetVelocityDistanceSec
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.CanIgnorePlayer = CanIgnorePlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WolfLinkFollowWait:
	ChildNames = ["回転", "待機"]

	def __init__(self, Name, TurnThreshold, LockonTurnThreshold, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnThreshold = TurnThreshold
		self.LockonTurnThreshold = LockonTurnThreshold
		self.Child0 = Child0
		self.Child1 = Child1


class WolfLinkGoToTarget:
	ChildNames = ["うろうろする", "崖である", "追いかける(近い)", "追いかける(遠い)"]

	def __init__(self, Name, DistanceSuccessEnd, DistanceMovingToward, DistanceRequestingPath, DistanceGivingUp, DistanceThresholdCry, DistanceCheckAvoidance, TargetVelocitySuccessEnd, UpdateTargetPosFrames, UpdateTargetPosFramesNear, SuccessEndDelays, SelfPositionOffsetLocal, SideDistance, TargetVelocityDistanceSec, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, CanIgnorePlayer, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceSuccessEnd = DistanceSuccessEnd
		self.DistanceMovingToward = DistanceMovingToward
		self.DistanceRequestingPath = DistanceRequestingPath
		self.DistanceGivingUp = DistanceGivingUp
		self.DistanceThresholdCry = DistanceThresholdCry
		self.DistanceCheckAvoidance = DistanceCheckAvoidance
		self.TargetVelocitySuccessEnd = TargetVelocitySuccessEnd
		self.UpdateTargetPosFrames = UpdateTargetPosFrames
		self.UpdateTargetPosFramesNear = UpdateTargetPosFramesNear
		self.SuccessEndDelays = SuccessEndDelays
		self.SelfPositionOffsetLocal = SelfPositionOffsetLocal
		self.SideDistance = SideDistance
		self.TargetVelocityDistanceSec = TargetVelocityDistanceSec
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.CanIgnorePlayer = CanIgnorePlayer
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class WolfLinkLeadToTarget:
	ChildNames = ["待機", "誘導", "誘導(騎乗)"]

	def __init__(self, Name, SuccessRadius, WaitDistance, ResumeLeadDistance, OkPathFailRange, DontWaitIfLeaderIsAhead, WaitFramesAfterArrive, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SuccessRadius = SuccessRadius
		self.WaitDistance = WaitDistance
		self.ResumeLeadDistance = ResumeLeadDistance
		self.OkPathFailRange = OkPathFailRange
		self.DontWaitIfLeaderIsAhead = DontWaitIfLeaderIsAhead
		self.WaitFramesAfterArrive = WaitFramesAfterArrive
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class WolfLinkNormalRoot:
	ChildNames = ["シークセンサー", "プレイヤーパス待機", "ワープ", "回復", "待機", "待機命令", "戦闘", "気づき", "気づき戦闘", "狩り", "追従", "追従リトライ", "遠吠え"]

	def __init__(self, Name, ShiekSensorLeadDistance, ShiekSensorGoalTolerance, ShiekSensorTargetFowardOffset, BattleAggressionRange, HowlAtEnemyRange, UtilityWantsToHunt, WarpToPlayerDistance, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Child9, Child10, Child11, Child12, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShiekSensorLeadDistance = ShiekSensorLeadDistance
		self.ShiekSensorGoalTolerance = ShiekSensorGoalTolerance
		self.ShiekSensorTargetFowardOffset = ShiekSensorTargetFowardOffset
		self.BattleAggressionRange = BattleAggressionRange
		self.HowlAtEnemyRange = HowlAtEnemyRange
		self.UtilityWantsToHunt = UtilityWantsToHunt
		self.WarpToPlayerDistance = WarpToPlayerDistance
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8
		self.Child9 = Child9
		self.Child10 = Child10
		self.Child11 = Child11
		self.Child12 = Child12


class WolfLinkReaction:
	ChildNames = ["凍結", "大ダメージ", "小ダメージ", "死亡", "気絶", "消滅", "炎上", "痺れ", "突風"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Child8, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7
		self.Child8 = Child8


class WolfLinkRoot:
	ChildNames = ["スクリプト用", "リアクション", "出現", "水中行動", "通常行動"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class WolfLinkRushAttack:
	ChildNames = ["失敗", "突進"]

	def __init__(self, Name, AttackPosOffsetLength, AllowUpdateTimerLength, CheckSafeGround, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPosOffsetLength = AttackPosOffsetLength
		self.AllowUpdateTimerLength = AllowUpdateTimerLength
		self.CheckSafeGround = CheckSafeGround
		self.Child0 = Child0
		self.Child1 = Child1


class WolfLinkSeqAttack:
	ChildNames = ["ミス", "崖である", "攻撃", "攻撃前", "距離を縮める"]

	def __init__(self, Name, DistBeginAttackAnimation, AngleReqBeginAttackAnimationMin, AngleReqBeginAttackAnimationMax, PlayOnMissAI, ChargeChainAttackOnHit, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistBeginAttackAnimation = DistBeginAttackAnimation
		self.AngleReqBeginAttackAnimationMin = AngleReqBeginAttackAnimationMin
		self.AngleReqBeginAttackAnimationMax = AngleReqBeginAttackAnimationMax
		self.PlayOnMissAI = PlayOnMissAI
		self.ChargeChainAttackOnHit = ChargeChainAttackOnHit
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class WolfLinkShiekSensorRoot:
	ChildNames = ["誘導"]

	def __init__(self, Name, DistanceUntilUpdateTarget, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceUntilUpdateTarget = DistanceUntilUpdateTarget
		self.Child0 = Child0


class WolfLinkWarp:
	ChildNames = ["ワープ", "ワープ前", "ワープ後", "ワープ開始"]

	def __init__(self, Name, TransitFrames, NumCalcPerFrame, FramesUntilFail, WarpFromPlayerOffset, InitialAngle, AreaSearchRadius, AreaSearchCharacterRadius, AreaThreshold, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TransitFrames = TransitFrames
		self.NumCalcPerFrame = NumCalcPerFrame
		self.FramesUntilFail = FramesUntilFail
		self.WarpFromPlayerOffset = WarpFromPlayerOffset
		self.InitialAngle = InitialAngle
		self.AreaSearchRadius = AreaSearchRadius
		self.AreaSearchCharacterRadius = AreaSearchCharacterRadius
		self.AreaThreshold = AreaThreshold
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class YunBoCannon:
	ChildNames = ["ユン坊離脱", "待機", "発射", "装填口開放", "装填完了", "装填完了後ユン坊離脱"]

	def __init__(self, Name, ReturnAnchorName, ActName, Offset, ShotNodeName, IsDrawDebug, RotRadAccel, RotBrake, IsUseShotNodeAngle, ShotCannonBallScale, Child0, Child1, Child2, Child3, Child4, Child5, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReturnAnchorName = ReturnAnchorName
		self.ActName = ActName
		self.Offset = Offset
		self.ShotNodeName = ShotNodeName
		self.IsDrawDebug = IsDrawDebug
		self.RotRadAccel = RotRadAccel
		self.RotBrake = RotBrake
		self.IsUseShotNodeAngle = IsUseShotNodeAngle
		self.ShotCannonBallScale = ShotCannonBallScale
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5


class YunBoCannonBallRoot:
	ChildNames = ["通常"]

	def __init__(self, Name, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0


class ZokuchoSunazarashi:
	ChildNames = ["ナビメッシュ移動", "停止", "待機", "移動"]

	def __init__(self, Name, PlayerLostDis, LeadPlayerAngle, MoveTargetDist, StopMoveDist, StayAwayDist, Child0, Child1, Child2, Child3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerLostDis = PlayerLostDis
		self.LeadPlayerAngle = LeadPlayerAngle
		self.MoveTargetDist = MoveTargetDist
		self.StopMoveDist = StopMoveDist
		self.StayAwayDist = StayAwayDist
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3


class ZoraHeroRelicBattleNormal:
	ChildNames = ["エリア外待機", "エリア外移動", "プレイヤ上空", "プレイヤ水中", "プレイヤ発見", "周回", "待機", "水中ワープ"]

	def __init__(self, Name, WarpDistanceXZ, NearPlayerDistanceXZ, Child0, Child1, Child2, Child3, Child4, Child5, Child6, Child7, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpDistanceXZ = WarpDistanceXZ
		self.NearPlayerDistanceXZ = NearPlayerDistanceXZ
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4
		self.Child5 = Child5
		self.Child6 = Child6
		self.Child7 = Child7


class ZoraHeroRelicBattleRidePlayer:
	ChildNames = ["周回", "待機", "滝つぼ待機", "跳ねあげる", "遺物に向かう"]

	def __init__(self, Name, Child0, Child1, Child2, Child3, Child4, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2
		self.Child3 = Child3
		self.Child4 = Child4


class ZoraHeroRelicBattleRoot:
	ChildNames = ["騎乗中", "騎乗待ち"]

	def __init__(self, Name, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Child0 = Child0
		self.Child1 = Child1


class ZoraHeroSoulGiftRoot:
	ChildNames = ["待機", "発動", "退場"]

	def __init__(self, Name, PosOffset, RotOffset, UseInitMtxForBasePos, UseInitMtxForBaseRot, Child0, Child1, Child2, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosOffset = PosOffset
		self.RotOffset = RotOffset
		self.UseInitMtxForBasePos = UseInitMtxForBasePos
		self.UseInitMtxForBaseRot = UseInitMtxForBaseRot
		self.Child0 = Child0
		self.Child1 = Child1
		self.Child2 = Child2


class ZoraHeroWarp2Player:
	ChildNames = ["でてくる", "もぐる"]

	def __init__(self, Name, DepthOffset, Child0, Child1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DepthOffset = DepthOffset
		self.Child0 = Child0
		self.Child1 = Child1


class addNoiseToTargetPos:
	ChildNames = ["行動"]

	def __init__(self, Name, RandYMin, RandYMax, RandLeftMax, RandRightMax, RandDistMin, RandDistMax, IsUpdateEveryFrame, Child0, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RandYMin = RandYMin
		self.RandYMax = RandYMax
		self.RandLeftMax = RandLeftMax
		self.RandRightMax = RandRightMax
		self.RandDistMin = RandDistMin
		self.RandDistMax = RandDistMax
		self.IsUpdateEveryFrame = IsUpdateEveryFrame
		self.Child0 = Child0


