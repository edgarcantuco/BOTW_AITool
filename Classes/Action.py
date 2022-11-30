class AIScheduleAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ASPlaySimpleAnmDriven:

	def __init__(self, Name, ASName, IsIgnoreSame, IsChangeable, ResetTransBoneOnLeave, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.IsChangeable = IsChangeable
		self.ResetTransBoneOnLeave = ResetTransBoneOnLeave


class ActivateAttackSensor:

	def __init__(self, Name, IsSuccessFinishCounterEnd, IsChangeable, UseMapUnitParamForDamage, AtkSensorName, FramesActive, AtDamage, AtPower, AtPowerReduce, AtImpact, AtShieldBreakPower, AtType, AtAttr, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSuccessFinishCounterEnd = IsSuccessFinishCounterEnd
		self.IsChangeable = IsChangeable
		self.UseMapUnitParamForDamage = UseMapUnitParamForDamage
		self.AtkSensorName = AtkSensorName
		self.FramesActive = FramesActive
		self.AtDamage = AtDamage
		self.AtPower = AtPower
		self.AtPowerReduce = AtPowerReduce
		self.AtImpact = AtImpact
		self.AtShieldBreakPower = AtShieldBreakPower
		self.AtType = AtType
		self.AtAttr = AtAttr
		self.AtDirType = AtDirType


class ActorInfoToGameDataFloat:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ActorInfoToGameDataInt:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ActorInfoToGameDataVec3:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AddAutoPlacementCreator:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AddNoUseTerritoryCounter:

	def __init__(self, Name, Counter, CamDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Counter = Counter
		self.CamDist = CamDist


class AddRigidBody:

	def __init__(self, Name, ResetLayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ResetLayer = ResetLayer


class AdvanceTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AirOctaFloat:

	def __init__(self, Name, Amplitude, GoalDistance, GoalInSuccessEnd, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Amplitude = Amplitude
		self.GoalDistance = GoalDistance
		self.GoalInSuccessEnd = GoalInSuccessEnd


class AirOctaMgr:

	def __init__(self, Name, LeaveDistance, LeaveDownY, onGraundEscapeDist, PlayerLostTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LeaveDistance = LeaveDistance
		self.LeaveDownY = LeaveDownY
		self.onGraundEscapeDist = onGraundEscapeDist
		self.PlayerLostTime = PlayerLostTime


class AirOctaNoticeTurn:

	def __init__(self, Name, NoDoubleNoticeTime, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoDoubleNoticeTime = NoDoubleNoticeTime
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class AirOctaReactionKorog:

	def __init__(self, Name, Speed, AS, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.AS = AS
		self.EndState = EndState


class AirOctaWoodBridge:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AirWallAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AirWallCurseGanon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AirWallHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AlarmLynelTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AlertNearbyEnemies:

	def __init__(self, Name, AlertRange, AlertTime, UseNoise, NoiseLevel, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AlertRange = AlertRange
		self.AlertTime = AlertTime
		self.UseNoise = UseNoise
		self.NoiseLevel = NoiseLevel
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AmbushThrown:

	def __init__(self, Name, ReactionLevel, FinishWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactionLevel = ReactionLevel
		self.FinishWaterDepth = FinishWaterDepth


class AnchorSummon:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class Angry:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AnimMatrixDriven:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AnimTimingAttackMove:

	def __init__(self, Name, ASName, IsRound, JumpHeight, MaxSpeed, RigidBodyName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsRound = IsRound
		self.JumpHeight = JumpHeight
		self.MaxSpeed = MaxSpeed
		self.RigidBodyName = RigidBodyName


class AnimalASPlayCheckMoveDir:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AnimalASPlayWithLegTurn:

	def __init__(self, Name, RotSpeed, RotAccRatio, RotRatio, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.RotAccRatio = RotAccRatio
		self.RotRatio = RotRatio
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AnimalEatAction:

	def __init__(self, Name, MinFramesPlayWaitAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinFramesPlayWaitAS = MinFramesPlayWaitAS


class AnimalElectricParalysis:

	def __init__(self, Name, PauseDelayFrames, ASName, ThrowOffAttackRigidBodyName, CanRiddenWhenLeave, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PauseDelayFrames = PauseDelayFrames
		self.ASName = ASName
		self.ThrowOffAttackRigidBodyName = ThrowOffAttackRigidBodyName
		self.CanRiddenWhenLeave = CanRiddenWhenLeave
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AnimalFollow:

	def __init__(self, Name, DistanceKept, UseGearType, WaitDistanceToLeader, Gear1DistanceToLeader, Gear2DistanceToLeader, Gear3DistanceToLeader, DistanceFactorAtGearDown, WaitDistanceIncreaseDistance, WaitDistanceIncreasePerFrame, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnDistance, IsEndAtAutoStop, UseMinRadius, DesiredDirAngleDeltaSecMax, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, NavMeshCharacterRadiusScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceKept = DistanceKept
		self.UseGearType = UseGearType
		self.WaitDistanceToLeader = WaitDistanceToLeader
		self.Gear1DistanceToLeader = Gear1DistanceToLeader
		self.Gear2DistanceToLeader = Gear2DistanceToLeader
		self.Gear3DistanceToLeader = Gear3DistanceToLeader
		self.DistanceFactorAtGearDown = DistanceFactorAtGearDown
		self.WaitDistanceIncreaseDistance = WaitDistanceIncreaseDistance
		self.WaitDistanceIncreasePerFrame = WaitDistanceIncreasePerFrame
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnDistance = AutoStopAndTurnDistance
		self.IsEndAtAutoStop = IsEndAtAutoStop
		self.UseMinRadius = UseMinRadius
		self.DesiredDirAngleDeltaSecMax = DesiredDirAngleDeltaSecMax
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.NavMeshCharacterRadiusScale = NavMeshCharacterRadiusScale


class AnimalFreeze:

	def __init__(self, Name, PauseDelayFrames, ASName, ThrowOffAttackRigidBodyName, CanRiddenWhenLeave, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PauseDelayFrames = PauseDelayFrames
		self.ASName = ASName
		self.ThrowOffAttackRigidBodyName = ThrowOffAttackRigidBodyName
		self.CanRiddenWhenLeave = CanRiddenWhenLeave
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AnimalLegTurnAutoSpeed:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AnimalMove:

	def __init__(self, Name, FinRadius, WeaponIdx, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance


class AnimalMoveStraightTimed:

	def __init__(self, Name, FramesUntilFinish, IsFinishOnLOSCheckFail, LOSCheckTimeAhead, UseDesiredMoveDir, MinUseGear, MaxUseGear, UseGearType, IsAutoGearDownEnabled, MinGearAtAutoGearDown, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FramesUntilFinish = FramesUntilFinish
		self.IsFinishOnLOSCheckFail = IsFinishOnLOSCheckFail
		self.LOSCheckTimeAhead = LOSCheckTimeAhead
		self.UseDesiredMoveDir = UseDesiredMoveDir
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown


class AnimalNavMeshMove:

	def __init__(self, Name, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnMode, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, WaitUntilPathSucceeded, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnMode = AutoStopAndTurnMode
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.WaitUntilPathSucceeded = WaitUntilPathSucceeded


class AnimalNoCheckMove:

	def __init__(self, Name, FinRadius, WeaponIdx, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance


class AnimalPlayASAndKeepOnGround:

	def __init__(self, Name, DownImpulseScale, IsUseDownImpulse, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DownImpulseScale = DownImpulseScale
		self.IsUseDownImpulse = IsUseDownImpulse
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AnimalStop:

	def __init__(self, Name, IsFixAxisY, UseGearType, SmoothStopFrames, SmoothStopFramesGear3, MinFramesGear1, IsCourbetteEnabled, IsLight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFixAxisY = IsFixAxisY
		self.UseGearType = UseGearType
		self.SmoothStopFrames = SmoothStopFrames
		self.SmoothStopFramesGear3 = SmoothStopFramesGear3
		self.MinFramesGear1 = MinFramesGear1
		self.IsCourbetteEnabled = IsCourbetteEnabled
		self.IsLight = IsLight


class AnimalTurn:

	def __init__(self, Name, AnimPlayRate, FinishAngleRange, RotateAngleMax, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimPlayRate = AnimPlayRate
		self.FinishAngleRange = FinishAngleRange
		self.RotateAngleMax = RotateAngleMax
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class AnimeDrivenTurn:

	def __init__(self, Name, AnimPlayRate, FinishAngleRange, RotateAngleMax, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, TargetBone, IsAllowAnimeDrivenNoChangeAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimPlayRate = AnimPlayRate
		self.FinishAngleRange = FinishAngleRange
		self.RotateAngleMax = RotateAngleMax
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.TargetBone = TargetBone
		self.IsAllowAnimeDrivenNoChangeAS = IsAllowAnimeDrivenNoChangeAS


class AnmArmorBindAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AnmBackMove:

	def __init__(self, Name, ASName, PosReduceRatio, RotReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio


class AnmBlownOff:

	def __init__(self, Name, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, OnGroundTime, AS, IsFinishByAnm, IsWaitForAnmEnd, WeaponDropSpeedXZ, WeaponDropSpeedY, IsItemDrop, IsFinishByWater, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.OnGroundTime = OnGroundTime
		self.AS = AS
		self.IsFinishByAnm = IsFinishByAnm
		self.IsWaitForAnmEnd = IsWaitForAnmEnd
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.IsItemDrop = IsItemDrop
		self.IsFinishByWater = IsFinishByWater
		self.UseKnockbackDir = UseKnockbackDir


class AnmBlownOffBackward:

	def __init__(self, Name, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, OnGroundTime, AS, IsFinishByAnm, IsWaitForAnmEnd, WeaponDropSpeedXZ, WeaponDropSpeedY, IsItemDrop, IsFinishByWater, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.OnGroundTime = OnGroundTime
		self.AS = AS
		self.IsFinishByAnm = IsFinishByAnm
		self.IsWaitForAnmEnd = IsWaitForAnmEnd
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.IsItemDrop = IsItemDrop
		self.IsFinishByWater = IsFinishByWater
		self.UseKnockbackDir = UseKnockbackDir


class AnmDamage:

	def __init__(self, Name, AS, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class AnmDirectionMove:

	def __init__(self, Name, ASName, PosReduceRatio, RotReduceRatio, IsChangeable, Direction, UsereachableCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsChangeable = IsChangeable
		self.Direction = Direction
		self.UsereachableCheck = UsereachableCheck


class AnmDrivenHover:

	def __init__(self, Name, RotReduceRatio, ASName, MoveYLimit, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotReduceRatio = RotReduceRatio
		self.ASName = ASName
		self.MoveYLimit = MoveYLimit
		self.PosReduceRatio = PosReduceRatio


class AnmDrivenHoverTurn:

	def __init__(self, Name, RotSpeed, BaseRotRatio, RotAccRatio, FinRotate, ASName, MoveYLimit, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.BaseRotRatio = BaseRotRatio
		self.RotAccRatio = RotAccRatio
		self.FinRotate = FinRotate
		self.ASName = ASName
		self.MoveYLimit = MoveYLimit
		self.PosReduceRatio = PosReduceRatio


class AnmDrivenMoveAttack:

	def __init__(self, Name, WeaponIdx, JustAvoidDist, IsForceGuardBreak, JustAvoidAngle, ASKeyName, TargetBoneName, IsChangeable, IsIgnoreSameAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.JustAvoidDist = JustAvoidDist
		self.IsForceGuardBreak = IsForceGuardBreak
		self.JustAvoidAngle = JustAvoidAngle
		self.ASKeyName = ASKeyName
		self.TargetBoneName = TargetBoneName
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS


class AnmDrivenSpeedBackWalk:

	def __init__(self, Name, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx


class AnmTimingBackWalk:

	def __init__(self, Name, AngReduceRatio, PosReduceRatio, ASName, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngReduceRatio = AngReduceRatio
		self.PosReduceRatio = PosReduceRatio
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class AnmToRagdollDie:

	def __init__(self, Name, ASName, ChangeRagdollFrame, PosBaseRagdollRbName, RagdollControllerName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ChangeRagdollFrame = ChangeRagdollFrame
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.RagdollControllerName = RagdollControllerName


class AnmUpDownMove:

	def __init__(self, Name, ASName, PosReduceRatio, RotReduceRatio, AccRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.AccRatio = AccRatio


class Appear:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AppearDeathCounter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearFullPouchInfo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearGameOver:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearMagneForce:

	def __init__(self, Name, MaxMagneForceRange, MinMagneForceRange, MagneControlSpeed, MagneForceRadius, MagneForceDamp, MagneForceVelRate, ObjectTerror, MagneShootSpeed, MagneControlRotateSpeed, MagneControlUpDownSpeed, ResistanceSpeedScale, MaxMagneHeight, CancelAngle, CancelHeight, CancelAngleFixed, CancelHeightFixed, GyroUpDownSpeed, GyroRotateSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxMagneForceRange = MaxMagneForceRange
		self.MinMagneForceRange = MinMagneForceRange
		self.MagneControlSpeed = MagneControlSpeed
		self.MagneForceRadius = MagneForceRadius
		self.MagneForceDamp = MagneForceDamp
		self.MagneForceVelRate = MagneForceVelRate
		self.ObjectTerror = ObjectTerror
		self.MagneShootSpeed = MagneShootSpeed
		self.MagneControlRotateSpeed = MagneControlRotateSpeed
		self.MagneControlUpDownSpeed = MagneControlUpDownSpeed
		self.ResistanceSpeedScale = ResistanceSpeedScale
		self.MaxMagneHeight = MaxMagneHeight
		self.CancelAngle = CancelAngle
		self.CancelHeight = CancelHeight
		self.CancelAngleFixed = CancelAngleFixed
		self.CancelHeightFixed = CancelHeightFixed
		self.GyroUpDownSpeed = GyroUpDownSpeed
		self.GyroRotateSpeed = GyroRotateSpeed


class AppearNumDungeonClearSeal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearNumHeroSeal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearNumKorokNuts:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AppearNumTargets:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ApplyHorizontalImpulse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ApplyMoveImpulse:

	def __init__(self, Name, FellImpRate, FellRotRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FellImpRate = FellImpRate
		self.FellRotRate = FellRotRate


class ApplyMoveTrigger:

	def __init__(self, Name, IsOnDebugDraw, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOnDebugDraw = IsOnDebugDraw


class AreaActorObserveByActorTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaActorObserveByGroup:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaBase:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaBottomTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaCulling:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaCullingClipArea:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaFireObserve:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaHorseSpeedLimitAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaLocation:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaObserveActorAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaOutRecreateActorAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaRecreateActorAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class AreaRoot:

	def __init__(self, Name, AutoSaveInterval, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AutoSaveInterval = AutoSaveInterval


class ArmorBindAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ArmorBindNodeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ArmorBindWithAS:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ArrowShootHoming:

	def __init__(self, Name, SubAngMax, HomingRate, NearDist, FallSpeedRatioByRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAngMax = SubAngMax
		self.HomingRate = HomingRate
		self.NearDist = NearDist
		self.FallSpeedRatioByRange = FallSpeedRatioByRange


class ArrowShootMove:

	def __init__(self, Name, FallSpeedRatioByRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FallSpeedRatioByRange = FallSpeedRatioByRange


class ArrowShootMoveForLargeObject:

	def __init__(self, Name, RayCastDist, CallSEKeyAtStick, FallSpeedRatioByRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RayCastDist = RayCastDist
		self.CallSEKeyAtStick = CallSEKeyAtStick
		self.FallSpeedRatioByRange = FallSpeedRatioByRange


class ArrowShootMoveWithStickOffset:

	def __init__(self, Name, StickOffset, FallSpeedRatioByRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StickOffset = StickOffset
		self.FallSpeedRatioByRange = FallSpeedRatioByRange


class ArrowSkyShootMove:

	def __init__(self, Name, SkyShootDist, Interval, FallSpeedRatioByRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SkyShootDist = SkyShootDist
		self.Interval = Interval
		self.FallSpeedRatioByRange = FallSpeedRatioByRange


class AscendingCurrent:

	def __init__(self, Name, WindSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WindSpeed = WindSpeed


class AscendingCurrentFixedSize:

	def __init__(self, Name, Size, DisableInDemo, WindSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Size = Size
		self.DisableInDemo = DisableInDemo
		self.WindSpeed = WindSpeed


class AscendingCurrentShieldable:

	def __init__(self, Name, WindSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WindSpeed = WindSpeed


class AssassinBossIronBallAppear:

	def __init__(self, Name, IronBallNum, CreateDist, BackDist, TopOffsetY, BaseOffsetY, IronBallPartsName, UDLimit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.CreateDist = CreateDist
		self.BackDist = BackDist
		self.TopOffsetY = TopOffsetY
		self.BaseOffsetY = BaseOffsetY
		self.IronBallPartsName = IronBallPartsName
		self.UDLimit = UDLimit


class AssassinBossIronBallAtkWithRot:

	def __init__(self, Name, AngSpd, IsJumpType, AddAngle, CentralAnchorName, IronBallNum, AttackType, IronBallPartsName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngSpd = AngSpd
		self.IsJumpType = IsJumpType
		self.AddAngle = AddAngle
		self.CentralAnchorName = CentralAnchorName
		self.IronBallNum = IronBallNum
		self.AttackType = AttackType
		self.IronBallPartsName = IronBallPartsName


class AssassinBossIronBallAttack:

	def __init__(self, Name, IronBallNum, AttackType, IronBallPartsName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.AttackType = AttackType
		self.IronBallPartsName = IronBallPartsName


class AssassinBossIronMagicChargeShot:

	def __init__(self, Name, IronBallNum, AttackType, IronBallPartsName, Level2AttackLifeRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IronBallNum = IronBallNum
		self.AttackType = AttackType
		self.IronBallPartsName = IronBallPartsName
		self.Level2AttackLifeRatio = Level2AttackLifeRatio


class AtAndBodyOnWait:

	def __init__(self, Name, BodyName, AtkAttrType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BodyName = BodyName
		self.AtkAttrType = AtkAttrType


class AtOnWait:

	def __init__(self, Name, AtkAttrType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkAttrType = AtkAttrType


class AtOnWaitNoHitRope:

	def __init__(self, Name, AtkAttrType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkAttrType = AtkAttrType


class Attack:

	def __init__(self, Name, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsIgnoreSmallHit, ASName, IsNoRodAttack, IsNoColRodAttack, RodAttackDelayTime, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.ASName = ASName
		self.IsNoRodAttack = IsNoRodAttack
		self.IsNoColRodAttack = IsNoColRodAttack
		self.RodAttackDelayTime = RodAttackDelayTime
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AttackJumpToTarget:

	def __init__(self, Name, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsIgnoreSmallHit, PosOffsetDist, IsCheckNoChangeAS, PreJumpAS, JumpAS, LandAS, MaxSpeed, JumpHeight, JumpGravity, PosReduceRatioOnGround, RotReduceRatioOnGround, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.PosOffsetDist = PosOffsetDist
		self.IsCheckNoChangeAS = IsCheckNoChangeAS
		self.PreJumpAS = PreJumpAS
		self.JumpAS = JumpAS
		self.LandAS = LandAS
		self.MaxSpeed = MaxSpeed
		self.JumpHeight = JumpHeight
		self.JumpGravity = JumpGravity
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.InWaterDepth = InWaterDepth


class AttackPartBind:

	def __init__(self, Name, ASSlot, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsIgnoreSmallHit, ASName, IsNoRodAttack, IsNoColRodAttack, RodAttackDelayTime, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASSlot = ASSlot
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.ASName = ASName
		self.IsNoRodAttack = IsNoRodAttack
		self.IsNoColRodAttack = IsNoColRodAttack
		self.RodAttackDelayTime = RodAttackDelayTime
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class AwarenessShareOnePartsASPlay:

	def __init__(self, Name, PartsKey, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey = PartsKey
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class BackFlip:

	def __init__(self, Name, Speed, PosRestRatio, JumpHeight, NearGrHeight, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.PosRestRatio = PosRestRatio
		self.JumpHeight = JumpHeight
		self.NearGrHeight = NearGrHeight
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class BackStep:

	def __init__(self, Name, JumpDist, StopSpeedRatio, StopRotSpeedRatio, JumpGravity, JumpHeight, RotRatio, CheckRotEvent, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpDist = JumpDist
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.JumpGravity = JumpGravity
		self.JumpHeight = JumpHeight
		self.RotRatio = RotRatio
		self.CheckRotEvent = CheckRotEvent


class BackStepAttack:

	def __init__(self, Name, WeaponIdx, MoveDist, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, JumpDist, StopSpeedRatio, StopRotSpeedRatio, JumpGravity, JumpHeight, RotRatio, CheckRotEvent, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.MoveDist = MoveDist
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.JumpDist = JumpDist
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.JumpGravity = JumpGravity
		self.JumpHeight = JumpHeight
		self.RotRatio = RotRatio
		self.CheckRotEvent = CheckRotEvent


class BackStepToTargetPos:

	def __init__(self, Name, IsJumpHeightFromHigherPos, StartAS, LoopAS, PreLandAS, EndAS, StopSpeedRatio, StopRotSpeedRatio, JumpGravity, JumpHeight, RotRatio, CheckRotEvent, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsJumpHeightFromHigherPos = IsJumpHeightFromHigherPos
		self.StartAS = StartAS
		self.LoopAS = LoopAS
		self.PreLandAS = PreLandAS
		self.EndAS = EndAS
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.JumpGravity = JumpGravity
		self.JumpHeight = JumpHeight
		self.RotRatio = RotRatio
		self.CheckRotEvent = CheckRotEvent


class BackSwim:

	def __init__(self, Name, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCheckCliff, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCheckCliff = IsCheckCliff
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class BackToRailFromLava:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BackWalk:

	def __init__(self, Name, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class BackWalkWithAS:

	def __init__(self, Name, ASName, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class BackseatKorokLight:

	def __init__(self, Name, GroundWaitASName, GroundAppearASName, GroundDisappearASName, FlyWaitASName, FlyAppearASName, FlyDisappearASName, AppearDist, DisappearDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GroundWaitASName = GroundWaitASName
		self.GroundAppearASName = GroundAppearASName
		self.GroundDisappearASName = GroundDisappearASName
		self.FlyWaitASName = FlyWaitASName
		self.FlyAppearASName = FlyAppearASName
		self.FlyDisappearASName = FlyDisappearASName
		self.AppearDist = AppearDist
		self.DisappearDist = DisappearDist


class BackseatKorokWait:

	def __init__(self, Name, WaitASName, AppearASName, DisappearASName, AppearDist, DisappearDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitASName = WaitASName
		self.AppearASName = AppearASName
		self.DisappearASName = DisappearASName
		self.AppearDist = AppearDist
		self.DisappearDist = DisappearDist


class Balloon:

	def __init__(self, Name, Length, RopeActorName, UpLimitSpeed, MaxAccel, MassScale, IsChaseInitHeight, HeightLimit, BreakTimer, WindAccScale, WindSpdScale, StayAccScale, ReturnToOriginalPos, ReturnStrengthFactor, RemainsHeightLimit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Length = Length
		self.RopeActorName = RopeActorName
		self.UpLimitSpeed = UpLimitSpeed
		self.MaxAccel = MaxAccel
		self.MassScale = MassScale
		self.IsChaseInitHeight = IsChaseInitHeight
		self.HeightLimit = HeightLimit
		self.BreakTimer = BreakTimer
		self.WindAccScale = WindAccScale
		self.WindSpdScale = WindSpdScale
		self.StayAccScale = StayAccScale
		self.ReturnToOriginalPos = ReturnToOriginalPos
		self.ReturnStrengthFactor = ReturnStrengthFactor
		self.RemainsHeightLimit = RemainsHeightLimit


class BasicSignalBossAwakeSleep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BasicSignalChangeDamping:

	def __init__(self, Name, LinearDamping, AngularDamping, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinearDamping = LinearDamping
		self.AngularDamping = AngularDamping


class BasicSignalEnemyForceNotice:

	def __init__(self, Name, Interval, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Interval = Interval


class BattleCloseDangerAvoidRun:

	def __init__(self, Name, AvoidSubAngle, DamageIgnoreDist, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AvoidSubAngle = AvoidSubAngle
		self.DamageIgnoreDist = DamageIgnoreDist
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseExplosivesAvoidRun:

	def __init__(self, Name, DamageIgnoreDist, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DamageIgnoreDist = DamageIgnoreDist
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseExplosivesGuardRun:

	def __init__(self, Name, DamageIgnoreDist, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DamageIgnoreDist = DamageIgnoreDist
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseGuardRun:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseGuardWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseLevelFlyMove:

	def __init__(self, Name, ASName, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.FlyHeightMin = FlyHeightMin


class BattleCloseMeanderGuardRun:

	def __init__(self, Name, MeanderWidth, MeanderSpeed, JumpUpSpeedReduceRatio, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MeanderWidth = MeanderWidth
		self.MeanderSpeed = MeanderSpeed
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseMeanderRun:

	def __init__(self, Name, MeanderWidth, MeanderSpeed, JumpUpSpeedReduceRatio, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MeanderWidth = MeanderWidth
		self.MeanderSpeed = MeanderSpeed
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseMove:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseSlippedWalk:

	def __init__(self, Name, ASName, AccRatio, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AccRatio = AccRatio
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleCloseWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class BattleDungeonBGMAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BattleHover:

	def __init__(self, Name, RotSpeed, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class BattleLevelFlyMove:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRotate, FinRadius, TargetHeightOffset, RotRatio, CheckStopSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.FinRadius = FinRadius
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.CheckStopSpeed = CheckStopSpeed


class BattleWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class BeamMove:

	def __init__(self, Name, ForceExplodeFrame, AtMinDamage, ShieldDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceExplodeFrame = ForceExplodeFrame
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage


class BeamTailDelete:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BeamosStaticBeam:

	def __init__(self, Name, BeamRange, BeamSpeed, MuzzleOffset, BeamDirection, UseDynamicCutting, BeamBoneName, BeamActorName, BeamActorKey, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BeamRange = BeamRange
		self.BeamSpeed = BeamSpeed
		self.MuzzleOffset = MuzzleOffset
		self.BeamDirection = BeamDirection
		self.UseDynamicCutting = UseDynamicCutting
		self.BeamBoneName = BeamBoneName
		self.BeamActorName = BeamActorName
		self.BeamActorKey = BeamActorKey
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class BecomePreActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BecomeSpeaker:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BeeAttack:

	def __init__(self, Name, ThroughDist, Speed, RotSpd, FinRotate, HorizontalFinRadius, TargetHeightOffset, RotRatio, VerticalFinLength, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThroughDist = ThroughDist
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.VerticalFinLength = VerticalFinLength


class BeeDamaged:

	def __init__(self, Name, SubActorSpeed, Time, AddYSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubActorSpeed = SubActorSpeed
		self.Time = Time
		self.AddYSpeed = AddYSpeed


class BeginObservation:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BeltConveyor:

	def __init__(self, Name, IsReverse, ASName, ASRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReverse = IsReverse
		self.ASName = ASName
		self.ASRate = ASRate


class BigEnemyLocaterRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BikeWarpEffectValueSetter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BindActionForManyActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BindActionUseParentPickInfo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BindOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BindParentAction:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class BirdEscape:

	def __init__(self, Name, MoveSpeedMax, MoveSpeedMin, TurnSpeed, InterpolateFrameForMaxSpeed, TargetEscapeWidthMax, TargetEscapeWidthMin, TargetHeightMax, TargetHeightMin, TargetTurnAngle, ContinueEscapeDistanceXZ, AdditionalWidth, TargetUpperAngle, StartReduceHeightRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeedMax = MoveSpeedMax
		self.MoveSpeedMin = MoveSpeedMin
		self.TurnSpeed = TurnSpeed
		self.InterpolateFrameForMaxSpeed = InterpolateFrameForMaxSpeed
		self.TargetEscapeWidthMax = TargetEscapeWidthMax
		self.TargetEscapeWidthMin = TargetEscapeWidthMin
		self.TargetHeightMax = TargetHeightMax
		self.TargetHeightMin = TargetHeightMin
		self.TargetTurnAngle = TargetTurnAngle
		self.ContinueEscapeDistanceXZ = ContinueEscapeDistanceXZ
		self.AdditionalWidth = AdditionalWidth
		self.TargetUpperAngle = TargetUpperAngle
		self.StartReduceHeightRate = StartReduceHeightRate


class BlowOffAttack:

	def __init__(self, Name, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsIgnoreSmallHit, ASName, IsNoRodAttack, IsNoColRodAttack, RodAttackDelayTime, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.ASName = ASName
		self.IsNoRodAttack = IsNoRodAttack
		self.IsNoColRodAttack = IsNoColRodAttack
		self.RodAttackDelayTime = RodAttackDelayTime
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class BlownOff:

	def __init__(self, Name, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class Bolt:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BombExplode:

	def __init__(self, Name, SizeUpTime, ExplodeTime, ShockPower, UseDefaultEffect, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SizeUpTime = SizeUpTime
		self.ExplodeTime = ExplodeTime
		self.ShockPower = ShockPower
		self.UseDefaultEffect = UseDefaultEffect


class BoomerangMove:

	def __init__(self, Name, PreCurveTimer, RadSpeed, CurveSpeedRate, StraightSpeedRate, TargetOffset, CurvePredictFrame, CurveCheckYDist, StraightPredictFrame, StraightCheckYDist, CatchAttentionName, FlyLimitTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreCurveTimer = PreCurveTimer
		self.RadSpeed = RadSpeed
		self.CurveSpeedRate = CurveSpeedRate
		self.StraightSpeedRate = StraightSpeedRate
		self.TargetOffset = TargetOffset
		self.CurvePredictFrame = CurvePredictFrame
		self.CurveCheckYDist = CurveCheckYDist
		self.StraightPredictFrame = StraightPredictFrame
		self.StraightCheckYDist = StraightCheckYDist
		self.CatchAttentionName = CatchAttentionName
		self.FlyLimitTime = FlyLimitTime


class BowArrowHold:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BowArrowReload:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BowArrowShoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BowChildArrowRain:

	def __init__(self, Name, MoveSpeed, MoveHeight, WaitTime, MoveCountNum, MoveRange, MoveOffsetBase, RotateRate, RotateStepMax, AngleToTarget, RainMax, TargetOffsetBase, RainScale, ToTargetTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed
		self.MoveHeight = MoveHeight
		self.WaitTime = WaitTime
		self.MoveCountNum = MoveCountNum
		self.MoveRange = MoveRange
		self.MoveOffsetBase = MoveOffsetBase
		self.RotateRate = RotateRate
		self.RotateStepMax = RotateStepMax
		self.AngleToTarget = AngleToTarget
		self.RainMax = RainMax
		self.TargetOffsetBase = TargetOffsetBase
		self.RainScale = RainScale
		self.ToTargetTime = ToTargetTime


class BowChildCreate:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class BowChildDeviceAppear:

	def __init__(self, Name, InitSpeed, EndTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitSpeed = InitSpeed
		self.EndTime = EndTime


class BowChildDeviceGaleArrow:

	def __init__(self, Name, CenterOffset, MaxMoveSpeed, RotateSpeedMax, RotateAccel, RotateOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CenterOffset = CenterOffset
		self.MaxMoveSpeed = MaxMoveSpeed
		self.RotateSpeedMax = RotateSpeedMax
		self.RotateAccel = RotateAccel
		self.RotateOffset = RotateOffset


class BowChildDeviceNormal:

	def __init__(self, Name, MoveSpeed, IsMoveAccel, WaitTime, AccelRate, BrakeStartDist, VibrationSpeed, StopDist, VibrationLength, MoveTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed
		self.IsMoveAccel = IsMoveAccel
		self.WaitTime = WaitTime
		self.AccelRate = AccelRate
		self.BrakeStartDist = BrakeStartDist
		self.VibrationSpeed = VibrationSpeed
		self.StopDist = StopDist
		self.VibrationLength = VibrationLength
		self.MoveTime = MoveTime


class BowChildReflectBullet:

	def __init__(self, Name, MoveSpeed, OffsetLength, TargetOffsetY, TargetMoveOffset, TargetMoveOffsetRandRange, MoveRotateRate, MoveRotateMax, MoveRotateMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed
		self.OffsetLength = OffsetLength
		self.TargetOffsetY = TargetOffsetY
		self.TargetMoveOffset = TargetMoveOffset
		self.TargetMoveOffsetRandRange = TargetMoveOffsetRandRange
		self.MoveRotateRate = MoveRotateRate
		self.MoveRotateMax = MoveRotateMax
		self.MoveRotateMin = MoveRotateMin


class BrightBowSlowFall:

	def __init__(self, Name, Gravity, FloatWaveCycle, FloatWaveWidth, FloatHeight, FloatSpring, FloatDamper, FallBrakeHeight, FallBrake, TailEffectKeyName, InitRotate, RotateSpeed, AttractionRange, AttractionRate, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Gravity = Gravity
		self.FloatWaveCycle = FloatWaveCycle
		self.FloatWaveWidth = FloatWaveWidth
		self.FloatHeight = FloatHeight
		self.FloatSpring = FloatSpring
		self.FloatDamper = FloatDamper
		self.FallBrakeHeight = FallBrakeHeight
		self.FallBrake = FallBrake
		self.TailEffectKeyName = TailEffectKeyName
		self.InitRotate = InitRotate
		self.RotateSpeed = RotateSpeed
		self.AttractionRange = AttractionRange
		self.AttractionRate = AttractionRate
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class BulletVertivalRotateOwner:

	def __init__(self, Name, RotSpeed, RotSpdAccRatio, OffsetY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.RotSpdAccRatio = RotSpdAccRatio
		self.OffsetY = OffsetY


class BurnDamage:

	def __init__(self, Name, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class CalcVecLengthToGameData:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CallOvserveActorTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraAbyss:

	def __init__(self, Name, RadiusMin, Fovy, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RadiusMin = RadiusMin
		self.Fovy = Fovy
		self.BowFlag = BowFlag


class CameraAiming:

	def __init__(self, Name, latMin, latMax, LatOffset, latStickScale, lngStickScale, latGyroScale, lngGyroScale, radiusMin, radiusMax, radiusMinLat, radiusMaxLat, radiusCus, sideOffset, worldBaseOffset, OffsetZ, OffsetZMin, OffsetZMax, atCus, fovy, gyro, ConnectType, Connect, Near, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latMin = latMin
		self.latMax = latMax
		self.LatOffset = LatOffset
		self.latStickScale = latStickScale
		self.lngStickScale = lngStickScale
		self.latGyroScale = latGyroScale
		self.lngGyroScale = lngGyroScale
		self.radiusMin = radiusMin
		self.radiusMax = radiusMax
		self.radiusMinLat = radiusMinLat
		self.radiusMaxLat = radiusMaxLat
		self.radiusCus = radiusCus
		self.sideOffset = sideOffset
		self.worldBaseOffset = worldBaseOffset
		self.OffsetZ = OffsetZ
		self.OffsetZMin = OffsetZMin
		self.OffsetZMax = OffsetZMax
		self.atCus = atCus
		self.fovy = fovy
		self.gyro = gyro
		self.ConnectType = ConnectType
		self.Connect = Connect
		self.Near = Near
		self.BowFlag = BowFlag


class CameraAiming2:

	def __init__(self, Name, LatMin, LatMax, LatMinWidth, LatMaxWidth, LatMinWeight, LatMaxWeight, LatStickScale, LngStickScale, LatGyroScale, LngGyroScale, RadiusMin, RadiusMax, RadiusMinWidth, RadiusMaxWidth, RadiusMinWeight, RadiusMaxWeight, SideOffset, OffsetYMin, OffsetYMax, OffsetYMinWidth, OffsetYMaxWidth, OffsetYMinWeight, OffsetYMaxWeight, Fovy, Gyro, Connect, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.LatMinWidth = LatMinWidth
		self.LatMaxWidth = LatMaxWidth
		self.LatMinWeight = LatMinWeight
		self.LatMaxWeight = LatMaxWeight
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.LatGyroScale = LatGyroScale
		self.LngGyroScale = LngGyroScale
		self.RadiusMin = RadiusMin
		self.RadiusMax = RadiusMax
		self.RadiusMinWidth = RadiusMinWidth
		self.RadiusMaxWidth = RadiusMaxWidth
		self.RadiusMinWeight = RadiusMinWeight
		self.RadiusMaxWeight = RadiusMaxWeight
		self.SideOffset = SideOffset
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.OffsetYMinWidth = OffsetYMinWidth
		self.OffsetYMaxWidth = OffsetYMaxWidth
		self.OffsetYMinWeight = OffsetYMinWeight
		self.OffsetYMaxWeight = OffsetYMaxWeight
		self.Fovy = Fovy
		self.Gyro = Gyro
		self.Connect = Connect
		self.BowFlag = BowFlag


class CameraChase:

	def __init__(self, Name, latMin, LatLimitMin, latMax, LatLimitMax, LatMinWidth, LatMaxWidth, LatMinWeight, LatMaxWeight, lat, lngCus, lngCusSpeedEffect, latStickScale, lngStickScale, radiusMin, radiusMax, RadiusMinWidth, RadiusMaxWidth, RadiusMinWeight, RadiusMaxWeight, radius, atMoveOffset, OffsetYMin, OffsetYMax, OffsetYMinWidth, OffsetYMaxWidth, OffsetYMinWeight, OffsetYMaxWeight, AtHCusMin, AtHCusMax, atVCusMin, atVCusMax, Fovy, Connect, ConnectItem, ConnectIndoor, BgCheckToAt, ProcMode, controlMode, keepManual, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latMin = latMin
		self.LatLimitMin = LatLimitMin
		self.latMax = latMax
		self.LatLimitMax = LatLimitMax
		self.LatMinWidth = LatMinWidth
		self.LatMaxWidth = LatMaxWidth
		self.LatMinWeight = LatMinWeight
		self.LatMaxWeight = LatMaxWeight
		self.lat = lat
		self.lngCus = lngCus
		self.lngCusSpeedEffect = lngCusSpeedEffect
		self.latStickScale = latStickScale
		self.lngStickScale = lngStickScale
		self.radiusMin = radiusMin
		self.radiusMax = radiusMax
		self.RadiusMinWidth = RadiusMinWidth
		self.RadiusMaxWidth = RadiusMaxWidth
		self.RadiusMinWeight = RadiusMinWeight
		self.RadiusMaxWeight = RadiusMaxWeight
		self.radius = radius
		self.atMoveOffset = atMoveOffset
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.OffsetYMinWidth = OffsetYMinWidth
		self.OffsetYMaxWidth = OffsetYMaxWidth
		self.OffsetYMinWeight = OffsetYMinWeight
		self.OffsetYMaxWeight = OffsetYMaxWeight
		self.AtHCusMin = AtHCusMin
		self.AtHCusMax = AtHCusMax
		self.atVCusMin = atVCusMin
		self.atVCusMax = atVCusMax
		self.Fovy = Fovy
		self.Connect = Connect
		self.ConnectItem = ConnectItem
		self.ConnectIndoor = ConnectIndoor
		self.BgCheckToAt = BgCheckToAt
		self.ProcMode = ProcMode
		self.controlMode = controlMode
		self.keepManual = keepManual
		self.BowFlag = BowFlag


class CameraClimbObj:

	def __init__(self, Name, Lat, LatMin, LatMax, LatStickScale, LngStickScale, Radius, OffsetY, Fovy, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Lat = Lat
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.Radius = Radius
		self.OffsetY = OffsetY
		self.Fovy = Fovy
		self.BowFlag = BowFlag


class CameraEdit:

	def __init__(self, Name, Normal, LockOn, Wall, NormalSubject, Bow, BowSquat, BowLockOn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Normal = Normal
		self.LockOn = LockOn
		self.Wall = Wall
		self.NormalSubject = NormalSubject
		self.Bow = Bow
		self.BowSquat = BowSquat
		self.BowLockOn = BowLockOn


class CameraEventAnim:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventAnimFlow:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventAnimFlowAbs:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventAnimFlowForMapTower:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventConnectTypeSpecify:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventFocusDistSetting:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventGameOver:

	def __init__(self, Name, Lat, Radius, OffsetY, Fovy, Count, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Lat = Lat
		self.Radius = Radius
		self.OffsetY = OffsetY
		self.Fovy = Fovy
		self.Count = Count
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventIdling:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventLook:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventLookDirect:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventMove:

	def __init__(self, Name, Radius, Fovy, TargetActor, FrontBoneName, FrontBoneAxis, FrontBoneAxisReverse, ReviseModeRunning, ReviseModeEnd, CollisionInterpolateSkip, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.Fovy = Fovy
		self.TargetActor = TargetActor
		self.FrontBoneName = FrontBoneName
		self.FrontBoneAxis = FrontBoneAxis
		self.FrontBoneAxisReverse = FrontBoneAxisReverse
		self.ReviseModeRunning = ReviseModeRunning
		self.ReviseModeEnd = ReviseModeEnd
		self.CollisionInterpolateSkip = CollisionInterpolateSkip
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventMovePos:

	def __init__(self, Name, TargetActor1, ActorName1, UniqueName1, TargetActor2, ActorName2, UniqueName2, AtAppendMode, PosAppendMode, FovyAppendMode, BaseMode, MotionMode, Pattern1AtX, Pattern1AtY, Pattern1AtZ, Pattern1PosX, Pattern1PosY, Pattern1PosZ, Pattern1Fovy, Pattern1Use, Accept1FrameDelay, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetActor1 = TargetActor1
		self.ActorName1 = ActorName1
		self.UniqueName1 = UniqueName1
		self.TargetActor2 = TargetActor2
		self.ActorName2 = ActorName2
		self.UniqueName2 = UniqueName2
		self.AtAppendMode = AtAppendMode
		self.PosAppendMode = PosAppendMode
		self.FovyAppendMode = FovyAppendMode
		self.BaseMode = BaseMode
		self.MotionMode = MotionMode
		self.Pattern1AtX = Pattern1AtX
		self.Pattern1AtY = Pattern1AtY
		self.Pattern1AtZ = Pattern1AtZ
		self.Pattern1PosX = Pattern1PosX
		self.Pattern1PosY = Pattern1PosY
		self.Pattern1PosZ = Pattern1PosZ
		self.Pattern1Fovy = Pattern1Fovy
		self.Pattern1Use = Pattern1Use
		self.Accept1FrameDelay = Accept1FrameDelay
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventMovePosFlow:

	def __init__(self, Name, BaseMode, Pattern1Use, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseMode = BaseMode
		self.Pattern1Use = Pattern1Use
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventMultiTalk:

	def __init__(self, Name, LatMin, LatMax, LatStickScale, LngStickScale, RadiusOffset, Connect, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.RadiusOffset = RadiusOffset
		self.Connect = Connect
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventOverwriteFar:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventOverwriteNear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventPermitGfxNear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventPlayerHideOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventPlayerHideOn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventPolarCoordPlayerRel:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventReserveConnectTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraEventSavePoint:

	def __init__(self, Name, SavePoint, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SavePoint = SavePoint
		self.BowFlag = BowFlag


class CameraEventTalk:

	def __init__(self, Name, DistanceMin, DistanceMax, RadiusNear, RadiusFar, LngNear, LngFar, LngRandom, LatNear, LatFar, FovyNear, FovyFar, ElevationAngleEffect, SpeakerSwitching, HideCheck, LeftOnly, RightOnly, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistanceMin = DistanceMin
		self.DistanceMax = DistanceMax
		self.RadiusNear = RadiusNear
		self.RadiusFar = RadiusFar
		self.LngNear = LngNear
		self.LngFar = LngFar
		self.LngRandom = LngRandom
		self.LatNear = LatNear
		self.LatFar = LatFar
		self.FovyNear = FovyNear
		self.FovyFar = FovyFar
		self.ElevationAngleEffect = ElevationAngleEffect
		self.SpeakerSwitching = SpeakerSwitching
		self.HideCheck = HideCheck
		self.LeftOnly = LeftOnly
		self.RightOnly = RightOnly
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventTalkManualCtrl:

	def __init__(self, Name, LatMin, LatMax, LatStickScale, LngStickScale, DistanceMin, DistanceMax, RadiusNear, RadiusFar, FovyNear, FovyFar, Connect, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.DistanceMin = DistanceMin
		self.DistanceMax = DistanceMax
		self.RadiusNear = RadiusNear
		self.RadiusFar = RadiusFar
		self.FovyNear = FovyNear
		self.FovyFar = FovyFar
		self.Connect = Connect
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventTalkManualCtrlRet:

	def __init__(self, Name, LatMin, LatMax, LatStickScale, LngStickScale, DistanceMin, DistanceMax, RadiusNear, RadiusFar, FovyNear, FovyFar, Connect, SavePoint, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.DistanceMin = DistanceMin
		self.DistanceMax = DistanceMax
		self.RadiusNear = RadiusNear
		self.RadiusFar = RadiusFar
		self.FovyNear = FovyNear
		self.FovyFar = FovyFar
		self.Connect = Connect
		self.SavePoint = SavePoint
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraEventTurn:

	def __init__(self, Name, NotifyDemoCamera2Sound, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NotifyDemoCamera2Sound = NotifyDemoCamera2Sound
		self.BowFlag = BowFlag


class CameraFinder:

	def __init__(self, Name, latMin, latMax, LatOffset, radius, offsetY, offsetZ, atCus, fovyMin, fovyMax, fovyCus, GyroScaleWithFovyMin, GyroScaleWithFovyMax, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latMin = latMin
		self.latMax = latMax
		self.LatOffset = LatOffset
		self.radius = radius
		self.offsetY = offsetY
		self.offsetZ = offsetZ
		self.atCus = atCus
		self.fovyMin = fovyMin
		self.fovyMax = fovyMax
		self.fovyCus = fovyCus
		self.GyroScaleWithFovyMin = GyroScaleWithFovyMin
		self.GyroScaleWithFovyMax = GyroScaleWithFovyMax
		self.BowFlag = BowFlag


class CameraHorse:

	def __init__(self, Name, latSlow, latFast, latCus, latMin, latMax, lngCusSlow, lngCusFast, LngCusParallel, LngCusVertical, radiusSlow, radiusFast, radiusCus, sideOffsetSlow, sideOffsetFast, sideOffsetCus, OffsetYMin, OffsetYMax, atHCus, atVCus, AtHCusSlow, AtHCusFast, AtVCusSlow, AtVCusFast, fovySlow, fovyFast, fovyCus, startCus, speedMin, speedMax, HandlingRateCoefficient, HandlingRateReturnSpeed, sideOffsetCusNoInput, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latSlow = latSlow
		self.latFast = latFast
		self.latCus = latCus
		self.latMin = latMin
		self.latMax = latMax
		self.lngCusSlow = lngCusSlow
		self.lngCusFast = lngCusFast
		self.LngCusParallel = LngCusParallel
		self.LngCusVertical = LngCusVertical
		self.radiusSlow = radiusSlow
		self.radiusFast = radiusFast
		self.radiusCus = radiusCus
		self.sideOffsetSlow = sideOffsetSlow
		self.sideOffsetFast = sideOffsetFast
		self.sideOffsetCus = sideOffsetCus
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.atHCus = atHCus
		self.atVCus = atVCus
		self.AtHCusSlow = AtHCusSlow
		self.AtHCusFast = AtHCusFast
		self.AtVCusSlow = AtVCusSlow
		self.AtVCusFast = AtVCusFast
		self.fovySlow = fovySlow
		self.fovyFast = fovyFast
		self.fovyCus = fovyCus
		self.startCus = startCus
		self.speedMin = speedMin
		self.speedMax = speedMax
		self.HandlingRateCoefficient = HandlingRateCoefficient
		self.HandlingRateReturnSpeed = HandlingRateReturnSpeed
		self.sideOffsetCusNoInput = sideOffsetCusNoInput
		self.BowFlag = BowFlag


class CameraHorseLockOnEmpty:

	def __init__(self, Name, latSlow, latFast, latControlRangeUp, latControlRangeDown, latCus, lngControlRange, lngCus, radiusSlow, radiusFast, radiusCus, worldBaseOffset, playerBaseOffset, atHCus, atVCus, fovySlow, fovyFast, fovyCus, startCus, speedMin, speedMax, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latSlow = latSlow
		self.latFast = latFast
		self.latControlRangeUp = latControlRangeUp
		self.latControlRangeDown = latControlRangeDown
		self.latCus = latCus
		self.lngControlRange = lngControlRange
		self.lngCus = lngCus
		self.radiusSlow = radiusSlow
		self.radiusFast = radiusFast
		self.radiusCus = radiusCus
		self.worldBaseOffset = worldBaseOffset
		self.playerBaseOffset = playerBaseOffset
		self.atHCus = atHCus
		self.atVCus = atVCus
		self.fovySlow = fovySlow
		self.fovyFast = fovyFast
		self.fovyCus = fovyCus
		self.startCus = startCus
		self.speedMin = speedMin
		self.speedMax = speedMax
		self.BowFlag = BowFlag


class CameraKeep:

	def __init__(self, Name, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BowFlag = BowFlag


class CameraLockOn:

	def __init__(self, Name, distMin, distMax, atCus, atOffsetVNear, atOffsetVFar, atOffsetCus, latVDiffEffect, latOffsetNear, latOffsetFar, latMin, latMax, latCus, lngNear, lngFar, lngMax, lngCus, radiusNear, radiusFar, radiusCus, fovyNear, fovyFar, fovyCus, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.distMin = distMin
		self.distMax = distMax
		self.atCus = atCus
		self.atOffsetVNear = atOffsetVNear
		self.atOffsetVFar = atOffsetVFar
		self.atOffsetCus = atOffsetCus
		self.latVDiffEffect = latVDiffEffect
		self.latOffsetNear = latOffsetNear
		self.latOffsetFar = latOffsetFar
		self.latMin = latMin
		self.latMax = latMax
		self.latCus = latCus
		self.lngNear = lngNear
		self.lngFar = lngFar
		self.lngMax = lngMax
		self.lngCus = lngCus
		self.radiusNear = radiusNear
		self.radiusFar = radiusFar
		self.radiusCus = radiusCus
		self.fovyNear = fovyNear
		self.fovyFar = fovyFar
		self.fovyCus = fovyCus
		self.BowFlag = BowFlag


class CameraLockOnAimingAt:

	def __init__(self, Name, LatMin, LatMax, InputRangeNearDist, LatInputRange, LngInputRange, InputRangeFarDist, LatInputRangeFar, LngInputRangeFar, Radius, OffsetX, OffsetY, Fovy, Gyro, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatMax = LatMax
		self.InputRangeNearDist = InputRangeNearDist
		self.LatInputRange = LatInputRange
		self.LngInputRange = LngInputRange
		self.InputRangeFarDist = InputRangeFarDist
		self.LatInputRangeFar = LatInputRangeFar
		self.LngInputRangeFar = LngInputRangeFar
		self.Radius = Radius
		self.OffsetX = OffsetX
		self.OffsetY = OffsetY
		self.Fovy = Fovy
		self.Gyro = Gyro
		self.BowFlag = BowFlag


class CameraMagneCatch:

	def __init__(self, Name, distMin, distMax, atCus, atOffsetVNear, atOffsetVFar, atOffsetCus, latVDiffEffect, latOffsetNear, latOffsetFar, latMin, latMax, latCus, lngNear, lngFar, lngMax, lngCus, radiusNear, radiusFar, radiusCus, fovyNear, fovyFar, fovyCus, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.distMin = distMin
		self.distMax = distMax
		self.atCus = atCus
		self.atOffsetVNear = atOffsetVNear
		self.atOffsetVFar = atOffsetVFar
		self.atOffsetCus = atOffsetCus
		self.latVDiffEffect = latVDiffEffect
		self.latOffsetNear = latOffsetNear
		self.latOffsetFar = latOffsetFar
		self.latMin = latMin
		self.latMax = latMax
		self.latCus = latCus
		self.lngNear = lngNear
		self.lngFar = lngFar
		self.lngMax = lngMax
		self.lngCus = lngCus
		self.radiusNear = radiusNear
		self.radiusFar = radiusFar
		self.radiusCus = radiusCus
		self.fovyNear = fovyNear
		self.fovyFar = fovyFar
		self.fovyCus = fovyCus
		self.BowFlag = BowFlag


class CameraMotorcycle:

	def __init__(self, Name, SpeedMin, SpeedMax, LatitudeMin, LatitudeMax, AutoLatitudeSlow, AutoLatitudeFast, AutoLatitudeB2ICushion, CameraRadiusSlow, CameraRadiusFast, CameraRadiusB2ICushion, SideOffsetSlow, SideOffsetFast, MaxSideOffset, SideOffsetCushion, VerticalOffsetSlow, VerticalOffsetFast, VerticalOffetCushion, AtBaseHCushion, AtBaseVCushion, FollowingRotateCushion, FollowingTransCushion, FollowingAnglarVelCushion, AutoLngBaseCushion, AutoLngMaxRotSpeed, AutoLngMaxRotSpeedSpin, SwitchingCushionRate, AngularVelocityThreshold, CameraFollowRotCushion, CameraFollowPosCushionX, CameraFollowPosCushionZNormal, CameraFollowPosCushionZStart, CameraFollowPosCushionZWheelie, CFPCZCushionUp, CFPCZCushionDown, CamFollowCusChangeTimeStart, CamFollowCusChangeTimeWheelie, FovySlow, FovyFast, FovyStart, FovyWheelie, FovyBaseCushionDown, FovyBaseCushionUpNormal, FovyBaseCushionUpStart, FovyBaseCushionUpWheelie, FovyChangeTimeStart, FovyChangeTimeWheelie, IdealRotateVelScaleFactor, AgainstIdealRotVelCushion, SpeedRateCushion, SwitchingCushionRateLOE, SideOffsetByleaning, ThresholdAngleDiffCoeff, SpringBackToHardStartTime, SpringBackToHardCushion, SpringChangeToSoftStartDistance, SpringChangeToSoftEndDistance, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedMin = SpeedMin
		self.SpeedMax = SpeedMax
		self.LatitudeMin = LatitudeMin
		self.LatitudeMax = LatitudeMax
		self.AutoLatitudeSlow = AutoLatitudeSlow
		self.AutoLatitudeFast = AutoLatitudeFast
		self.AutoLatitudeB2ICushion = AutoLatitudeB2ICushion
		self.CameraRadiusSlow = CameraRadiusSlow
		self.CameraRadiusFast = CameraRadiusFast
		self.CameraRadiusB2ICushion = CameraRadiusB2ICushion
		self.SideOffsetSlow = SideOffsetSlow
		self.SideOffsetFast = SideOffsetFast
		self.MaxSideOffset = MaxSideOffset
		self.SideOffsetCushion = SideOffsetCushion
		self.VerticalOffsetSlow = VerticalOffsetSlow
		self.VerticalOffsetFast = VerticalOffsetFast
		self.VerticalOffetCushion = VerticalOffetCushion
		self.AtBaseHCushion = AtBaseHCushion
		self.AtBaseVCushion = AtBaseVCushion
		self.FollowingRotateCushion = FollowingRotateCushion
		self.FollowingTransCushion = FollowingTransCushion
		self.FollowingAnglarVelCushion = FollowingAnglarVelCushion
		self.AutoLngBaseCushion = AutoLngBaseCushion
		self.AutoLngMaxRotSpeed = AutoLngMaxRotSpeed
		self.AutoLngMaxRotSpeedSpin = AutoLngMaxRotSpeedSpin
		self.SwitchingCushionRate = SwitchingCushionRate
		self.AngularVelocityThreshold = AngularVelocityThreshold
		self.CameraFollowRotCushion = CameraFollowRotCushion
		self.CameraFollowPosCushionX = CameraFollowPosCushionX
		self.CameraFollowPosCushionZNormal = CameraFollowPosCushionZNormal
		self.CameraFollowPosCushionZStart = CameraFollowPosCushionZStart
		self.CameraFollowPosCushionZWheelie = CameraFollowPosCushionZWheelie
		self.CFPCZCushionUp = CFPCZCushionUp
		self.CFPCZCushionDown = CFPCZCushionDown
		self.CamFollowCusChangeTimeStart = CamFollowCusChangeTimeStart
		self.CamFollowCusChangeTimeWheelie = CamFollowCusChangeTimeWheelie
		self.FovySlow = FovySlow
		self.FovyFast = FovyFast
		self.FovyStart = FovyStart
		self.FovyWheelie = FovyWheelie
		self.FovyBaseCushionDown = FovyBaseCushionDown
		self.FovyBaseCushionUpNormal = FovyBaseCushionUpNormal
		self.FovyBaseCushionUpStart = FovyBaseCushionUpStart
		self.FovyBaseCushionUpWheelie = FovyBaseCushionUpWheelie
		self.FovyChangeTimeStart = FovyChangeTimeStart
		self.FovyChangeTimeWheelie = FovyChangeTimeWheelie
		self.IdealRotateVelScaleFactor = IdealRotateVelScaleFactor
		self.AgainstIdealRotVelCushion = AgainstIdealRotVelCushion
		self.SpeedRateCushion = SpeedRateCushion
		self.SwitchingCushionRateLOE = SwitchingCushionRateLOE
		self.SideOffsetByleaning = SideOffsetByleaning
		self.ThresholdAngleDiffCoeff = ThresholdAngleDiffCoeff
		self.SpringBackToHardStartTime = SpringBackToHardStartTime
		self.SpringBackToHardCushion = SpringBackToHardCushion
		self.SpringChangeToSoftStartDistance = SpringChangeToSoftStartDistance
		self.SpringChangeToSoftEndDistance = SpringChangeToSoftEndDistance
		self.BowFlag = BowFlag


class CameraMotorcycleLockOnEmpty:

	def __init__(self, Name, SpeedMax, SpeedMin, LatitudeMin, LatitudeMax, AutoLatitudeSlow, AutoLatitudeFast, AutoLatitudeB2ICushion, AutoLngBaseCushion, AutoLngMaxRotSpeed, CameraRadiusSlow, CameraRadiusFast, CameraRadiusB2ICushion, CameraFollowRotCushion, CameraFollowPosCushionX, CameraFollowPosCushionYUp, CameraFollowPosCushionYDown, CameraFollowPosCushionZ, FovySlow, FovyFast, FovyBaseCushion, AtOffsetWorld, AtOffsetLocal, SwitchingCushionRate, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedMax = SpeedMax
		self.SpeedMin = SpeedMin
		self.LatitudeMin = LatitudeMin
		self.LatitudeMax = LatitudeMax
		self.AutoLatitudeSlow = AutoLatitudeSlow
		self.AutoLatitudeFast = AutoLatitudeFast
		self.AutoLatitudeB2ICushion = AutoLatitudeB2ICushion
		self.AutoLngBaseCushion = AutoLngBaseCushion
		self.AutoLngMaxRotSpeed = AutoLngMaxRotSpeed
		self.CameraRadiusSlow = CameraRadiusSlow
		self.CameraRadiusFast = CameraRadiusFast
		self.CameraRadiusB2ICushion = CameraRadiusB2ICushion
		self.CameraFollowRotCushion = CameraFollowRotCushion
		self.CameraFollowPosCushionX = CameraFollowPosCushionX
		self.CameraFollowPosCushionYUp = CameraFollowPosCushionYUp
		self.CameraFollowPosCushionYDown = CameraFollowPosCushionYDown
		self.CameraFollowPosCushionZ = CameraFollowPosCushionZ
		self.FovySlow = FovySlow
		self.FovyFast = FovyFast
		self.FovyBaseCushion = FovyBaseCushion
		self.AtOffsetWorld = AtOffsetWorld
		self.AtOffsetLocal = AtOffsetLocal
		self.SwitchingCushionRate = SwitchingCushionRate
		self.BowFlag = BowFlag


class CameraRevolve:

	def __init__(self, Name, latTarget, latCus, isKeepLat, lngTarget, lngCus, isKeepLng, radiusMin, radiusMax, radiusCus, sideOffset, sideOffsetCus, worldBaseOffset, playerBaseOffset, atHCus, atHCusSword, atVCus, fovy, fovyCus, startCus, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latTarget = latTarget
		self.latCus = latCus
		self.isKeepLat = isKeepLat
		self.lngTarget = lngTarget
		self.lngCus = lngCus
		self.isKeepLng = isKeepLng
		self.radiusMin = radiusMin
		self.radiusMax = radiusMax
		self.radiusCus = radiusCus
		self.sideOffset = sideOffset
		self.sideOffsetCus = sideOffsetCus
		self.worldBaseOffset = worldBaseOffset
		self.playerBaseOffset = playerBaseOffset
		self.atHCus = atHCus
		self.atHCusSword = atHCusSword
		self.atVCus = atVCus
		self.fovy = fovy
		self.fovyCus = fovyCus
		self.startCus = startCus
		self.BowFlag = BowFlag


class CameraRotRumble:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraRumble:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraRumbleLoop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraRumbleStop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraRumbleStopWithDamping:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CameraShieldSurfing:

	def __init__(self, Name, LatMin, LatLimitMin, LatMax, LatLimitMax, LatMinWidth, LatMaxWidth, LatMinWeight, LatMaxWeight, Lat, LngCus, LngCusSpeedEffect, LatStickScale, LngStickScale, RadiusMin, RadiusMax, RadiusMinWidth, RadiusMaxWidth, RadiusMinWeight, RadiusMaxWeight, Radius, OffsetYMin, OffsetYMax, OffsetYMinWidth, OffsetYMaxWidth, OffsetYMinWeight, OffsetYMaxWeight, SideOffset, SideOffsetCus, SideOffsetRateCus, AtHCus, AtVCusMin, AtVCusMax, Fovy, AutoModeConnect, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatLimitMin = LatLimitMin
		self.LatMax = LatMax
		self.LatLimitMax = LatLimitMax
		self.LatMinWidth = LatMinWidth
		self.LatMaxWidth = LatMaxWidth
		self.LatMinWeight = LatMinWeight
		self.LatMaxWeight = LatMaxWeight
		self.Lat = Lat
		self.LngCus = LngCus
		self.LngCusSpeedEffect = LngCusSpeedEffect
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.RadiusMin = RadiusMin
		self.RadiusMax = RadiusMax
		self.RadiusMinWidth = RadiusMinWidth
		self.RadiusMaxWidth = RadiusMaxWidth
		self.RadiusMinWeight = RadiusMinWeight
		self.RadiusMaxWeight = RadiusMaxWeight
		self.Radius = Radius
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.OffsetYMinWidth = OffsetYMinWidth
		self.OffsetYMaxWidth = OffsetYMaxWidth
		self.OffsetYMinWeight = OffsetYMinWeight
		self.OffsetYMaxWeight = OffsetYMaxWeight
		self.SideOffset = SideOffset
		self.SideOffsetCus = SideOffsetCus
		self.SideOffsetRateCus = SideOffsetRateCus
		self.AtHCus = AtHCus
		self.AtVCusMin = AtVCusMin
		self.AtVCusMax = AtVCusMax
		self.Fovy = Fovy
		self.AutoModeConnect = AutoModeConnect
		self.BowFlag = BowFlag


class CameraTail:

	def __init__(self, Name, latMin, latMax, Radius, RadiusDolly, OffsetYMin, OffsetYMax, Fovy, dstAngle, PanSpeedParam, StartInterpolateParam, ResetInterpolateParam, TargetSpeedMax, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.latMin = latMin
		self.latMax = latMax
		self.Radius = Radius
		self.RadiusDolly = RadiusDolly
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.Fovy = Fovy
		self.dstAngle = dstAngle
		self.PanSpeedParam = PanSpeedParam
		self.StartInterpolateParam = StartInterpolateParam
		self.ResetInterpolateParam = ResetInterpolateParam
		self.TargetSpeedMax = TargetSpeedMax
		self.BowFlag = BowFlag


class CameraVibrate:

	def __init__(self, Name, StartSoundName, LoopSoundName, IsSound, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartSoundName = StartSoundName
		self.LoopSoundName = LoopSoundName
		self.IsSound = IsSound


class CameraWakeboard:

	def __init__(self, Name, LatMin, LatLimitMin, LatMax, LatLimitMax, LatMinWidth, LatMaxWidth, LatMinWeight, LatMaxWeight, Lat, LngCus, LngCusSpeedEffect, LatStickScale, LngStickScale, RadiusMin, RadiusMax, RadiusMinWidth, RadiusMaxWidth, RadiusMinWeight, RadiusMaxWeight, Radius, OffsetYBase, OffsetYMin, OffsetYMax, OffsetYMinWidth, OffsetYMaxWidth, OffsetYMinWeight, OffsetYMaxWeight, OffsetZ, SideOffset, SideOffsetCus, AtHCusNormal, AtHCusSpurt, AtVCusMin, AtVCusMax, FovyNormal, FovySpurt, FovyCusAccel, FovyCusDecel, AutoModeConnect, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LatMin = LatMin
		self.LatLimitMin = LatLimitMin
		self.LatMax = LatMax
		self.LatLimitMax = LatLimitMax
		self.LatMinWidth = LatMinWidth
		self.LatMaxWidth = LatMaxWidth
		self.LatMinWeight = LatMinWeight
		self.LatMaxWeight = LatMaxWeight
		self.Lat = Lat
		self.LngCus = LngCus
		self.LngCusSpeedEffect = LngCusSpeedEffect
		self.LatStickScale = LatStickScale
		self.LngStickScale = LngStickScale
		self.RadiusMin = RadiusMin
		self.RadiusMax = RadiusMax
		self.RadiusMinWidth = RadiusMinWidth
		self.RadiusMaxWidth = RadiusMaxWidth
		self.RadiusMinWeight = RadiusMinWeight
		self.RadiusMaxWeight = RadiusMaxWeight
		self.Radius = Radius
		self.OffsetYBase = OffsetYBase
		self.OffsetYMin = OffsetYMin
		self.OffsetYMax = OffsetYMax
		self.OffsetYMinWidth = OffsetYMinWidth
		self.OffsetYMaxWidth = OffsetYMaxWidth
		self.OffsetYMinWeight = OffsetYMinWeight
		self.OffsetYMaxWeight = OffsetYMaxWeight
		self.OffsetZ = OffsetZ
		self.SideOffset = SideOffset
		self.SideOffsetCus = SideOffsetCus
		self.AtHCusNormal = AtHCusNormal
		self.AtHCusSpurt = AtHCusSpurt
		self.AtVCusMin = AtVCusMin
		self.AtVCusMax = AtVCusMax
		self.FovyNormal = FovyNormal
		self.FovySpurt = FovySpurt
		self.FovyCusAccel = FovyCusAccel
		self.FovyCusDecel = FovyCusDecel
		self.AutoModeConnect = AutoModeConnect
		self.BowFlag = BowFlag


class CameraWaterRemainsHowling:

	def __init__(self, Name, Radius, RadiusFromPlayer, AtY, AtOffsetZ, WaterAvoid4At, WaterAvoid4CameraPos, Fovy, Connect, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.RadiusFromPlayer = RadiusFromPlayer
		self.AtY = AtY
		self.AtOffsetZ = AtOffsetZ
		self.WaterAvoid4At = WaterAvoid4At
		self.WaterAvoid4CameraPos = WaterAvoid4CameraPos
		self.Fovy = Fovy
		self.Connect = Connect
		self.BowFlag = BowFlag


class CameraWaterfallClimb:

	def __init__(self, Name, Lat, Lng, Radius, HeightAllowance, ManualHeightMin, ManualHeightMax, OffsetY, Fovy, BowFlag, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Lat = Lat
		self.Lng = Lng
		self.Radius = Radius
		self.HeightAllowance = HeightAllowance
		self.ManualHeightMin = ManualHeightMin
		self.ManualHeightMax = ManualHeightMax
		self.OffsetY = OffsetY
		self.Fovy = Fovy
		self.BowFlag = BowFlag


class CapturedActElectricParalyisis:

	def __init__(self, Name, PauseDelayFrames, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PauseDelayFrames = PauseDelayFrames
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class CapturedActFreeze:

	def __init__(self, Name, ASKeyName, PauseDelayFrames, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.PauseDelayFrames = PauseDelayFrames
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class CapturedActKnockBack:

	def __init__(self, Name, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class Carried:

	def __init__(self, Name, IsCreateItem, IsRecoverCharCtrlAxis, IsUseConstraint, FailDistance, IsOnBaseLink, BindType, IsChangeable, HoldOnXLinkKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCreateItem = IsCreateItem
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.IsUseConstraint = IsUseConstraint
		self.FailDistance = FailDistance
		self.IsOnBaseLink = IsOnBaseLink
		self.BindType = BindType
		self.IsChangeable = IsChangeable
		self.HoldOnXLinkKey = HoldOnXLinkKey


class CarriedNoHit:

	def __init__(self, Name, IsCreateItem, IsRecoverCharCtrlAxis, IsUseConstraint, FailDistance, IsOnBaseLink, BindType, IsChangeable, HoldOnXLinkKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCreateItem = IsCreateItem
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.IsUseConstraint = IsUseConstraint
		self.FailDistance = FailDistance
		self.IsOnBaseLink = IsOnBaseLink
		self.BindType = BindType
		self.IsChangeable = IsChangeable
		self.HoldOnXLinkKey = HoldOnXLinkKey


class Catch:

	def __init__(self, Name, WeaponIdx, RotSpd, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.RotSpd = RotSpd
		self.ASName = ASName


class ChallengeChainRing:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChanegToLog:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeChoiceNumMsgFor3DShop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeEmotion:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeEnvForEnduranceDungeon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeFreeMovingForDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeMiniMapScale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangePosture:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangePostureWithAS:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeScene:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeScheduleAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChangeWeaponEquipState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChargeChemicalWeaponPower:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CheckExistenceOfParticipant:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CheckHorseCustomizeEdit:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ChemicalElectricWaterBall:

	def __init__(self, Name, DeleteTime, TargetScale, ScaleKeep, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeleteTime = DeleteTime
		self.TargetScale = TargetScale
		self.ScaleKeep = ScaleKeep
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class ChemicalPhysBall:

	def __init__(self, Name, DeleteTime, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeleteTime = DeleteTime
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class ChemicalPhysHitBreakBall:

	def __init__(self, Name, DeleteTime, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeleteTime = DeleteTime
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class ChemicalStayObject:

	def __init__(self, Name, DeleteTime, AtAttr, IsBindToGeneratedActor, BindNodeName, CurveAng, ReduceVelRate, BindOffset, CurveAngRandomRange, ReduceVelRandomRange, SideAmplitude, IsChemicalAttack, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeleteTime = DeleteTime
		self.AtAttr = AtAttr
		self.IsBindToGeneratedActor = IsBindToGeneratedActor
		self.BindNodeName = BindNodeName
		self.CurveAng = CurveAng
		self.ReduceVelRate = ReduceVelRate
		self.BindOffset = BindOffset
		self.CurveAngRandomRange = CurveAngRandomRange
		self.ReduceVelRandomRange = ReduceVelRandomRange
		self.SideAmplitude = SideAmplitude
		self.IsChemicalAttack = IsChemicalAttack


class Chemicalward:

	def __init__(self, Name, WeaponIdx, NodeName, NodeAxisIdx, TiredRadius, TiredAngle, StableTime, KeepTime, TiredTime, Voltage, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.NodeName = NodeName
		self.NodeAxisIdx = NodeAxisIdx
		self.TiredRadius = TiredRadius
		self.TiredAngle = TiredAngle
		self.StableTime = StableTime
		self.KeepTime = KeepTime
		self.TiredTime = TiredTime
		self.Voltage = Voltage
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ChuchuCommonDownTimer:

	def __init__(self, Name, MinWaitFrame, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinWaitFrame = MinWaitFrame
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ChuchuDissappearEscape:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ChuchuPreAttack:

	def __init__(self, Name, DamageAS, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, SubAS, SubASSlot, LeaveSubAS, DamageSubAS, PosReduceRatioByDamage, JumpNum, MoveBoneRotRatio, MoveBoneRotSpeedMin, ASName, TurnSpeed, PosReduceRatio, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DamageAS = DamageAS
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.LeaveSubAS = LeaveSubAS
		self.DamageSubAS = DamageSubAS
		self.PosReduceRatioByDamage = PosReduceRatioByDamage
		self.JumpNum = JumpNum
		self.MoveBoneRotRatio = MoveBoneRotRatio
		self.MoveBoneRotSpeedMin = MoveBoneRotSpeedMin
		self.ASName = ASName
		self.TurnSpeed = TurnSpeed
		self.PosReduceRatio = PosReduceRatio
		self.JumpHeight = JumpHeight


class CloseArmorProcessing:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CloseClockTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CloseItemMenu:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ClosePouchAddStockNum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CollaboShootingStarAreaTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CollaboShootingStarBrightTower:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CollaboShootingStartFlying:

	def __init__(self, Name, InitialVelocityMax, InitialVelocityMin, LookSuccessRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitialVelocityMax = InitialVelocityMax
		self.InitialVelocityMin = InitialVelocityMin
		self.LookSuccessRate = LookSuccessRate


class CollaborationShootingStarAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ControlBombEffect:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ControllerRumble:

	def __init__(self, Name, Pattern, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Pattern = Pattern


class CopyMapPinPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CreateActorInAreaBasic:

	def __init__(self, Name, BaseOffset, CreateRandArea, ProhibitedCreateArea, CreateNewActorIntervalFirst, CreateNewActorInterval, CreateContinueTime, CreateBasePosNum, CreateActorName, AfterWaitTime, IsAllowCreateNoSafeArea, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseOffset = BaseOffset
		self.CreateRandArea = CreateRandArea
		self.ProhibitedCreateArea = ProhibitedCreateArea
		self.CreateNewActorIntervalFirst = CreateNewActorIntervalFirst
		self.CreateNewActorInterval = CreateNewActorInterval
		self.CreateContinueTime = CreateContinueTime
		self.CreateBasePosNum = CreateBasePosNum
		self.CreateActorName = CreateActorName
		self.AfterWaitTime = AfterWaitTime
		self.IsAllowCreateNoSafeArea = IsAllowCreateNoSafeArea


class CreateAndReplaceAssassin:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CreateDragonChallengeXLink:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CreateEpona:

	def __init__(self, Name, AreaThreshold, AreaSearchRadius, AreaSearchCharacterRadius, CreateStartRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AreaThreshold = AreaThreshold
		self.AreaSearchRadius = AreaSearchRadius
		self.AreaSearchCharacterRadius = AreaSearchCharacterRadius
		self.CreateStartRate = CreateStartRate


class CreateGanonChemicalPillar:

	def __init__(self, Name, ScaleTime, AttackPower, AtMinDamage, MaxScale, CreateActorName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ScaleTime = ScaleTime
		self.AttackPower = AttackPower
		self.AtMinDamage = AtMinDamage
		self.MaxScale = MaxScale
		self.CreateActorName = CreateActorName


class CreateObjectsOfOwnedHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CurseRRematchCount:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CustomDuckingEndAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class CustomDuckingStartAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DRCAppNoUseTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DamageField:

	def __init__(self, Name, FieldType, RigidSetName, RigidBodyName, IsChangeRigidWorldMode, IsUseCollisionInfo, CollisionInfoName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FieldType = FieldType
		self.RigidSetName = RigidSetName
		self.RigidBodyName = RigidBodyName
		self.IsChangeRigidWorldMode = IsChangeRigidWorldMode
		self.IsUseCollisionInfo = IsUseCollisionInfo
		self.CollisionInfoName = CollisionInfoName


class DamageTurnByWeakPoint:

	def __init__(self, Name, ASName, TurnSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TurnSpeed = TurnSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class DamagedTurn:

	def __init__(self, Name, ASName, RotSpeed, RotRatio, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.RotSpeed = RotSpeed
		self.RotRatio = RotRatio
		self.PosReduceRatio = PosReduceRatio


class DefEscapeFreeMoveAction:

	def __init__(self, Name, ASKeyName, RunAwaySpeed, RunAwayAngleSpeed, RunAwayDistanceMax, RunAwayDistanceMin, RunAwayHeightOffset, AllowRandAngleVertical, AllowRandAngleHorizontal, InWater, IsSnake, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.RunAwaySpeed = RunAwaySpeed
		self.RunAwayAngleSpeed = RunAwayAngleSpeed
		self.RunAwayDistanceMax = RunAwayDistanceMax
		self.RunAwayDistanceMin = RunAwayDistanceMin
		self.RunAwayHeightOffset = RunAwayHeightOffset
		self.AllowRandAngleVertical = AllowRandAngleVertical
		self.AllowRandAngleHorizontal = AllowRandAngleHorizontal
		self.InWater = InWater
		self.IsSnake = IsSnake


class DefRandomMoveAction:

	def __init__(self, Name, IsUseBasepos, RadiusLimit, MaxMoveSpeed, MinMoveSpeed, MaxMoveDistance, MinMoveDistance, MaxMoveAngle, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseBasepos = IsUseBasepos
		self.RadiusLimit = RadiusLimit
		self.MaxMoveSpeed = MaxMoveSpeed
		self.MinMoveSpeed = MinMoveSpeed
		self.MaxMoveDistance = MaxMoveDistance
		self.MinMoveDistance = MinMoveDistance
		self.MaxMoveAngle = MaxMoveAngle
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class DefTurnAction:

	def __init__(self, Name, ASKeyName, RotateSpeed, WaitRotate, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.RotateSpeed = RotateSpeed
		self.WaitRotate = WaitRotate
		self.JumpHeight = JumpHeight


class DefeatedHugeEnemyCount:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Delete:

	def __init__(self, Name, DeleteType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeleteType = DeleteType


class DeleteAllIceBlockForDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DeleteInGround:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class DeletePorchItemIncludeEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoApplyDamageForPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoBeastGanonGrudgeDrop:

	def __init__(self, Name, GrudeRainObject, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrudeRainObject = GrudeRainObject


class DemoChangeEntityNoHit:

	def __init__(self, Name, IsNoHit, SetMotionType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsNoHit = IsNoHit
		self.SetMotionType = SetMotionType


class DemoCookPotCook:

	def __init__(self, Name, MaterialTargetBone, FairyTargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaterialTargetBone = MaterialTargetBone
		self.FairyTargetBone = FairyTargetBone


class DemoDelete:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoEnemyReset:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoFindPlayer:

	def __init__(self, Name, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class DemoForceSetPlayerSavePosAngle:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoGetItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoGetItemAnimStop:

	def __init__(self, Name, WaitASKeyName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitASKeyName = WaitASKeyName


class DemoGetWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoKokkoAngry:

	def __init__(self, Name, WaitTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime


class DemoMotorcyclePutMaterials:

	def __init__(self, Name, CloseSaddleFramesSincePut, FinishCookFramesSincePut, CloseSaddleFramesSincePutFairy, FinishCookFramesSincePutFairy, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseSaddleFramesSincePut = CloseSaddleFramesSincePut
		self.FinishCookFramesSincePut = FinishCookFramesSincePut
		self.CloseSaddleFramesSincePutFairy = CloseSaddleFramesSincePutFairy
		self.FinishCookFramesSincePutFairy = FinishCookFramesSincePutFairy


class DemoNoAnimDrivenTurn:

	def __init__(self, Name, IsUpdateTarget, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsFollowGround, IsRotEndFinish, IsFinishForceStopRot, IsChangeable, IsUpFollow, RotAccRatio, RotAccMaxSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUpdateTarget = IsUpdateTarget
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsFollowGround = IsFollowGround
		self.IsRotEndFinish = IsRotEndFinish
		self.IsFinishForceStopRot = IsFinishForceStopRot
		self.IsChangeable = IsChangeable
		self.IsUpFollow = IsUpFollow
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio


class DemoPlayerZoraRide:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoResetActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoResetBoneCtrl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoSweep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoTriggerToggleVisible:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoTurnToActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoVisibleOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoVisibleOn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DemoVoiceTrigger:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObjDLCSpurGearB01:

	def __init__(self, Name, IsReverse, IsTwoWayGear, StopCheckSpdRate, CheckSpdIdlingRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReverse = IsReverse
		self.IsTwoWayGear = IsTwoWayGear
		self.StopCheckSpdRate = StopCheckSpdRate
		self.CheckSpdIdlingRate = CheckSpdIdlingRate


class DgnObjDlcGondolaCreateTag:

	def __init__(self, Name, ActorName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorName = ActorName


class DgnObj_DLC_CWRotDirSwitch:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_CWRotDirSwitchOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_CogWheel_ASPlay:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_CogWheel_Reject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DgnObj_DLC_CogWheel_Rotate:

	def __init__(self, Name, TargetAngularDisplPerSec, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetAngularDisplPerSec = TargetAngularDisplPerSec


class DgnObj_DLC_DungeonRotate:

	def __init__(self, Name, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAxisIndex = RotateAxisIndex


class Die:

	def __init__(self, Name, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class DieAnm:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class DieAnmDropWeapon:

	def __init__(self, Name, WeaponDropSpeedY, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class DieAnmKnockBack:

	def __init__(self, Name, ASName, IsDropWeapon, WeaponDropSpeedY, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsDropWeapon = IsDropWeapon
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class DieHomeRun:

	def __init__(self, Name, ToStarHeight, FallHeight, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ToStarHeight = ToStarHeight
		self.FallHeight = FallHeight
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class DirectToWindDirection:

	def __init__(self, Name, FrontDir, UpDir, RotSpeed, RotMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FrontDir = FrontDir
		self.UpDir = UpDir
		self.RotSpeed = RotSpeed
		self.RotMax = RotMax


class DisableAutoSavePausing:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DisappearDeathCounter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DisappearNumDungeonClearSeal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DisappearNumHeroSeal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DisappearNumKorokNuts:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DisappearNumTargets:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DoorOpenAndClose:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DoubleAttack:

	def __init__(self, Name, CloseDist, WeaponIdx, Speed, RotSpd, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.WeaponIdx = WeaponIdx
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle


class DownSwingAttack:

	def __init__(self, Name, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, JustAvoidCheckLength, JustAvoidCheckAngle, LoopTime, LoopTimeRand, WeaponIdx, IsSpecialAttack, SpecialAttackRadius, SpineControlOffsetY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.JustAvoidCheckLength = JustAvoidCheckLength
		self.JustAvoidCheckAngle = JustAvoidCheckAngle
		self.LoopTime = LoopTime
		self.LoopTimeRand = LoopTimeRand
		self.WeaponIdx = WeaponIdx
		self.IsSpecialAttack = IsSpecialAttack
		self.SpecialAttackRadius = SpecialAttackRadius
		self.SpineControlOffsetY = SpineControlOffsetY


class DownloadAlbum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DownloadPictureBook:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DownloadRemainsMap:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DownloadShiekSensor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DownloadShiekSensorMoveIcon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DragonChemicalBall:

	def __init__(self, Name, Life, HitScale, Gravity, HomingPower, HomingDistance, HomingTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Life = Life
		self.HitScale = HitScale
		self.Gravity = Gravity
		self.HomingPower = HomingPower
		self.HomingDistance = HomingDistance
		self.HomingTime = HomingTime


class DragonFixPlacement:

	def __init__(self, Name, Rotate, Position, BlendStartFrame, BlendStartRate, BlendTime, HeadFixedModeTime, RailAdjustModeTime, CameraVibStartFrame, CameraVibLoop, CameraVibPower, CameraVibRange, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Rotate = Rotate
		self.Position = Position
		self.BlendStartFrame = BlendStartFrame
		self.BlendStartRate = BlendStartRate
		self.BlendTime = BlendTime
		self.HeadFixedModeTime = HeadFixedModeTime
		self.RailAdjustModeTime = RailAdjustModeTime
		self.CameraVibStartFrame = CameraVibStartFrame
		self.CameraVibLoop = CameraVibLoop
		self.CameraVibPower = CameraVibPower
		self.CameraVibRange = CameraVibRange
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class DragonFollow:

	def __init__(self, Name, DungeonName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DungeonName = DungeonName


class DragonItemInCarryBox:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DragonItemShootUp:

	def __init__(self, Name, FlyAwaySpeed, ContactSpeedDownXZ, ContactSpeedDownY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FlyAwaySpeed = FlyAwaySpeed
		self.ContactSpeedDownXZ = ContactSpeedDownXZ
		self.ContactSpeedDownY = ContactSpeedDownY


class DragonMoveTo:

	def __init__(self, Name, RollMax, RollSpeed, RollMaxSpeed, RollAmount, ASName, RestoreUp, BackAdjustAngle, BackAdjustRestoreUp, FixAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RollMax = RollMax
		self.RollSpeed = RollSpeed
		self.RollMaxSpeed = RollMaxSpeed
		self.RollAmount = RollAmount
		self.ASName = ASName
		self.RestoreUp = RestoreUp
		self.BackAdjustAngle = BackAdjustAngle
		self.BackAdjustRestoreUp = BackAdjustRestoreUp
		self.FixAngle = FixAngle


class DragonPlayASForDemo:

	def __init__(self, Name, Position, Rotate, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Position = Position
		self.Rotate = Rotate
		self.AnimeDrivenSettings = AnimeDrivenSettings


class DragonReleaseGrudgeForDemo:

	def __init__(self, Name, ReleaseTime, HeadTransSmoothStartFrame, HeadTransSmoothEndFrame, HeadTransSmoothRate, HeadTransSmoothSklRootRate, Position, Rotate, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReleaseTime = ReleaseTime
		self.HeadTransSmoothStartFrame = HeadTransSmoothStartFrame
		self.HeadTransSmoothEndFrame = HeadTransSmoothEndFrame
		self.HeadTransSmoothRate = HeadTransSmoothRate
		self.HeadTransSmoothSklRootRate = HeadTransSmoothSklRootRate
		self.Position = Position
		self.Rotate = Rotate
		self.AnimeDrivenSettings = AnimeDrivenSettings


class DropBreakWeaponUnEquiped:

	def __init__(self, Name, BoundNum, KillTimer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoundNum = BoundNum
		self.KillTimer = KillTimer


class DropCreateForReplace:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DropWeapon:

	def __init__(self, Name, WeaponDropSpeedXZ, WeaponDropSpeedY, WeaponIdx, AngleOffsetY, ChemReset, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponIdx = WeaponIdx
		self.AngleOffsetY = AngleOffsetY
		self.ChemReset = ChemReset
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class DrowningDeath:

	def __init__(self, Name, PosBaseRagdollRbName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosBaseRagdollRbName = PosBaseRagdollRbName


class DummyAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DummyDropTable:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DummyTriggerAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DunegonRotateWait:

	def __init__(self, Name, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAxisIndex = RotateAxisIndex


class DungeonEntranceASPlay:

	def __init__(self, Name, SetDgnName, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SetDgnName = SetDgnName
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class DungeonMove:

	def __init__(self, Name, Accel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Accel = Accel


class DungeonMoveAlwaysVibrateCam:

	def __init__(self, Name, IsSilentOnSuccess, Accel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSilentOnSuccess = IsSilentOnSuccess
		self.Accel = Accel


class DungeonMoveReset:

	def __init__(self, Name, Accel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Accel = Accel


class DungeonRotate:

	def __init__(self, Name, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotate2Target:

	def __init__(self, Name, DgnRotDir, RotSpAccel, RotSpSlowDown, RotSpSlowDownTh, MinRotSp, RotReverseSlowDown, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DgnRotDir = DgnRotDir
		self.RotSpAccel = RotSpAccel
		self.RotSpSlowDown = RotSpSlowDown
		self.RotSpSlowDownTh = RotSpSlowDownTh
		self.MinRotSp = MinRotSp
		self.RotReverseSlowDown = RotReverseSlowDown
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateAccel:

	def __init__(self, Name, IsSlowDown, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSlowDown = IsSlowDown
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateApp:

	def __init__(self, Name, RotDirType, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotDirType = RotDirType
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateCont:

	def __init__(self, Name, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateGyro:

	def __init__(self, Name, SlerpRatio, IsUseInstParamSlerpRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlerpRatio = SlerpRatio
		self.IsUseInstParamSlerpRatio = IsUseInstParamSlerpRatio


class DungeonRotateInOrder:

	def __init__(self, Name, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateShuttle:

	def __init__(self, Name, RotDir, RotateAxisIndex, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotDir = RotDir
		self.RotateAxisIndex = RotateAxisIndex


class DungeonRotateSymmetry:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class DynamicAttackPowerExplode:

	def __init__(self, Name, AttackPower, MinDamage, PlayerDamage, SizeUpTime, ExplodeTime, UseDefaultEffect, IsDelete, IsDamageGuarantee, AttackIntensity, IsVanish, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPower = AttackPower
		self.MinDamage = MinDamage
		self.PlayerDamage = PlayerDamage
		self.SizeUpTime = SizeUpTime
		self.ExplodeTime = ExplodeTime
		self.UseDefaultEffect = UseDefaultEffect
		self.IsDelete = IsDelete
		self.IsDamageGuarantee = IsDamageGuarantee
		self.AttackIntensity = AttackIntensity
		self.IsVanish = IsVanish


class DynamicFireWood:

	def __init__(self, Name, ChemicalRigidOn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChemicalRigidOn = ChemicalRigidOn


class Eat:

	def __init__(self, Name, IsHeal, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsHeal = IsHeal
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class EatAndHeal:

	def __init__(self, Name, MinFramesPlayWaitAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinFramesPlayWaitAS = MinFramesPlayWaitAS


class EatForSunazarashiSPC:

	def __init__(self, Name, TargetDirToStickX, TargetDistOffset, TargetDistToStickY, MaxStickXForEat, MaxStickYForEat, DelayFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetDirToStickX = TargetDirToStickX
		self.TargetDistOffset = TargetDistOffset
		self.TargetDistToStickY = TargetDistToStickY
		self.MaxStickXForEat = MaxStickXForEat
		self.MaxStickYForEat = MaxStickYForEat
		self.DelayFrames = DelayFrames


class EatWithAS:

	def __init__(self, Name, ASName, IsHeal, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsHeal = IsHeal
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ElectricAttack:

	def __init__(self, Name, Voltage, MaxTimer, MaxKeepTimer, HitAfterTime, ElectricActorName, ElectricActorKey, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Voltage = Voltage
		self.MaxTimer = MaxTimer
		self.MaxKeepTimer = MaxKeepTimer
		self.HitAfterTime = HitAfterTime
		self.ElectricActorName = ElectricActorName
		self.ElectricActorKey = ElectricActorKey
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ElectricBlownOff:

	def __init__(self, Name, Voltage, MaxTimer, MaxKeepTimer, ElectricActorName, ElectricActorKey, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Voltage = Voltage
		self.MaxTimer = MaxTimer
		self.MaxKeepTimer = MaxKeepTimer
		self.ElectricActorName = ElectricActorName
		self.ElectricActorKey = ElectricActorKey
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class ElectricCableEnergized:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ElectricDie:

	def __init__(self, Name, Voltage, MaxTimer, MaxKeepTimer, ElectricActorName, ElectricActorKey, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Voltage = Voltage
		self.MaxTimer = MaxTimer
		self.MaxKeepTimer = MaxKeepTimer
		self.ElectricActorName = ElectricActorName
		self.ElectricActorKey = ElectricActorKey
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class ElectricParalysis:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class EmitEffectLoopAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EmitElectricWaterBall:

	def __init__(self, Name, ActorName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorName = ActorName


class EndChangeableASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class EnemyAreaInOutSendMessage:

	def __init__(self, Name, MessageID, BufferNum, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MessageID = MessageID
		self.BufferNum = BufferNum


class EnemyChangeWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EnemyFortressChatCall:

	def __init__(self, Name, TryNum, TimeOut, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TryNum = TryNum
		self.TimeOut = TimeOut


class EnemyFortressChatSpeak:

	def __init__(self, Name, TryNum, TimeOut, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TryNum = TryNum
		self.TimeOut = TimeOut


class EnemyFortressChatTurn:

	def __init__(self, Name, TryNum, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TryNum = TryNum


class EnemyFortressSimpleAction:

	def __init__(self, Name, NoRequestTime, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoRequestTime = NoRequestTime
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class EnemyRigidBodyDie:

	def __init__(self, Name, Speed, RiseSpeed, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RiseSpeed = RiseSpeed
		self.ASName = ASName


class EnemyRigidBodyFreeFallDie:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class EnemyRigidBodySpinDie:

	def __init__(self, Name, Speed, RiseSpeed, ASName, RotSpeed, IsFinishedByBgHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RiseSpeed = RiseSpeed
		self.ASName = ASName
		self.RotSpeed = RotSpeed
		self.IsFinishedByBgHit = IsFinishedByBgHit


class EnemyRushAttack:

	def __init__(self, Name, ASKeyName, Speed, UpdateTargetPosInterval, DisableUpdateTargetRadius, GoalDistanceTolerance, MovePredictionRate, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.UpdateTargetPosInterval = UpdateTargetPosInterval
		self.DisableUpdateTargetRadius = DisableUpdateTargetRadius
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.MovePredictionRate = MovePredictionRate
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class EnvSeEmitPointBirdPlayAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EnvSeEmitPointInsectPlayAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EnvSetLensFlare:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipDisplay:

	def __init__(self, Name, SwordEquipNode, LSwordEquipNode, SpearEquipNode, BowEquipNode, ShieldEquipNode, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SwordEquipNode = SwordEquipNode
		self.LSwordEquipNode = LSwordEquipNode
		self.SpearEquipNode = SpearEquipNode
		self.BowEquipNode = BowEquipNode
		self.ShieldEquipNode = ShieldEquipNode


class EquipDisplayCreate:

	def __init__(self, Name, SwordEquipNode, LSwordEquipNode, SpearEquipNode, BowEquipNode, ShieldEquipNode, XLinkKey, DelayTimer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SwordEquipNode = SwordEquipNode
		self.LSwordEquipNode = LSwordEquipNode
		self.SpearEquipNode = SpearEquipNode
		self.BowEquipNode = BowEquipNode
		self.ShieldEquipNode = ShieldEquipNode
		self.XLinkKey = XLinkKey
		self.DelayTimer = DelayTimer


class EquipDisplayGet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedASPlay:

	def __init__(self, Name, AS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS


class EquipedAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedChemicalWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedDeadlyBlowWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedDefaultWindWeapon:

	def __init__(self, Name, WindRadius, WindRadiusLarge, WindSpeed, WindSpeedLarge, WindSpeedRate1, WindSpeedRate2, WindSpeedRate3, WindLength, CapsuleMaxSpeed, WindReduceRate, WindReduceRateLarge, WindFlyingDist, WindFlyingDistLarge, WindFlyingDistRate1, WindFlyingDistRate2, WindFlyingDistRate3, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WindRadius = WindRadius
		self.WindRadiusLarge = WindRadiusLarge
		self.WindSpeed = WindSpeed
		self.WindSpeedLarge = WindSpeedLarge
		self.WindSpeedRate1 = WindSpeedRate1
		self.WindSpeedRate2 = WindSpeedRate2
		self.WindSpeedRate3 = WindSpeedRate3
		self.WindLength = WindLength
		self.CapsuleMaxSpeed = CapsuleMaxSpeed
		self.WindReduceRate = WindReduceRate
		self.WindReduceRateLarge = WindReduceRateLarge
		self.WindFlyingDist = WindFlyingDist
		self.WindFlyingDistLarge = WindFlyingDistLarge
		self.WindFlyingDistRate1 = WindFlyingDistRate1
		self.WindFlyingDistRate2 = WindFlyingDistRate2
		self.WindFlyingDistRate3 = WindFlyingDistRate3


class EquipedOptionalWeaponAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedQuiver:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EquipedRod:

	def __init__(self, Name, MagicCreateYOffset, MagicShootVelOffset, IsAxisYTop, IsCreateWeaponPosOffset, CreatePosOffset, AxisYAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MagicCreateYOffset = MagicCreateYOffset
		self.MagicShootVelOffset = MagicShootVelOffset
		self.IsAxisYTop = IsAxisYTop
		self.IsCreateWeaponPosOffset = IsCreateWeaponPosOffset
		self.CreatePosOffset = CreatePosOffset
		self.AxisYAngle = AxisYAngle


class EquipedWeaponChild:

	def __init__(self, Name, IsChangeScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeScale = IsChangeScale


class EquipedWithScale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Escape:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class EscapeBackTurn:

	def __init__(self, Name, MoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed


class EventAddGameDataIntAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAddGameDataToRupeeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAppearCheckPointNum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAppearFlyDistance:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAppearGolfCount:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAppearRaceResult:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAppearRupeeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAutoSaveAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventAutoSaveAtGameClear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventBgmCtrlAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventBgmStartAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventBgmStartAndKeepAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventBgmStopAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventBind:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCallDemoAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCancelEndAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCancelGet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCancelSleepTargetActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCancelStartAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventChangeFadeColor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventChangeShadowNearAndFar:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCheckAndCreateEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCloseMessageTipsAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCloudShadowOnOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventControlRupeeUI:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventCreateParaShawlSetToPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisableContactIdle:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisableContactLayerTrigger:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisableMiniGameTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisappearCheckPointNum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisappearFlyDistance:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisappearGolfCount:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDisappearRaceResult:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDoorOpenAndClose:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventDummyAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventEnableModelDraw:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventEquipLastSetItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventFadeIn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventFadeOut:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventFireControl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventFlagOFFAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventFlagONAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventHoverNullASPlay:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventIncreaseFameAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventIncreaseGameDataIntAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventIncreasePorchItemAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventIncreaseRupeeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventInitTalkAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventLoopEndAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameFinish:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameRetire:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameStart:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameTimeMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventMiniGameTimerWrite:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventOffWaitRevivalAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventOnWaitRevivalAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventOpenGetDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventOpenGetWeaponDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventOpenMessageTips:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPickOutFromPorch:

	def __init__(self, Name, PickOutItemType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PickOutItemType = PickOutItemType


class EventPlayMovieAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiActorName:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiBossHpAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiBossHpDamage:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiOPTextAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiOneTimeAnimAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiScreenAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiStaffRoll:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPlayUiStaffRollImage:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventPrizeSuccess:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRecoverPlayerCondition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRecoverPlayerEnergy:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRecoverPlayerLife:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRegisterToDeathConter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRegisterToGetCounter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventResetQuestAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventRollbackQuestAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSendCatchWeaponMsgToPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetAddFogOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetAttentionForbidSale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetCharAmbientScale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetCharaMainLightScale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetCloudShadowMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetCloudShadowPos:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetDiffuseAttenuate:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetDirectionalLight:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetDirectionalLightYang:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetDynamic:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetEnableGrass:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetFixed:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetFocusDist:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetFogDirect:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetGameDataFloatAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetGameDataIntAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetGameDataStringAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetItemDataToPouch:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetMoonType:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetPaletteType:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetRainSplashRatio:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetSkyPaletteType:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetWeather:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSetYfogRatio:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSleepTargetActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventSuccessGet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventTalkEndAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventTrigNullASPlay:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventUnregisterFromDeathCounter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventUnregisterFromGetCounter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventUpdateMiniGameBestScore:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventVariableFadeIn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventVariableFadeOut:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventWaitFrameAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class EventWatchCannonHit:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ExitGame:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ExpandChemicalField:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ExpandSensor:

	def __init__(self, Name, AtkAttrType, AtkType, OffLength, OnLength, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkAttrType = AtkAttrType
		self.AtkType = AtkType
		self.OffLength = OffLength
		self.OnLength = OnLength


class ExpandSensorSlowly:

	def __init__(self, Name, AtkAttrType, AtkType, OffLength, OnLength, AtExpandStep, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkAttrType = AtkAttrType
		self.AtkType = AtkType
		self.OffLength = OffLength
		self.OnLength = OnLength
		self.AtExpandStep = AtExpandStep


class Explode:

	def __init__(self, Name, SizeUpTime, ExplodeTime, UseDefaultEffect, IsDelete, IsDamageGuarantee, AttackIntensity, IsVanish, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SizeUpTime = SizeUpTime
		self.ExplodeTime = ExplodeTime
		self.UseDefaultEffect = UseDefaultEffect
		self.IsDelete = IsDelete
		self.IsDamageGuarantee = IsDamageGuarantee
		self.AttackIntensity = AttackIntensity
		self.IsVanish = IsVanish


class ExplodeReserved:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class FadeInOutWithOptions:

	def __init__(self, Name, FadeType, FadeStartFrame, FadeFinishFrame, ToggleAttention, ToggleAwareness, ToggleEffects, ToggleCollision, ToggleHorseOptions, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FadeType = FadeType
		self.FadeStartFrame = FadeStartFrame
		self.FadeFinishFrame = FadeFinishFrame
		self.ToggleAttention = ToggleAttention
		self.ToggleAwareness = ToggleAwareness
		self.ToggleEffects = ToggleEffects
		self.ToggleCollision = ToggleCollision
		self.ToggleHorseOptions = ToggleHorseOptions


class FadeoutDelete:

	def __init__(self, Name, FadeoutTime, DeleteType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FadeoutTime = FadeoutTime
		self.DeleteType = DeleteType


class Fall:

	def __init__(self, Name, ASName, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth


class FallAttack:

	def __init__(self, Name, ASName, AtkBodyName, WeaponIdx, Gravity, JustAvoidDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AtkBodyName = AtkBodyName
		self.WeaponIdx = WeaponIdx
		self.Gravity = Gravity
		self.JustAvoidDist = JustAvoidDist


class FallAttackWithAtAttr:

	def __init__(self, Name, AtAttr, AtAttrNoWeapon, ASName, AtkBodyName, WeaponIdx, Gravity, JustAvoidDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtAttr = AtAttr
		self.AtAttrNoWeapon = AtAttrNoWeapon
		self.ASName = ASName
		self.AtkBodyName = AtkBodyName
		self.WeaponIdx = WeaponIdx
		self.Gravity = Gravity
		self.JustAvoidDist = JustAvoidDist


class FireWood:

	def __init__(self, Name, ChemicalRigidOn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChemicalRigidOn = ChemicalRigidOn


class FirstRunelGrudgeDemo:

	def __init__(self, Name, Position, Rotate, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Position = Position
		self.Rotate = Rotate
		self.AnimeDrivenSettings = AnimeDrivenSettings


class FishOnGround:

	def __init__(self, Name, ASKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKey = ASKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class FixedMagneSliderBlock:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FixedMagneStick:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FixedOrConstraint:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Flint:

	def __init__(self, Name, Radius, Life, SetDelete, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.Life = Life
		self.SetDelete = SetDelete


class FloatDrownDeath:

	def __init__(self, Name, ASName, FloatDepth, FloatSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.FloatDepth = FloatDepth
		self.FloatSpeed = FloatSpeed


class FloatWait:

	def __init__(self, Name, ASKeyName, WaterEffectSpeedRate, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.WaterEffectSpeedRate = WaterEffectSpeedRate
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class FlowingDust:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FlyMove:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRotate, HorizontalFinRadius, TargetHeightOffset, RotRatio, VerticalFinLength, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.VerticalFinLength = VerticalFinLength


class FlyingBalloonObserverTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FlyingBirdDie:

	def __init__(self, Name, IsChangeStateFallOnce, EnableHitGroundCheckTimer, FallAS, OnGroundAS, IsCheckFallASFinished, IsIgnoreSameAS4Fall, IsIgnoreSameAS4OnGround, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, RiseSpeed, LastSpeedRatio, PosReduceRatioOnGround, RotReduceRatioOnGround, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeStateFallOnce = IsChangeStateFallOnce
		self.EnableHitGroundCheckTimer = EnableHitGroundCheckTimer
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.IsCheckFallASFinished = IsCheckFallASFinished
		self.IsIgnoreSameAS4Fall = IsIgnoreSameAS4Fall
		self.IsIgnoreSameAS4OnGround = IsIgnoreSameAS4OnGround
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.RiseSpeed = RiseSpeed
		self.LastSpeedRatio = LastSpeedRatio
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterBlownOff:

	def __init__(self, Name, PosReduceRatioOnGround, RotReduceRatioOnGround, Speed, RiseSpeed, FallAS, OnGroundAS, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.Speed = Speed
		self.RiseSpeed = RiseSpeed
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterBlownOffDie:

	def __init__(self, Name, PosReduceRatioOnGround, RotReduceRatioOnGround, Speed, RiseSpeed, FallAS, OnGroundAS, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.Speed = Speed
		self.RiseSpeed = RiseSpeed
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterDamage:

	def __init__(self, Name, FallAS, OnGroundAS, IsCheckFallASFinished, IsIgnoreSameAS4Fall, IsIgnoreSameAS4OnGround, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, RiseSpeed, LastSpeedRatio, PosReduceRatioOnGround, RotReduceRatioOnGround, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.IsCheckFallASFinished = IsCheckFallASFinished
		self.IsIgnoreSameAS4Fall = IsIgnoreSameAS4Fall
		self.IsIgnoreSameAS4OnGround = IsIgnoreSameAS4OnGround
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.RiseSpeed = RiseSpeed
		self.LastSpeedRatio = LastSpeedRatio
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterDie:

	def __init__(self, Name, FallAS, OnGroundAS, IsCheckFallASFinished, IsIgnoreSameAS4Fall, IsIgnoreSameAS4OnGround, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, RiseSpeed, LastSpeedRatio, PosReduceRatioOnGround, RotReduceRatioOnGround, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.IsCheckFallASFinished = IsCheckFallASFinished
		self.IsIgnoreSameAS4Fall = IsIgnoreSameAS4Fall
		self.IsIgnoreSameAS4OnGround = IsIgnoreSameAS4OnGround
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.RiseSpeed = RiseSpeed
		self.LastSpeedRatio = LastSpeedRatio
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterFreeFallDie:

	def __init__(self, Name, PosReduceRatioOnGround, RotReduceRatioOnGround, FallAS, OnGroundAS, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.FallAS = FallAS
		self.OnGroundAS = OnGroundAS
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterFreeFallEx:

	def __init__(self, Name, GravityScaleRate, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GravityScaleRate = GravityScaleRate
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterFreeze:

	def __init__(self, Name, StopTime, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopTime = StopTime
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FlyingCharacterFreezeDie:

	def __init__(self, Name, StopTime, PosReduceRatio, RotReduceRatio, IsControlRotation, IsSetBackLastState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopTime = StopTime
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.IsControlRotation = IsControlRotation
		self.IsSetBackLastState = IsSetBackLastState


class FollowAttack:

	def __init__(self, Name, RodAttackDelayTime, IsNoRodAttack, IsIgnoreSmallHit, JustAvoidAngle, JustAvoidBackDist, JustAvoidSideDist, WeaponIdx, ForceKillMode, IsRodDirHosei, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RodAttackDelayTime = RodAttackDelayTime
		self.IsNoRodAttack = IsNoRodAttack
		self.IsIgnoreSmallHit = IsIgnoreSmallHit
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidSideDist = JustAvoidSideDist
		self.WeaponIdx = WeaponIdx
		self.ForceKillMode = ForceKillMode
		self.IsRodDirHosei = IsRodDirHosei
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class FollowDungeonRotate:

	def __init__(self, Name, IsSetNoHit, IsChangeableOnEnter, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSetNoHit = IsSetNoHit
		self.IsChangeableOnEnter = IsChangeableOnEnter


class FollowDungeonRotateASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, IsSuccessEndOnASFinish, OnWaitRevival, OnLinkTagBasic, IsSetNoHit, IsChangeableOnEnter, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx
		self.IsSuccessEndOnASFinish = IsSuccessEndOnASFinish
		self.OnWaitRevival = OnWaitRevival
		self.OnLinkTagBasic = OnLinkTagBasic
		self.IsSetNoHit = IsSetNoHit
		self.IsChangeableOnEnter = IsChangeableOnEnter


class FollowIgniteToBonePos:

	def __init__(self, Name, BoneName, LocalOffSetX, LocalOffSetY, LocalOffSetZ, MemoryPartsName, IsIgnitePosYZero, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BoneName = BoneName
		self.LocalOffSetX = LocalOffSetX
		self.LocalOffSetY = LocalOffSetY
		self.LocalOffSetZ = LocalOffSetZ
		self.MemoryPartsName = MemoryPartsName
		self.IsIgnitePosYZero = IsIgnitePosYZero
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class FollowIgniteToSelfPos:

	def __init__(self, Name, MemoryPartsName, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MemoryPartsName = MemoryPartsName
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class FootStepCalcOn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForbidComeback:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForbidSettingInstEventFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceChangeAction:

	def __init__(self, Name, Tree, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Tree = Tree


class ForceEndPlayerSlow:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceGetUpFreeze:

	def __init__(self, Name, ASName, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ForceGetUpWaterFloatFreeze:

	def __init__(self, Name, ASName, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class ForceMarkPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceMasterSwordFakeMode:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceOffMagneGrabbed:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceOpenMainScreen:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceRagdollOffFreeze:

	def __init__(self, Name, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ForceRagdollOffWaterFloatFreeze:

	def __init__(self, Name, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class ForceSetMtxFromPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceSetPlayerRestartPosAngle:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForceSystemFadeOut:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForestGiantWakeUp:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class ForkAITreeValWeakPointTimer:

	def __init__(self, Name, Timer, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Timer = Timer
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkAITreeVariableMove:

	def __init__(self, Name, IsChangeable, IsSuccessEndOnArrive, ArrivedRadius, TargetSpeed, RotSlerpRate, IsKeepDistFromGround, KeepDistFromGround, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeable = IsChangeable
		self.IsSuccessEndOnArrive = IsSuccessEndOnArrive
		self.ArrivedRadius = ArrivedRadius
		self.TargetSpeed = TargetSpeed
		self.RotSlerpRate = RotSlerpRate
		self.IsKeepDistFromGround = IsKeepDistFromGround
		self.KeepDistFromGround = KeepDistFromGround


class ForkASHoldLegTurn:

	def __init__(self, Name, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, RotBaseBoneName, IsFixBoneWithGround, TargetPosNoUpdateArea, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.RotBaseBoneName = RotBaseBoneName
		self.IsFixBoneWithGround = IsFixBoneWithGround
		self.TargetPosNoUpdateArea = TargetPosNoUpdateArea


class ForkASHoldLinearMove:

	def __init__(self, Name, MoveDir, MoveSpeed, RotRestRatio, PosRestRatio, GravityTransReduce, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveDir = MoveDir
		self.MoveSpeed = MoveSpeed
		self.RotRestRatio = RotRestRatio
		self.PosRestRatio = PosRestRatio
		self.GravityTransReduce = GravityTransReduce


class ForkASPlay:

	def __init__(self, Name, ASName, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, FirstRandomRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.FirstRandomRatio = FirstRandomRatio


class ForkASTrgAerialTurn:

	def __init__(self, Name, PosStayRatio, RotStayRatio, AngSpd, IsOnASEventChangeable, IsUpdateRotSpd, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosStayRatio = PosStayRatio
		self.RotStayRatio = RotStayRatio
		self.AngSpd = AngSpd
		self.IsOnASEventChangeable = IsOnASEventChangeable
		self.IsUpdateRotSpd = IsUpdateRotSpd


class ForkASTrgChargeArrow:

	def __init__(self, Name, WeaponIdx, IsEndState, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IsEndState = IsEndState
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkASTrgDeleteChild:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkASTrgDeleteEquip:

	def __init__(self, Name, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx


class ForkASTrgEmitChmFieldPos:

	def __init__(self, Name, OffsetPos, EmitIntervalTime, PartsKey, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, ActorPowerScale, XLinkKey, AtTarget, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetPos = OffsetPos
		self.EmitIntervalTime = EmitIntervalTime
		self.PartsKey = PartsKey
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.ActorPowerScale = ActorPowerScale
		self.XLinkKey = XLinkKey
		self.AtTarget = AtTarget
		self.AtDirType = AtDirType


class ForkASTrgEmitShockWaveAtEnter:

	def __init__(self, Name, OffsetPos, ShockWaveActorName, ShockWavePartsKey, Power, MaxScale, ScaleTime, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, EmitIntervalTime, IsHeavy, AtMinDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetPos = OffsetPos
		self.ShockWaveActorName = ShockWaveActorName
		self.ShockWavePartsKey = ShockWavePartsKey
		self.Power = Power
		self.MaxScale = MaxScale
		self.ScaleTime = ScaleTime
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.EmitIntervalTime = EmitIntervalTime
		self.IsHeavy = IsHeavy
		self.AtMinDamage = AtMinDamage


class ForkASTrgEmitShockWavePos:

	def __init__(self, Name, OffsetPos, ShockWaveActorName, ShockWavePartsKey, Power, MaxScale, ScaleTime, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, EmitIntervalTime, IsHeavy, AtMinDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetPos = OffsetPos
		self.ShockWaveActorName = ShockWaveActorName
		self.ShockWavePartsKey = ShockWavePartsKey
		self.Power = Power
		self.MaxScale = MaxScale
		self.ScaleTime = ScaleTime
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.EmitIntervalTime = EmitIntervalTime
		self.IsHeavy = IsHeavy
		self.AtMinDamage = AtMinDamage


class ForkASTrgForceDirAerialTurn:

	def __init__(self, Name, Dir, PosStayRatio, RotStayRatio, AngSpd, IsOnASEventChangeable, IsUpdateRotSpd, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dir = Dir
		self.PosStayRatio = PosStayRatio
		self.RotStayRatio = RotStayRatio
		self.AngSpd = AngSpd
		self.IsOnASEventChangeable = IsOnASEventChangeable
		self.IsUpdateRotSpd = IsUpdateRotSpd


class ForkASTrgGolemChemicalReset:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkASTrgHorseParamUse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkASTrgRemainsHowl:

	def __init__(self, Name, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkASTrgShootArrow:

	def __init__(self, Name, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, IsEndState, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.IsEndState = IsEndState
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkASTrgShootArrowWithBaseBone:

	def __init__(self, Name, BaseBoneName, FrontDirOfBaseBone, FrontDirAngle, IsAddTargetActorAimPosHeight, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, IsEndState, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseBoneName = BaseBoneName
		self.FrontDirOfBaseBone = FrontDirOfBaseBone
		self.FrontDirAngle = FrontDirAngle
		self.IsAddTargetActorAimPosHeight = IsAddTargetActorAimPosHeight
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.IsEndState = IsEndState
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkASTrgShootSkyArrow:

	def __init__(self, Name, BaseBoneName, FrontDirOfBaseBone, WeaponIdx, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseBoneName = BaseBoneName
		self.FrontDirOfBaseBone = FrontDirOfBaseBone
		self.WeaponIdx = WeaponIdx
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkASTrgStepMove:

	def __init__(self, Name, CloseDist, Speed, RotSpd, WeaponIdx, FinishDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.WeaponIdx = WeaponIdx
		self.FinishDist = FinishDist


class ForkASTrgTurnGround:

	def __init__(self, Name, Axis, SpeedBasePosRatio, CtrlOffset, OnAfterGroundRotAngle, CtrlAngleOffset, ActMoveVec, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Axis = Axis
		self.SpeedBasePosRatio = SpeedBasePosRatio
		self.CtrlOffset = CtrlOffset
		self.OnAfterGroundRotAngle = OnAfterGroundRotAngle
		self.CtrlAngleOffset = CtrlAngleOffset
		self.ActMoveVec = ActMoveVec


class ForkASTrgWeaponDrop:

	def __init__(self, Name, WeaponIdx1, WeaponIdx2, WeaponIdx3, WeaponIdx4, IsKeepRemind, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx1 = WeaponIdx1
		self.WeaponIdx2 = WeaponIdx2
		self.WeaponIdx3 = WeaponIdx3
		self.WeaponIdx4 = WeaponIdx4
		self.IsKeepRemind = IsKeepRemind


class ForkAddCalcScaleMapUnit:

	def __init__(self, Name, StartRate, AddRate, MinAddScaleRate, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartRate = StartRate
		self.AddRate = AddRate
		self.MinAddScaleRate = MinAddScaleRate
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkAddLinearImpulse:

	def __init__(self, Name, Direction, Power, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Direction = Direction
		self.Power = Power


class ForkAerialAcrobatics:

	def __init__(self, Name, SpeedKeepRatio, RotSpeedKeepRatio, MinGravityScale, GravityPer, RetGravityPer, IsStopGravitySpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedKeepRatio = SpeedKeepRatio
		self.RotSpeedKeepRatio = RotSpeedKeepRatio
		self.MinGravityScale = MinGravityScale
		self.GravityPer = GravityPer
		self.RetGravityPer = RetGravityPer
		self.IsStopGravitySpeed = IsStopGravitySpeed


class ForkAllowReactionLift:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkAlwayForceGetUpVelocityDir:

	def __init__(self, Name, RotRatio, RotSpdMin, RotSpdMax, IsUseCRBOffsetUnit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.RotSpdMin = RotSpdMin
		self.RotSpdMax = RotSpdMax
		self.IsUseCRBOffsetUnit = IsUseCRBOffsetUnit


class ForkAlwaysColTgOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkAlwaysForceGetUp:

	def __init__(self, Name, RotRatio, RotSpdMin, RotSpdMax, IsUseCRBOffsetUnit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.RotSpdMin = RotSpdMin
		self.RotSpdMax = RotSpdMax
		self.IsUseCRBOffsetUnit = IsUseCRBOffsetUnit


class ForkAlwaysForceGetUpWithOffset:

	def __init__(self, Name, RotCenterPos, RotRatio, RotSpdMin, RotSpdMax, IsUseCRBOffsetUnit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotCenterPos = RotCenterPos
		self.RotRatio = RotRatio
		self.RotSpdMin = RotSpdMin
		self.RotSpdMax = RotSpdMax
		self.IsUseCRBOffsetUnit = IsUseCRBOffsetUnit


class ForkAlwaysHoverTurn:

	def __init__(self, Name, IsUpdateTarget, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsFollowGround, IsRotEndFinish, IsFinishForceStopRot, IsChangeable, IsUpFollow, RotAccRatio, RotAccMaxSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUpdateTarget = IsUpdateTarget
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsFollowGround = IsFollowGround
		self.IsRotEndFinish = IsRotEndFinish
		self.IsFinishForceStopRot = IsFinishForceStopRot
		self.IsChangeable = IsChangeable
		self.IsUpFollow = IsUpFollow
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio


class ForkAlwaysOneColTgOff:

	def __init__(self, Name, RigidBodyName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyName = RigidBodyName


class ForkAlwaysRotDownGr:

	def __init__(self, Name, GroundRotAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GroundRotAngle = GroundRotAngle


class ForkAlwaysRotate:

	def __init__(self, Name, RotSpd, RotAxis, OnEndForceStop, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.RotAxis = RotAxis
		self.OnEndForceStop = OnEndForceStop


class ForkAlwaysSetModelEffect:

	def __init__(self, Name, Timer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Timer = Timer


class ForkAlwaysTargetVerticalRotate:

	def __init__(self, Name, RotSpdMax, RotSpdRatio, OtherAxis, IsUpdateTargetPos, IsIgnoreY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpdMax = RotSpdMax
		self.RotSpdRatio = RotSpdRatio
		self.OtherAxis = OtherAxis
		self.IsUpdateTargetPos = IsUpdateTargetPos
		self.IsIgnoreY = IsIgnoreY


class ForkAlwaysTurn:

	def __init__(self, Name, IsUpdateTarget, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsFollowGround, IsRotEndFinish, IsFinishForceStopRot, IsChangeable, IsUpFollow, RotAccRatio, RotAccMaxSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUpdateTarget = IsUpdateTarget
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsFollowGround = IsFollowGround
		self.IsRotEndFinish = IsRotEndFinish
		self.IsFinishForceStopRot = IsFinishForceStopRot
		self.IsChangeable = IsChangeable
		self.IsUpFollow = IsUpFollow
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio


class ForkAlwaysTurnUDLimit:

	def __init__(self, Name, LimitUD, IsUpdateTarget, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsFollowGround, IsRotEndFinish, IsFinishForceStopRot, IsChangeable, IsUpFollow, RotAccRatio, RotAccMaxSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LimitUD = LimitUD
		self.IsUpdateTarget = IsUpdateTarget
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsFollowGround = IsFollowGround
		self.IsRotEndFinish = IsRotEndFinish
		self.IsFinishForceStopRot = IsFinishForceStopRot
		self.IsChangeable = IsChangeable
		self.IsUpFollow = IsUpFollow
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio


class ForkAnimDriveFreeMoving:

	def __init__(self, Name, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBone = TargetBone


class ForkAnimDriveMove:

	def __init__(self, Name, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBone = TargetBone


class ForkAnimDriveTurn:

	def __init__(self, Name, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBone = TargetBone


class ForkAnimReset:

	def __init__(self, Name, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkAnimalASPlay:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class ForkBattleNodeForAttackGround:

	def __init__(self, Name, AttackPosOffset, IsOffsetFromBaseBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPosOffset = AttackPosOffset
		self.IsOffsetFromBaseBone = IsOffsetFromBaseBone


class ForkBeastGanonMessageDialogCtrl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkBombIgniteCarriedByPlayer:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class ForkBoneControlFrontGround:

	def __init__(self, Name, TargetOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetOffset = TargetOffset


class ForkCapsuleWindFollow:

	def __init__(self, Name, Radius, Speed, Length, Dir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.Speed = Speed
		self.Length = Length
		self.Dir = Dir


class ForkCatchWeapon:

	def __init__(self, Name, WeaponIdx, IsNoGrabSuccess, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IsNoGrabSuccess = IsNoGrabSuccess


class ForkChemicalChuchuAttack:

	def __init__(self, Name, LandAtkRadius, LandAtkTime, AtDirString, IsImpulseLarge, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackType, ChmName1, AttackPowerScale, IsUseAttackParam, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LandAtkRadius = LandAtkRadius
		self.LandAtkTime = LandAtkTime
		self.AtDirString = AtDirString
		self.IsImpulseLarge = IsImpulseLarge
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackType = AttackType
		self.ChmName1 = ChmName1
		self.AttackPowerScale = AttackPowerScale
		self.IsUseAttackParam = IsUseAttackParam
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkClothOnOffASPlay:

	def __init__(self, Name, ASName, ClothOffASName, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ClothOffASName = ClothOffASName
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkDisableContactByPreAS:

	def __init__(self, Name, DisableTime, PreASName0, PreASName1, PreASName2, PreASName3, PreASName4, RigidBodyName0, RigidBodyName1, RigidBodyName2, RigidBodyName3, RigidBodyName4, RecoverDelayTimeMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisableTime = DisableTime
		self.PreASName0 = PreASName0
		self.PreASName1 = PreASName1
		self.PreASName2 = PreASName2
		self.PreASName3 = PreASName3
		self.PreASName4 = PreASName4
		self.RigidBodyName0 = RigidBodyName0
		self.RigidBodyName1 = RigidBodyName1
		self.RigidBodyName2 = RigidBodyName2
		self.RigidBodyName3 = RigidBodyName3
		self.RigidBodyName4 = RigidBodyName4
		self.RecoverDelayTimeMin = RecoverDelayTimeMin


class ForkDisableContactForAttack:

	def __init__(self, Name, RigidBodyName0, RigidBodyName1, RigidBodyName2, RigidBodyName3, RigidBodyName4, RecoverDelayTimeMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyName0 = RigidBodyName0
		self.RigidBodyName1 = RigidBodyName1
		self.RigidBodyName2 = RigidBodyName2
		self.RigidBodyName3 = RigidBodyName3
		self.RigidBodyName4 = RigidBodyName4
		self.RecoverDelayTimeMin = RecoverDelayTimeMin


class ForkDisableContactOnAtHitPlayer:

	def __init__(self, Name, RigidBodyName0, RigidBodyName1, RigidBodyName2, RigidBodyName3, RigidBodyName4, RecoverDelayTimeMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyName0 = RigidBodyName0
		self.RigidBodyName1 = RigidBodyName1
		self.RigidBodyName2 = RigidBodyName2
		self.RigidBodyName3 = RigidBodyName3
		self.RigidBodyName4 = RigidBodyName4
		self.RecoverDelayTimeMin = RecoverDelayTimeMin


class ForkDrawWeapon:

	def __init__(self, Name, WeaponIdx, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkDrawWeaponAtEnter:

	def __init__(self, Name, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx


class ForkDropGiantNecklace:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkDropWeaponWithSpeed:

	def __init__(self, Name, WeaponDropSpeedXZ, WeaponDropSpeedY, WeaponIdx, AngleOffsetY, ChemReset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponIdx = WeaponIdx
		self.AngleOffsetY = AngleOffsetY
		self.ChemReset = ChemReset


class ForkDrownTimer:

	def __init__(self, Name, Time, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.InWaterDepth = InWaterDepth


class ForkDynASPlay:

	def __init__(self, Name, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, FirstRandomRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.FirstRandomRatio = FirstRandomRatio


class ForkDynActorNoTargetSelf:

	def __init__(self, Name, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkEmitChmFieldByContact:

	def __init__(self, Name, RigidBodyName, EmitIntervalTime, PartsKey, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, ActorPowerScale, XLinkKey, AtTarget, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyName = RigidBodyName
		self.EmitIntervalTime = EmitIntervalTime
		self.PartsKey = PartsKey
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.ActorPowerScale = ActorPowerScale
		self.XLinkKey = XLinkKey
		self.AtTarget = AtTarget
		self.AtDirType = AtDirType


class ForkEmitChmFieldFromWeapon:

	def __init__(self, Name, WeaponIdx, SeqBank, TargetBone, EmitIntervalTime, PartsKey, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, ActorPowerScale, XLinkKey, AtTarget, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.EmitIntervalTime = EmitIntervalTime
		self.PartsKey = PartsKey
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.ActorPowerScale = ActorPowerScale
		self.XLinkKey = XLinkKey
		self.AtTarget = AtTarget
		self.AtDirType = AtDirType


class ForkEmitExpandChemicalField:

	def __init__(self, Name, PartsKey, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, ActorPowerScale, XLinkKey, AtTarget, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey = PartsKey
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.ActorPowerScale = ActorPowerScale
		self.XLinkKey = XLinkKey
		self.AtTarget = AtTarget
		self.AtDirType = AtDirType


class ForkEmitExpandFieldWithCreate:

	def __init__(self, Name, IsReuseActor, ScaleTime, IsSetPartsLink, PartsKey, Scale, AttackPower, AttackIntensity, IsUseAtCollision, AttackType, CutGrassType, ActorPowerScale, XLinkKey, AtTarget, AtDirType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReuseActor = IsReuseActor
		self.ScaleTime = ScaleTime
		self.IsSetPartsLink = IsSetPartsLink
		self.PartsKey = PartsKey
		self.Scale = Scale
		self.AttackPower = AttackPower
		self.AttackIntensity = AttackIntensity
		self.IsUseAtCollision = IsUseAtCollision
		self.AttackType = AttackType
		self.CutGrassType = CutGrassType
		self.ActorPowerScale = ActorPowerScale
		self.XLinkKey = XLinkKey
		self.AtTarget = AtTarget
		self.AtDirType = AtDirType


class ForkEmitShockWaveByContact:

	def __init__(self, Name, RigidBodyName, ShockWaveActorName, ShockWavePartsKey, Power, MaxScale, ScaleTime, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, EmitIntervalTime, IsHeavy, AtMinDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidBodyName = RigidBodyName
		self.ShockWaveActorName = ShockWaveActorName
		self.ShockWavePartsKey = ShockWavePartsKey
		self.Power = Power
		self.MaxScale = MaxScale
		self.ScaleTime = ScaleTime
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.EmitIntervalTime = EmitIntervalTime
		self.IsHeavy = IsHeavy
		self.AtMinDamage = AtMinDamage


class ForkEndByDistance:

	def __init__(self, Name, EndDist, WeaponIdx, EndMode, IsOnlyXZ, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndDist = EndDist
		self.WeaponIdx = WeaponIdx
		self.EndMode = EndMode
		self.IsOnlyXZ = IsOnlyXZ
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkEndByPartsActorEnd:

	def __init__(self, Name, PartsKey, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey = PartsKey
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkFixedAngleVacuumShootTarget:

	def __init__(self, Name, ShootOffset, ShootSpeedMin, ShootSpeedMax, ShootRotate, ShootRotSpeed, Angle, MaxNoiseDist, OffsetHeight, BaseNode, PartsKey, IsReuseBullet, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootOffset = ShootOffset
		self.ShootSpeedMin = ShootSpeedMin
		self.ShootSpeedMax = ShootSpeedMax
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.Angle = Angle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsKey = PartsKey
		self.IsReuseBullet = IsReuseBullet


class ForkFlyToTargetDirect:

	def __init__(self, Name, FinRadius, MoveSpd, OnEndForceStop, OnGround, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinRadius = FinRadius
		self.MoveSpd = MoveSpd
		self.OnEndForceStop = OnEndForceStop
		self.OnGround = OnGround


class ForkFollowGround:

	def __init__(self, Name, RotSpd, BaseRotRatio, UpdateTargetUpDirMinAngle, UpdateTargetUpDirRatio, UpdateFrameCountAfterNoMove, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.BaseRotRatio = BaseRotRatio
		self.UpdateTargetUpDirMinAngle = UpdateTargetUpDirMinAngle
		self.UpdateTargetUpDirRatio = UpdateTargetUpDirRatio
		self.UpdateFrameCountAfterNoMove = UpdateFrameCountAfterNoMove


class ForkForceGetUp:

	def __init__(self, Name, RotRatio, RotSpdMin, RotSpdMax, IsUseCRBOffsetUnit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.RotSpdMin = RotSpdMin
		self.RotSpdMax = RotSpdMax
		self.IsUseCRBOffsetUnit = IsUseCRBOffsetUnit


class ForkForceIgniteCarriedActor:

	def __init__(self, Name, GrabIdx, IsCheckAfterChildState, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrabIdx = GrabIdx
		self.IsCheckAfterChildState = IsCheckAfterChildState
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkFourFootActorLustGrass:

	def __init__(self, Name, WorldOffset, MaxRadius, MinRadius, Node1Name, Node2Name, Node3Name, Node4Name, RadSpd, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WorldOffset = WorldOffset
		self.MaxRadius = MaxRadius
		self.MinRadius = MinRadius
		self.Node1Name = Node1Name
		self.Node2Name = Node2Name
		self.Node3Name = Node3Name
		self.Node4Name = Node4Name
		self.RadSpd = RadSpd


class ForkFreeMoving:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkGanonAscendingCreateManage:

	def __init__(self, Name, CreateGrudgeName, MaxNum, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateGrudgeName = CreateGrudgeName
		self.MaxNum = MaxNum


class ForkGanonBeastAppearHolyWall:

	def __init__(self, Name, ShowDist, KeyName, AppearDist, EffectYOffset, BasePos, UiDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShowDist = ShowDist
		self.KeyName = KeyName
		self.AppearDist = AppearDist
		self.EffectYOffset = EffectYOffset
		self.BasePos = BasePos
		self.UiDist = UiDist


class ForkGanonBeastBeamShoot:

	def __init__(self, Name, BeamRange, MuzzleOffset, BeamBoneName, BeamActorKey, BeamActorName, BeamDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BeamRange = BeamRange
		self.MuzzleOffset = MuzzleOffset
		self.BeamBoneName = BeamBoneName
		self.BeamActorKey = BeamActorKey
		self.BeamActorName = BeamActorName
		self.BeamDir = BeamDir


class ForkGanonBeastHeadBarrier:

	def __init__(self, Name, BarrierRad, BarrierFront, BarrierBack, BarrierHeight, BarrierHeightMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BarrierRad = BarrierRad
		self.BarrierFront = BarrierFront
		self.BarrierBack = BarrierBack
		self.BarrierHeight = BarrierHeight
		self.BarrierHeightMax = BarrierHeightMax


class ForkGanonBeastWeakPointCheck:

	def __init__(self, Name, ASSlot, LastWeakCounter, LastWeakSlowEndSafeTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASSlot = ASSlot
		self.LastWeakCounter = LastWeakCounter
		self.LastWeakSlowEndSafeTime = LastWeakSlowEndSafeTime


class ForkGanonBeastWeakPointOff:

	def __init__(self, Name, TargetSlotIdx, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetSlotIdx = TargetSlotIdx
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkGanonBeastWeakPointOn:

	def __init__(self, Name, TargetSlotIdx, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetSlotIdx = TargetSlotIdx
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkGelDisableBodyRot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkGolemMaterialASPlay:

	def __init__(self, Name, ASName, TargetPartType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TargetPartType = TargetPartType


class ForkGravityScaleChange:

	def __init__(self, Name, Scale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Scale = Scale


class ForkHoldWeapon:

	def __init__(self, Name, WeaponIdx, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkHopInAir:

	def __init__(self, Name, HopHeight, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HopHeight = HopHeight
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkHover:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ForkHoverKeepRotateTurn:

	def __init__(self, Name, MinRotSpd, EndAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinRotSpd = MinRotSpd
		self.EndAngle = EndAngle


class ForkIgniteCarriedActor:

	def __init__(self, Name, GrabIdx, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrabIdx = GrabIdx
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkInWaterDropWeaponWithSpeed:

	def __init__(self, Name, InWaterDepth, OutWaterDepth, ChemReset, WeaponDropSpeedXZ, WeaponDropSpeedY, WeaponIdx, AngleOffsetY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.OutWaterDepth = OutWaterDepth
		self.ChemReset = ChemReset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponIdx = WeaponIdx
		self.AngleOffsetY = AngleOffsetY


class ForkJumpToTargetOnDownEnd:

	def __init__(self, Name, AngleDir, JumpDist, JumpHeight, LimitSpeed, EndGrSpeed, IsBasisByTarget, JumpMinDist, OnGround, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngleDir = AngleDir
		self.JumpDist = JumpDist
		self.JumpHeight = JumpHeight
		self.LimitSpeed = LimitSpeed
		self.EndGrSpeed = EndGrSpeed
		self.IsBasisByTarget = IsBasisByTarget
		self.JumpMinDist = JumpMinDist
		self.OnGround = OnGround


class ForkKnockBackNoRot:

	def __init__(self, Name, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class ForkLodNoCountTimer:

	def __init__(self, Name, CamDist, IsTrgStart, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CamDist = CamDist
		self.IsTrgStart = IsTrgStart
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkLodTimer:

	def __init__(self, Name, WaitFrame, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkLynelBreathShoot:

	def __init__(self, Name, AttackRatio, BreathSize, EnlargeTime, Range, Speed, ShootDir, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, PartsKey, IsReuseBullet, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRatio = AttackRatio
		self.BreathSize = BreathSize
		self.EnlargeTime = EnlargeTime
		self.Range = Range
		self.Speed = Speed
		self.ShootDir = ShootDir
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsKey = PartsKey
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkLynelDrawWeapon:

	def __init__(self, Name, ASName, WeaponIdx0, WeaponIdx1, SeqBank, TargetBone, ASWeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx0 = WeaponIdx0
		self.WeaponIdx1 = WeaponIdx1
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.ASWeaponIdx = ASWeaponIdx


class ForkLynelDrawWeaponASPlay:

	def __init__(self, Name, ASName, WeaponIdx0, WeaponIdx1, SeqBank, TargetBone, ASWeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx0 = WeaponIdx0
		self.WeaponIdx1 = WeaponIdx1
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.ASWeaponIdx = ASWeaponIdx


class ForkModelFadeOut:

	def __init__(self, Name, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkModelVisibleOff:

	def __init__(self, Name, UseFadeIn, UseASEvent, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseFadeIn = UseFadeIn
		self.UseASEvent = UseASEvent
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkMoveDistanceCheckByMapUnit:

	def __init__(self, Name, IsCheckOnlyXZ, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckOnlyXZ = IsCheckOnlyXZ
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkMultiSleep:

	def __init__(self, Name, PartsBaseName, Num, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsBaseName = PartsBaseName
		self.Num = Num


class ForkNeckOnlyRotateDynPosBasic:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkNeckRotateDynPosBasic:

	def __init__(self, Name, UseSimpleOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseSimpleOffset = UseSimpleOffset


class ForkNoCountActionReservedTimer:

	def __init__(self, Name, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkNoHitGroundCrawl:

	def __init__(self, Name, MaxSpeed, EndRadius, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.EndRadius = EndRadius


class ForkNoSlowTimer:

	def __init__(self, Name, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkNoWeaponAttack:

	def __init__(self, Name, TargetBone, SeqBank, IsImpulseLarge, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackType, ChmName1, AttackPowerScale, IsUseAttackParam, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBone = TargetBone
		self.SeqBank = SeqBank
		self.IsImpulseLarge = IsImpulseLarge
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackType = AttackType
		self.ChmName1 = ChmName1
		self.AttackPowerScale = AttackPowerScale
		self.IsUseAttackParam = IsUseAttackParam
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkNoWeaponAttackAllTime:

	def __init__(self, Name, AtDirString, IsImpulseLarge, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackType, ChmName1, AttackPowerScale, IsUseAttackParam, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtDirString = AtDirString
		self.IsImpulseLarge = IsImpulseLarge
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackType = AttackType
		self.ChmName1 = ChmName1
		self.AttackPowerScale = AttackPowerScale
		self.IsUseAttackParam = IsUseAttackParam
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkNoWeaponAttackAllTimeMinSet:

	def __init__(self, Name, MinDamage, AtDirString, IsImpulseLarge, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackType, ChmName1, AttackPowerScale, IsUseAttackParam, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinDamage = MinDamage
		self.AtDirString = AtDirString
		self.IsImpulseLarge = IsImpulseLarge
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackType = AttackType
		self.ChmName1 = ChmName1
		self.AttackPowerScale = AttackPowerScale
		self.IsUseAttackParam = IsUseAttackParam
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkNoWeaponAttackDirectParam:

	def __init__(self, Name, AttackPower, GuardBreakPower, Impulse, TargetBone, SeqBank, IsImpulseLarge, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackType, ChmName1, AttackPowerScale, IsUseAttackParam, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackPower = AttackPower
		self.GuardBreakPower = GuardBreakPower
		self.Impulse = Impulse
		self.TargetBone = TargetBone
		self.SeqBank = SeqBank
		self.IsImpulseLarge = IsImpulseLarge
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackType = AttackType
		self.ChmName1 = ChmName1
		self.AttackPowerScale = AttackPowerScale
		self.IsUseAttackParam = IsUseAttackParam
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkNoWeaponAttackParamWeapon:

	def __init__(self, Name, WeaponIdx, SeqBank, TargetBone, AtkBodyName, AttackIntensity, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.AtkBodyName = AtkBodyName
		self.AttackIntensity = AttackIntensity


class ForkOctarockEnterReloadWig:

	def __init__(self, Name, GrabIdx, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrabIdx = GrabIdx
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkOnEnterCharCtrlInvalid:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkOnEnterDropWeaponWithSpeed:

	def __init__(self, Name, ChemReset, WeaponDropSpeedXZ, WeaponDropSpeedY, WeaponIdx, AngleOffsetY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChemReset = ChemReset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponIdx = WeaponIdx
		self.AngleOffsetY = AngleOffsetY


class ForkOnEnterWeaponUse:

	def __init__(self, Name, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx


class ForkOnLeaveChildDelete:

	def __init__(self, Name, ForceDelete, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceDelete = ForceDelete


class ForkOnLeaveGolemChemReset:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkOnResetBasicSignalOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkOverrideStartNoDrawTimer:

	def __init__(self, Name, Time, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time


class ForkPreJump:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkRagdollOff:

	def __init__(self, Name, OffTiming, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffTiming = OffTiming


class ForkSandwormAtkCol:

	def __init__(self, Name, MinDamage, IsUseTossAt, IsColNoHitPlayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinDamage = MinDamage
		self.IsUseTossAt = IsUseTossAt
		self.IsColNoHitPlayer = IsColNoHitPlayer


class ForkSeparateThreeASPart:

	def __init__(self, Name, RootNode, Slot1StartNode, Slot2StartNode, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RootNode = RootNode
		self.Slot1StartNode = Slot1StartNode
		self.Slot2StartNode = Slot2StartNode


class ForkSeqNoWeaponAttack:

	def __init__(self, Name, IsImpulseLarge, AttackType, ExcludeAtkName0, ExcludeAtkName1, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsImpulseLarge = IsImpulseLarge
		self.AttackType = AttackType
		self.ExcludeAtkName0 = ExcludeAtkName0
		self.ExcludeAtkName1 = ExcludeAtkName1
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkSetComebackPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkSetCustomPallete:

	def __init__(self, Name, PalleteType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PalleteType = PalleteType


class ForkSetCustomWeather:

	def __init__(self, Name, WeatherType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeatherType = WeatherType


class ForkSetJustAvoid:

	def __init__(self, Name, JustAvoidAngleL, JustAvoidAngleR, JustAvoidDistFar, JustAvoidDistNear, WeaponIdx, IsAddRangeToFar, IsAddRangeToNear, TargetBone, SeqBank, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JustAvoidAngleL = JustAvoidAngleL
		self.JustAvoidAngleR = JustAvoidAngleR
		self.JustAvoidDistFar = JustAvoidDistFar
		self.JustAvoidDistNear = JustAvoidDistNear
		self.WeaponIdx = WeaponIdx
		self.IsAddRangeToFar = IsAddRangeToFar
		self.IsAddRangeToNear = IsAddRangeToNear
		self.TargetBone = TargetBone
		self.SeqBank = SeqBank


class ForkSetJustAvoidFromBone:

	def __init__(self, Name, TransBaseBoneName, RotBaseBoneName, BaseDir, JustAvoidAngleL, JustAvoidAngleR, JustAvoidDistFar, JustAvoidDistNear, WeaponIdx, IsAddRangeToFar, IsAddRangeToNear, TargetBone, SeqBank, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TransBaseBoneName = TransBaseBoneName
		self.RotBaseBoneName = RotBaseBoneName
		self.BaseDir = BaseDir
		self.JustAvoidAngleL = JustAvoidAngleL
		self.JustAvoidAngleR = JustAvoidAngleR
		self.JustAvoidDistFar = JustAvoidDistFar
		self.JustAvoidDistNear = JustAvoidDistNear
		self.WeaponIdx = WeaponIdx
		self.IsAddRangeToFar = IsAddRangeToFar
		self.IsAddRangeToNear = IsAddRangeToNear
		self.TargetBone = TargetBone
		self.SeqBank = SeqBank


class ForkSetSwarmMaterialAnimByDist:

	def __init__(self, Name, ApplyMaterialAnimNumPerFrame, ApplyMaterialAnimDist, MaterialAnimName, MaterialAnimFrame, SetState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ApplyMaterialAnimNumPerFrame = ApplyMaterialAnimNumPerFrame
		self.ApplyMaterialAnimDist = ApplyMaterialAnimDist
		self.MaterialAnimName = MaterialAnimName
		self.MaterialAnimFrame = MaterialAnimFrame
		self.SetState = SetState


class ForkSimpleGrab:

	def __init__(self, Name, CheckRadius, GrabIdx, IsNoGrabSuccess, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.IsNoGrabSuccess = IsNoGrabSuccess


class ForkSlipAndStop:

	def __init__(self, Name, PosReduceRatioForSlip, AngReduceRatioForSlip, PosReduceRatio, AngReduceRatio, UseLineCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatioForSlip = PosReduceRatioForSlip
		self.AngReduceRatioForSlip = AngReduceRatioForSlip
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.UseLineCheck = UseLineCheck


class ForkStalEnemyForceDamage:

	def __init__(self, Name, LifeRate, Damage, ASTrigType, DamageType, DamageAttr, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LifeRate = LifeRate
		self.Damage = Damage
		self.ASTrigType = ASTrigType
		self.DamageType = DamageType
		self.DamageAttr = DamageAttr


class ForkStalEnemyGrabOwnPart:

	def __init__(self, Name, SeqBank, TargetBone, BoneName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.BoneName = BoneName


class ForkStalEnemyHeadShot:

	def __init__(self, Name, AddVec, Speed, UseAddVec, RotVec, RotSpd, HeadBoneKey, VisibleCount, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddVec = AddVec
		self.Speed = Speed
		self.UseAddVec = UseAddVec
		self.RotVec = RotVec
		self.RotSpd = RotSpd
		self.HeadBoneKey = HeadBoneKey
		self.VisibleCount = VisibleCount


class ForkStalPartApplyDamageImpulse:

	def __init__(self, Name, MaxAddSpeed, SwordRate, SpearRate, LswordRate, ArrowRate, BombRate, GustRate, LargeAttackAddRate, MaxAddSpeedY, IsViewHitDir, RotSpd, FinRotate, RotAccRatio, RotAccMaxSpeedRatio, BaseRotRatio, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxAddSpeed = MaxAddSpeed
		self.SwordRate = SwordRate
		self.SpearRate = SpearRate
		self.LswordRate = LswordRate
		self.ArrowRate = ArrowRate
		self.BombRate = BombRate
		self.GustRate = GustRate
		self.LargeAttackAddRate = LargeAttackAddRate
		self.MaxAddSpeedY = MaxAddSpeedY
		self.IsViewHitDir = IsViewHitDir
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkStalPartBlownOff:

	def __init__(self, Name, BaseNodeName, ShootDir, ShootSpeed, LifeRate, ShootParts, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseNodeName = BaseNodeName
		self.ShootDir = ShootDir
		self.ShootSpeed = ShootSpeed
		self.LifeRate = LifeRate
		self.ShootParts = ShootParts


class ForkStop:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ForkStopWithNavCheck:

	def __init__(self, Name, PosReduceRatio, RotReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio


class ForkSwapPartsItemFromDropTable:

	def __init__(self, Name, PartsKey0, PartsKey1, PartsKey2, PartsKey3, PartsKey4, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
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
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkSwarmAttack:

	def __init__(self, Name, IsAttackOnce, AttackIntensity, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsAttackOnce = IsAttackOnce
		self.AttackIntensity = AttackIntensity


class ForkTimer:

	def __init__(self, Name, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkTimerForceResetCondition:

	def __init__(self, Name, ResetCondition, WaitFrame, WaitFrameRand, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ResetCondition = ResetCondition
		self.WaitFrame = WaitFrame
		self.WaitFrameRand = WaitFrameRand
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class ForkToggleFreeMoving:

	def __init__(self, Name, EnterChoice, LeaveChoice, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnterChoice = EnterChoice
		self.LeaveChoice = LeaveChoice


class ForkTogglePriestBossFreeMoving:

	def __init__(self, Name, SetFreeMoving, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SetFreeMoving = SetFreeMoving


class ForkToggleWeaponXLinkSleep:

	def __init__(self, Name, Toggle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Toggle = Toggle


class ForkTurnASHold:

	def __init__(self, Name, IsUpdateTarget, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsFollowGround, IsRotEndFinish, IsFinishForceStopRot, IsChangeable, IsUpFollow, RotAccRatio, RotAccMaxSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUpdateTarget = IsUpdateTarget
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsFollowGround = IsFollowGround
		self.IsRotEndFinish = IsRotEndFinish
		self.IsFinishForceStopRot = IsFinishForceStopRot
		self.IsChangeable = IsChangeable
		self.IsUpFollow = IsUpFollow
		self.RotAccRatio = RotAccRatio
		self.RotAccMaxSpeedRatio = RotAccMaxSpeedRatio


class ForkVacuumShootToTarget:

	def __init__(self, Name, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, PartsKey, IsReuseBullet, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsKey = PartsKey
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkWaitCloseGanonShoutMsgClose:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ForkWaitGroundHit:

	def __init__(self, Name, InWaterDepth, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.IsChangeable = IsChangeable


class ForkWeaponAttack:

	def __init__(self, Name, WeaponIdx, IsNoRod, SeqBank, TargetBone, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.IsNoRod = IsNoRod
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkWeaponAttackWithAtkBody:

	def __init__(self, Name, AtkBodyName, WeaponIdx, IsNoRod, SeqBank, TargetBone, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkBodyName = AtkBodyName
		self.WeaponIdx = WeaponIdx
		self.IsNoRod = IsNoRod
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class ForkWeaponShockWave:

	def __init__(self, Name, WeaponIdx, ShockWaveRadius, UnderRayLength, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.ShockWaveRadius = ShockWaveRadius
		self.UnderRayLength = UnderRayLength
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class ForkWeaponShockWaveCheckValue:

	def __init__(self, Name, AtEventValue, WeaponIdx, ShockWaveRadius, UnderRayLength, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtEventValue = AtEventValue
		self.WeaponIdx = WeaponIdx
		self.ShockWaveRadius = ShockWaveRadius
		self.UnderRayLength = UnderRayLength
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class FreeMoveByGuideBase:

	def __init__(self, Name, RotateAngleMax, KeepPlacementRotation, KeepRotationBaseBoneName, ASKeyName, MaxAngleAcc, AngleAccRatio, IsTraceRailPointRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotateAngleMax = RotateAngleMax
		self.KeepPlacementRotation = KeepPlacementRotation
		self.KeepRotationBaseBoneName = KeepRotationBaseBoneName
		self.ASKeyName = ASKeyName
		self.MaxAngleAcc = MaxAngleAcc
		self.AngleAccRatio = AngleAccRatio
		self.IsTraceRailPointRotation = IsTraceRailPointRotation


class FreeMoveRandom:

	def __init__(self, Name, RandVertical, RandHorizontal, RandSpeedMax, RandSpeedMin, TargetDistance, HeightMax, HeightMin, MoveAreaRadius, ASKeyName, Speed, SpeedAddRate, AngleSpeed, IsChangeable, IsIgnoreSameAS, AllowPitchRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RandVertical = RandVertical
		self.RandHorizontal = RandHorizontal
		self.RandSpeedMax = RandSpeedMax
		self.RandSpeedMin = RandSpeedMin
		self.TargetDistance = TargetDistance
		self.HeightMax = HeightMax
		self.HeightMin = HeightMin
		self.MoveAreaRadius = MoveAreaRadius
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.SpeedAddRate = SpeedAddRate
		self.AngleSpeed = AngleSpeed
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.AllowPitchRotation = AllowPitchRotation


class FreeMoveToNearGround:

	def __init__(self, Name, ReduceSpeedRateWithWind, WindVelocityLimit4Reduce, FinishRadius, TargetUpdateInterval, ASKeyName, Speed, SpeedAddRate, AngleSpeed, IsChangeable, IsIgnoreSameAS, AllowPitchRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReduceSpeedRateWithWind = ReduceSpeedRateWithWind
		self.WindVelocityLimit4Reduce = WindVelocityLimit4Reduce
		self.FinishRadius = FinishRadius
		self.TargetUpdateInterval = TargetUpdateInterval
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.SpeedAddRate = SpeedAddRate
		self.AngleSpeed = AngleSpeed
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.AllowPitchRotation = AllowPitchRotation


class FreeMoveToTarget:

	def __init__(self, Name, FinishRadius, TargetUpdateInterval, ASKeyName, Speed, SpeedAddRate, AngleSpeed, IsChangeable, IsIgnoreSameAS, AllowPitchRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinishRadius = FinishRadius
		self.TargetUpdateInterval = TargetUpdateInterval
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.SpeedAddRate = SpeedAddRate
		self.AngleSpeed = AngleSpeed
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.AllowPitchRotation = AllowPitchRotation


class FreeMoveToTargetInWataer:

	def __init__(self, Name, AllowMoveWaterDepth, IsForceTurnAgainstStream, ForceTurnLimitSpeedStream, ForceUseFrontDir, FinishRadius, TargetUpdateInterval, ASKeyName, Speed, SpeedAddRate, AngleSpeed, IsChangeable, IsIgnoreSameAS, AllowPitchRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AllowMoveWaterDepth = AllowMoveWaterDepth
		self.IsForceTurnAgainstStream = IsForceTurnAgainstStream
		self.ForceTurnLimitSpeedStream = ForceTurnLimitSpeedStream
		self.ForceUseFrontDir = ForceUseFrontDir
		self.FinishRadius = FinishRadius
		self.TargetUpdateInterval = TargetUpdateInterval
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.SpeedAddRate = SpeedAddRate
		self.AngleSpeed = AngleSpeed
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.AllowPitchRotation = AllowPitchRotation


class FreeMoveToTargetWithBank:

	def __init__(self, Name, BankAngleMax, LimitMoveAngle4Bank, FinishRadius, TargetUpdateInterval, ASKeyName, Speed, SpeedAddRate, AngleSpeed, IsChangeable, IsIgnoreSameAS, AllowPitchRotation, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BankAngleMax = BankAngleMax
		self.LimitMoveAngle4Bank = LimitMoveAngle4Bank
		self.FinishRadius = FinishRadius
		self.TargetUpdateInterval = TargetUpdateInterval
		self.ASKeyName = ASKeyName
		self.Speed = Speed
		self.SpeedAddRate = SpeedAddRate
		self.AngleSpeed = AngleSpeed
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.AllowPitchRotation = AllowPitchRotation


class Freeze:

	def __init__(self, Name, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class FreezedInIce:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FreezedInIceWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FromCDungeonToMainField:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class FrontierSpotBgmTriggerAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataAddFloat:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataAddInt:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataAddVec3:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataConvertIntToSring:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataCopyFloat:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataCopyInt:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataSubFloat:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataSubInt:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GameDataSubVec3:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GanonAttackWithEmitChemical:

	def __init__(self, Name, EmitActorName, EmitNum, EmitOffsetFromParent, EmitIntervalDist, EmitIntervalRotate, EmitScale, EmitMaxScale, ScaleTime, EmitInterval, EmitStartFrame, EmitAngleFromParent, EmitActorSpeed, EmitActorSpeedRotate, EmitAttackPower, EmitMinDamage, EmitBaseBoneName, EmitBoneRotateOffset, EmitPartsName, ChildCreateLimit, CallSEKeyAtAtOn, ASName, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, WeaponIdx, AttackPower, AtkMinPower, AtAttr, IsGuardPierce, IsGuardBreak, AttackCancelDist, AttackCancelAng, BattleNodeOffsetLR, BattleNodeOffsetUD, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EmitActorName = EmitActorName
		self.EmitNum = EmitNum
		self.EmitOffsetFromParent = EmitOffsetFromParent
		self.EmitIntervalDist = EmitIntervalDist
		self.EmitIntervalRotate = EmitIntervalRotate
		self.EmitScale = EmitScale
		self.EmitMaxScale = EmitMaxScale
		self.ScaleTime = ScaleTime
		self.EmitInterval = EmitInterval
		self.EmitStartFrame = EmitStartFrame
		self.EmitAngleFromParent = EmitAngleFromParent
		self.EmitActorSpeed = EmitActorSpeed
		self.EmitActorSpeedRotate = EmitActorSpeedRotate
		self.EmitAttackPower = EmitAttackPower
		self.EmitMinDamage = EmitMinDamage
		self.EmitBaseBoneName = EmitBaseBoneName
		self.EmitBoneRotateOffset = EmitBoneRotateOffset
		self.EmitPartsName = EmitPartsName
		self.ChildCreateLimit = ChildCreateLimit
		self.CallSEKeyAtAtOn = CallSEKeyAtAtOn
		self.ASName = ASName
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.WeaponIdx = WeaponIdx
		self.AttackPower = AttackPower
		self.AtkMinPower = AtkMinPower
		self.AtAttr = AtAttr
		self.IsGuardPierce = IsGuardPierce
		self.IsGuardBreak = IsGuardBreak
		self.AttackCancelDist = AttackCancelDist
		self.AttackCancelAng = AttackCancelAng
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD


class GanonBarrierOn:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class GanonBeamIgnite:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, OffsetHeight, BaseNode, IsConnectChild, DirMinAngle, DirMaxAngle, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.IsConnectChild = IsConnectChild
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GanonBeamMove:

	def __init__(self, Name, ForceExplodeFrame, AtMinDamage, ShieldDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceExplodeFrame = ForceExplodeFrame
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage


class GanonBeastASPlayFromActiveWp:

	def __init__(self, Name, ASName, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, FirstRandomRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.FirstRandomRatio = FirstRandomRatio


class GanonBeastBeamMove:

	def __init__(self, Name, RestActor, RestDistLimit, RestDistMinLimit, RestDistInterval, RestDistTime, RestDistTimeAdd, RestNumMax, IsGuarantee, Type, IsGuardPierces, IsSetAtIgnoreObstacle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RestActor = RestActor
		self.RestDistLimit = RestDistLimit
		self.RestDistMinLimit = RestDistMinLimit
		self.RestDistInterval = RestDistInterval
		self.RestDistTime = RestDistTime
		self.RestDistTimeAdd = RestDistTimeAdd
		self.RestNumMax = RestNumMax
		self.IsGuarantee = IsGuarantee
		self.Type = Type
		self.IsGuardPierces = IsGuardPierces
		self.IsSetAtIgnoreObstacle = IsSetAtIgnoreObstacle


class GanonBeastDamageASPlay:

	def __init__(self, Name, IsStateChange, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, FirstRandomRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsStateChange = IsStateChange
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.FirstRandomRatio = FirstRandomRatio


class GanonBoneControl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GanonChangeState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GanonChemicalPillarAttack:

	def __init__(self, Name, CreateActorName, ASName, AttackPower, AtMinPower, PillarOffset, AttackPowerForPlayer, PillarNum, PillarInterval, AppearPosDist, AppearPosHeight, IgnitionInterval, PileScale, WaitASName, CreatePileASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateActorName = CreateActorName
		self.ASName = ASName
		self.AttackPower = AttackPower
		self.AtMinPower = AtMinPower
		self.PillarOffset = PillarOffset
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.PillarNum = PillarNum
		self.PillarInterval = PillarInterval
		self.AppearPosDist = AppearPosDist
		self.AppearPosHeight = AppearPosHeight
		self.IgnitionInterval = IgnitionInterval
		self.PileScale = PileScale
		self.WaitASName = WaitASName
		self.CreatePileASName = CreatePileASName


class GanonFallAttack:

	def __init__(self, Name, IsEmitShockWave, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEmitShockWave = IsEmitShockWave


class GanonMove:

	def __init__(self, Name, MoveSpeed, MoveAccel, ASName, IsUpEqualGravity, AvoidMoveSpeed, AvoidMoveAccel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveSpeed = MoveSpeed
		self.MoveAccel = MoveAccel
		self.ASName = ASName
		self.IsUpEqualGravity = IsUpEqualGravity
		self.AvoidMoveSpeed = AvoidMoveSpeed
		self.AvoidMoveAccel = AvoidMoveAccel


class GanonSmallDamage:

	def __init__(self, Name, UpAS, AS, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpAS = UpAS
		self.AS = AS
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class GanonStunRecover:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GanonThrowFireBall:

	def __init__(self, Name, InitVelocity, FireBallScale, BallAppearOffset, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitVelocity = InitVelocity
		self.FireBallScale = FireBallScale
		self.BallAppearOffset = BallAppearOffset
		self.ASName = ASName


class GanonThrowMultiIce:

	def __init__(self, Name, ThrowNumAtSameTiming, InitVelocity, FireBallScale, BallAppearOffset, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowNumAtSameTiming = ThrowNumAtSameTiming
		self.InitVelocity = InitVelocity
		self.FireBallScale = FireBallScale
		self.BallAppearOffset = BallAppearOffset
		self.ASName = ASName


class GanonThrowMultiTornado:

	def __init__(self, Name, AppearOffset1, InitVelocity, AppearOffset, ASName, CreateHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AppearOffset1 = AppearOffset1
		self.InitVelocity = InitVelocity
		self.AppearOffset = AppearOffset
		self.ASName = ASName
		self.CreateHeight = CreateHeight


class GanonThrowTornado:

	def __init__(self, Name, InitVelocity, AppearOffset, ASName, CreateHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitVelocity = InitVelocity
		self.AppearOffset = AppearOffset
		self.ASName = ASName
		self.CreateHeight = CreateHeight


class GanonTurnOnWall:

	def __init__(self, Name, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable


class GanonWeaponNearAttack:

	def __init__(self, Name, ASName, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, WeaponIdx, AttackPower, AtkMinPower, AtAttr, IsGuardPierce, IsGuardBreak, AttackCancelDist, AttackCancelAng, BattleNodeOffsetLR, BattleNodeOffsetUD, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.WeaponIdx = WeaponIdx
		self.AttackPower = AttackPower
		self.AtkMinPower = AtkMinPower
		self.AtAttr = AtAttr
		self.IsGuardPierce = IsGuardPierce
		self.IsGuardBreak = IsGuardBreak
		self.AttackCancelDist = AttackCancelDist
		self.AttackCancelAng = AttackCancelAng
		self.BattleNodeOffsetLR = BattleNodeOffsetLR
		self.BattleNodeOffsetUD = BattleNodeOffsetUD


class GearRotate:

	def __init__(self, Name, IsReverse, IsTwoWayGear, StopCheckSpdRate, CheckSpdIdlingRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReverse = IsReverse
		self.IsTwoWayGear = IsTwoWayGear
		self.StopCheckSpdRate = StopCheckSpdRate
		self.CheckSpdIdlingRate = CheckSpdIdlingRate


class GearStop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GelEnemyAppear:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GelEnemyFreeze:

	def __init__(self, Name, ASName, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GelEnemySystemHideChase:

	def __init__(self, Name, IsOnAttention, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOnAttention = IsOnAttention
		self.ASName = ASName


class GelJumpTackle:

	def __init__(self, Name, IsEnableCloth, SubAS, SubASSlot, LeaveSubAS, BodyRotSpeed, MaxSpeed, MinSpeed, JumpHeight, JumpHeightMaxOffset, IsFinishedAtPreLandFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsEnableCloth = IsEnableCloth
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.LeaveSubAS = LeaveSubAS
		self.BodyRotSpeed = BodyRotSpeed
		self.MaxSpeed = MaxSpeed
		self.MinSpeed = MinSpeed
		self.JumpHeight = JumpHeight
		self.JumpHeightMaxOffset = JumpHeightMaxOffset
		self.IsFinishedAtPreLandFrame = IsFinishedAtPreLandFrame


class GerudoQueenWakeBoardReady:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetCapturedActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetItemAnotherActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetItemGet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetItemIntoBag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetOffFromHorseAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetRupee:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetSmallKeyItemGet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GetUp:

	def __init__(self, Name, RotRatio, ASName, RootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.RootOffset = RootOffset


class GetUpLinear:

	def __init__(self, Name, RotCenterPos, ASName, RootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotCenterPos = RotCenterPos
		self.ASName = ASName
		self.RootOffset = RootOffset


class GetUpMoveAnmDriven:

	def __init__(self, Name, TargetBoneName, RotRatio, ASName, RootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetBoneName = TargetBoneName
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.RootOffset = RootOffset


class GetWeaponEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GiantArmorBurned:

	def __init__(self, Name, StartAS, LoopAS, EndAS, UseRestart, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartAS = StartAS
		self.LoopAS = LoopAS
		self.EndAS = EndAS
		self.UseRestart = UseRestart
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiantArmorElectric:

	def __init__(self, Name, TimeMin, StartAS, LoopAS, EndAS, UseRestart, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TimeMin = TimeMin
		self.StartAS = StartAS
		self.LoopAS = LoopAS
		self.EndAS = EndAS
		self.UseRestart = UseRestart
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiantArmorEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GiantBattleCloseMove:

	def __init__(self, Name, VibrationPower, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VibrationPower = VibrationPower
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class GiantBattleCloseWalk:

	def __init__(self, Name, VibrationPower, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VibrationPower = VibrationPower
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class GiantCatchTreeWeapon:

	def __init__(self, Name, CatchPosOffset, WeaponIdx, RotSpd, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CatchPosOffset = CatchPosOffset
		self.WeaponIdx = WeaponIdx
		self.RotSpd = RotSpd
		self.ASName = ASName


class GiantDoubleGroundPunch:

	def __init__(self, Name, CoBodyName0, CoBodyName1, CoBodyName2, CoBodyName3, ASName, ASName2, PunchAimPosL0, PunchAimPosR0, PunchAimPosL1, PunchAimPosR1, PunchAimPosL2, PunchAimPosR2, RotOffset0, RotOffset1, RotOffset2, RotSpeedMax, IsImpulseLarge, AttackType, ExcludeAtkName0, ExcludeAtkName1, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CoBodyName0 = CoBodyName0
		self.CoBodyName1 = CoBodyName1
		self.CoBodyName2 = CoBodyName2
		self.CoBodyName3 = CoBodyName3
		self.ASName = ASName
		self.ASName2 = ASName2
		self.PunchAimPosL0 = PunchAimPosL0
		self.PunchAimPosR0 = PunchAimPosR0
		self.PunchAimPosL1 = PunchAimPosL1
		self.PunchAimPosR1 = PunchAimPosR1
		self.PunchAimPosL2 = PunchAimPosL2
		self.PunchAimPosR2 = PunchAimPosR2
		self.RotOffset0 = RotOffset0
		self.RotOffset1 = RotOffset1
		self.RotOffset2 = RotOffset2
		self.RotSpeedMax = RotSpeedMax
		self.IsImpulseLarge = IsImpulseLarge
		self.AttackType = AttackType
		self.ExcludeAtkName0 = ExcludeAtkName0
		self.ExcludeAtkName1 = ExcludeAtkName1
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class GiantDownSwingAttack:

	def __init__(self, Name, WeaponIdx, ASName, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, RotBaseBoneName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.ASName = ASName
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.RotBaseBoneName = RotBaseBoneName


class GiantEnemyWalk:

	def __init__(self, Name, VibrationPower, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VibrationPower = VibrationPower
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class GiantHandClapToTarget:

	def __init__(self, Name, AtkBodyScale, ASName, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsImpulseLarge, IsHeavy, IsHammer, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkBodyScale = AtkBodyScale
		self.ASName = ASName
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsImpulseLarge = IsImpulseLarge
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiantNavMeshWalk:

	def __init__(self, Name, VibrationPower, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VibrationPower = VibrationPower
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class GiantOneHandAttackWithLegTurn:

	def __init__(self, Name, WeaponIdx, ShoulderBoneName, RotOffsetMin, RotOffsetMax, BaseTargetPos, TraceLRAngleMax, TraceLRAngleMin, TraceDistFar, TraceDistNear, ASName, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, RotBaseBoneName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.ShoulderBoneName = ShoulderBoneName
		self.RotOffsetMin = RotOffsetMin
		self.RotOffsetMax = RotOffsetMax
		self.BaseTargetPos = BaseTargetPos
		self.TraceLRAngleMax = TraceLRAngleMax
		self.TraceLRAngleMin = TraceLRAngleMin
		self.TraceDistFar = TraceDistFar
		self.TraceDistNear = TraceDistNear
		self.ASName = ASName
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.RotBaseBoneName = RotBaseBoneName


class GiantOneHandPunchWithLegTurn:

	def __init__(self, Name, AtkBodyName0, AtkBodyName1, CoBodyName, ShoulderBoneName, RotOffsetMin, RotOffsetMax, BaseTargetPos, TraceLRAngleMax, TraceLRAngleMin, TraceDistFar, TraceDistNear, ASName, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, RotBaseBoneName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkBodyName0 = AtkBodyName0
		self.AtkBodyName1 = AtkBodyName1
		self.CoBodyName = CoBodyName
		self.ShoulderBoneName = ShoulderBoneName
		self.RotOffsetMin = RotOffsetMin
		self.RotOffsetMax = RotOffsetMax
		self.BaseTargetPos = BaseTargetPos
		self.TraceLRAngleMax = TraceLRAngleMax
		self.TraceLRAngleMin = TraceLRAngleMin
		self.TraceDistFar = TraceDistFar
		self.TraceDistNear = TraceDistNear
		self.ASName = ASName
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.RotBaseBoneName = RotBaseBoneName


class GiantPunchAttack:

	def __init__(self, Name, CoBodyName, ASName, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsImpulseLarge, IsHeavy, IsHammer, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CoBodyName = CoBodyName
		self.ASName = ASName
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsImpulseLarge = IsImpulseLarge
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiantPunchWithAddEntitySensor:

	def __init__(self, Name, CoBodyName, ASName, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsImpulseLarge, IsHeavy, IsHammer, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CoBodyName = CoBodyName
		self.ASName = ASName
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsImpulseLarge = IsImpulseLarge
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiantSleep:

	def __init__(self, Name, RidableRigidBodyName, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RidableRigidBodyName = RidableRigidBodyName
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GiveCookResultForNpc:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GolemDieFromRagdoll:

	def __init__(self, Name, RagdollBodyName1, MaterialName1, RagdollBodyName2, MaterialName2, RagdollBodyName3, MaterialName3, RagdollBodyName4, MaterialName4, Time, PosBaseRagdollRbName, RagdollControllerKey, RagdollMoveLimitDist, BlownHeight, BlownSpeed, PosReduceRatio, RotReduceRatio, XLinkKey, ImpulseXLinkKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RagdollBodyName1 = RagdollBodyName1
		self.MaterialName1 = MaterialName1
		self.RagdollBodyName2 = RagdollBodyName2
		self.MaterialName2 = MaterialName2
		self.RagdollBodyName3 = RagdollBodyName3
		self.MaterialName3 = MaterialName3
		self.RagdollBodyName4 = RagdollBodyName4
		self.MaterialName4 = MaterialName4
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.RagdollControllerKey = RagdollControllerKey
		self.RagdollMoveLimitDist = RagdollMoveLimitDist
		self.BlownHeight = BlownHeight
		self.BlownSpeed = BlownSpeed
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.XLinkKey = XLinkKey
		self.ImpulseXLinkKey = ImpulseXLinkKey


class GolemRepairParts:

	def __init__(self, Name, ASName, PartsKey1, RigidBodyName1, EntitySensorName1, ModelMatrialName1, PartsKey2, RigidBodyName2, EntitySensorName2, ModelMatrialName2, TgtBodyName, ChmObjectName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PartsKey1 = PartsKey1
		self.RigidBodyName1 = RigidBodyName1
		self.EntitySensorName1 = EntitySensorName1
		self.ModelMatrialName1 = ModelMatrialName1
		self.PartsKey2 = PartsKey2
		self.RigidBodyName2 = RigidBodyName2
		self.EntitySensorName2 = EntitySensorName2
		self.ModelMatrialName2 = ModelMatrialName2
		self.TgtBodyName = TgtBodyName
		self.ChmObjectName = ChmObjectName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GolemThrowPartsToTarget:

	def __init__(self, Name, ShootPitchMin, ShootPitchMax, ASName, PartsKey1, RigidBodyName1, EntitySensorName1, ModelMatrialName1, PartsKey2, RigidBodyName2, EntitySensorName2, ModelMatrialName2, TgtBodyName, ChmObjectName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootPitchMin = ShootPitchMin
		self.ShootPitchMax = ShootPitchMax
		self.ASName = ASName
		self.PartsKey1 = PartsKey1
		self.RigidBodyName1 = RigidBodyName1
		self.EntitySensorName1 = EntitySensorName1
		self.ModelMatrialName1 = ModelMatrialName1
		self.PartsKey2 = PartsKey2
		self.RigidBodyName2 = RigidBodyName2
		self.EntitySensorName2 = EntitySensorName2
		self.ModelMatrialName2 = ModelMatrialName2
		self.TgtBodyName = TgtBodyName
		self.ChmObjectName = ChmObjectName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GoronHeroDescendentAppear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GoronHeroDescendentJump:

	def __init__(self, Name, MaxHeight, TimeScale, IsDebugDrawTargetPos, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxHeight = MaxHeight
		self.TimeScale = TimeScale
		self.IsDebugDrawTargetPos = IsDebugDrawTargetPos


class Grab:

	def __init__(self, Name, AttOffset, CheckRadius, GrabIdx, CheckSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttOffset = AttOffset
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.CheckSpeed = CheckSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GrabAndShoot:

	def __init__(self, Name, RotSpd, ShootSpeed, ShootAng, BlurMax, GrabIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.ShootSpeed = ShootSpeed
		self.ShootAng = ShootAng
		self.BlurMax = BlurMax
		self.GrabIdx = GrabIdx


class GrabAttack:

	def __init__(self, Name, ASName, AtRigidBodyName, AttOffset, CheckRadius, GrabIdx, CheckSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AtRigidBodyName = AtRigidBodyName
		self.AttOffset = AttOffset
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.CheckSpeed = CheckSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GrabLeft:

	def __init__(self, Name, AttOffset, CheckRadius, GrabIdx, CheckSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttOffset = AttOffset
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.CheckSpeed = CheckSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GrabLeftTurn:

	def __init__(self, Name, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class GrabLeftWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class GrabRight:

	def __init__(self, Name, AttOffset, CheckRadius, GrabIdx, CheckSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttOffset = AttOffset
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.CheckSpeed = CheckSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GrabRightTurn:

	def __init__(self, Name, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class GrabRightWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class GraveAttack:

	def __init__(self, Name, Time, KeepTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.KeepTime = KeepTime


class GroupAllowEmitAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GroupDisallowEmitAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Guard:

	def __init__(self, Name, RotSubsAngRate, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSubsAngRate = RotSubsAngRate
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class GuardBackWalk:

	def __init__(self, Name, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class GuardBreak:

	def __init__(self, Name, HitImpactForce, VelReduce, KnockBackTime, DropIdx, WeaponVel, WeaponVelY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HitImpactForce = HitImpactForce
		self.VelReduce = VelReduce
		self.KnockBackTime = KnockBackTime
		self.DropIdx = DropIdx
		self.WeaponVel = WeaponVel
		self.WeaponVelY = WeaponVelY


class GuardJust:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GuardLoop:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GuardTurn:

	def __init__(self, Name, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class GuardWithAS:

	def __init__(self, Name, ASName, ASSlot, RotSubsAngRate, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlot = ASSlot
		self.RotSubsAngRate = RotSubsAngRate
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class GuardianAimBeam:

	def __init__(self, Name, TargetOffset, TargetOffsetY, FluctuationRange, FluctuationTime, FluctuationSpan, NodeName, NodeOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetOffset = TargetOffset
		self.TargetOffsetY = TargetOffsetY
		self.FluctuationRange = FluctuationRange
		self.FluctuationTime = FluctuationTime
		self.FluctuationSpan = FluctuationSpan
		self.NodeName = NodeName
		self.NodeOffset = NodeOffset


class GuardianAimBeamWithAS:

	def __init__(self, Name, ASName, IsChangeable, TargetOffset, TargetOffsetY, FluctuationRange, FluctuationTime, FluctuationSpan, NodeName, NodeOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsChangeable = IsChangeable
		self.TargetOffset = TargetOffset
		self.TargetOffsetY = TargetOffsetY
		self.FluctuationRange = FluctuationRange
		self.FluctuationTime = FluctuationTime
		self.FluctuationSpan = FluctuationSpan
		self.NodeName = NodeName
		self.NodeOffset = NodeOffset


class GuardianBeamFire:

	def __init__(self, Name, Speed, ForceExplodeFrame, AtMinDamage, ShieldDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.ForceExplodeFrame = ForceExplodeFrame
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage


class GuardianChargeBeam:

	def __init__(self, Name, Time, TimeRand, ChargeRadius, Color, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.ChargeRadius = ChargeRadius
		self.Color = Color


class GuardianMiniBeamMove:

	def __init__(self, Name, ReboundDeccel, ForceExplodeFrame, AtMinDamage, ShieldDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReboundDeccel = ReboundDeccel
		self.ForceExplodeFrame = ForceExplodeFrame
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage


class GuardianMiniFinalBeamMove:

	def __init__(self, Name, Speed, ForceExplodeFrame, AtMinDamage, ShieldDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.ForceExplodeFrame = ForceExplodeFrame
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage


class GuardianMiniGuardBattleWalk:

	def __init__(self, Name, ASName, ASSlot, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlot = ASSlot
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio


class GuardianMiniGuardBreak:

	def __init__(self, Name, GuardBreakASName, OtherASName, ASSlot, HitImpactForce, VelReduce, KnockBackTime, DropIdx, WeaponVel, WeaponVelY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GuardBreakASName = GuardBreakASName
		self.OtherASName = OtherASName
		self.ASSlot = ASSlot
		self.HitImpactForce = HitImpactForce
		self.VelReduce = VelReduce
		self.KnockBackTime = KnockBackTime
		self.DropIdx = DropIdx
		self.WeaponVel = WeaponVel
		self.WeaponVelY = WeaponVelY


class GuardianMiniGuardNavMeshWalk:

	def __init__(self, Name, ASName, ASSlot, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlot = ASSlot
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class GuardianMiniGuardSideWalk:

	def __init__(self, Name, ASName, ASSlot, Speed, RotSpd, RotDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlot = ASSlot
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist


class GuardianMiniGuardTurn:

	def __init__(self, Name, ASName, ASSlot, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlot = ASSlot
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class GuardianMiniGuardWait:

	def __init__(self, Name, GuardASName, ASName, ASSlotRight, ASSlotLeft, ASSlotBack, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GuardASName = GuardASName
		self.ASName = ASName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GuardianMiniLineBeam:

	def __init__(self, Name, IceBlockBreakTime, IsGuarantee, Type, IsGuardPierces, IsSetAtIgnoreObstacle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IceBlockBreakTime = IceBlockBreakTime
		self.IsGuarantee = IsGuarantee
		self.Type = Type
		self.IsGuardPierces = IsGuardPierces
		self.IsSetAtIgnoreObstacle = IsSetAtIgnoreObstacle


class GuardianMiniNeckSpinBeam:

	def __init__(self, Name, SpinNum, MaxLengthTime, IsStraight, BeamRange, MuzzleOffset, BeamDirection, BeamBoneName, BeamActorKey, BeamActorName, SpinSpeed, NeckUDAngle, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpinNum = SpinNum
		self.MaxLengthTime = MaxLengthTime
		self.IsStraight = IsStraight
		self.BeamRange = BeamRange
		self.MuzzleOffset = MuzzleOffset
		self.BeamDirection = BeamDirection
		self.BeamBoneName = BeamBoneName
		self.BeamActorKey = BeamActorKey
		self.BeamActorName = BeamActorName
		self.SpinSpeed = SpinSpeed
		self.NeckUDAngle = NeckUDAngle
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GuardianMiniPracticeFlagSet:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class GuardianMiniWait:

	def __init__(self, Name, ASName, ASSlotRight, ASSlotLeft, ASSlotBack, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.ASSlotRight = ASSlotRight
		self.ASSlotLeft = ASSlotLeft
		self.ASSlotBack = ASSlotBack
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class GuardianMoveToPosition:

	def __init__(self, Name, Decelerate, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Decelerate = Decelerate
		self.Speed = Speed


class GuardianMoveToTarget:

	def __init__(self, Name, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed


class GuardianSearch:

	def __init__(self, Name, Lost, WaitFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Lost = Lost
		self.WaitFrame = WaitFrame


class GuardianStopWait:

	def __init__(self, Name, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed


class HiddenKorokAppear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HideBarrelCarried:

	def __init__(self, Name, CutLength, IsCreateItem, IsRecoverCharCtrlAxis, IsUseConstraint, FailDistance, IsOnBaseLink, BindType, IsChangeable, HoldOnXLinkKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CutLength = CutLength
		self.IsCreateItem = IsCreateItem
		self.IsRecoverCharCtrlAxis = IsRecoverCharCtrlAxis
		self.IsUseConstraint = IsUseConstraint
		self.FailDistance = FailDistance
		self.IsOnBaseLink = IsOnBaseLink
		self.BindType = BindType
		self.IsChangeable = IsChangeable
		self.HoldOnXLinkKey = HoldOnXLinkKey


class HideHover:

	def __init__(self, Name, EffectName, Timer, IsKeepLifeGage, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EffectName = EffectName
		self.Timer = Timer
		self.IsKeepLifeGage = IsKeepLifeGage
		self.IsChangeable = IsChangeable


class HideShootArrow:

	def __init__(self, Name, ShootStartASName, ShootASName, ShootEndASName, LoopTime, StopSpeedRatio, StopRotSpeedRatio, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootStartASName = ShootStartASName
		self.ShootASName = ShootASName
		self.ShootEndASName = ShootEndASName
		self.LoopTime = LoopTime
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.ASName = ASName


class HingeMagneFixedRigid:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HoldArrow:

	def __init__(self, Name, WeaponIdx, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class HoldArrowBackWalk:

	def __init__(self, Name, HoldWeaponIdx, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HoldWeaponIdx = HoldWeaponIdx
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class HoldArrowTurn:

	def __init__(self, Name, WeaponIdx, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class HoldArrowWalk:

	def __init__(self, Name, HoldWeaponIdx, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HoldWeaponIdx = HoldWeaponIdx
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class HopFlyByTriggers:

	def __init__(self, Name, ASName, XZSpeedMax, HopAccRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.XZSpeedMax = XZSpeedMax
		self.HopAccRatio = HopAccRatio


class HornUse:

	def __init__(self, Name, SpreadDist, SpreadTime, TerrorLevel, NoticeMaskState, WeaponIdx, SignalOnTime, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpreadDist = SpreadDist
		self.SpreadTime = SpreadTime
		self.TerrorLevel = TerrorLevel
		self.NoticeMaskState = NoticeMaskState
		self.WeaponIdx = WeaponIdx
		self.SignalOnTime = SignalOnTime
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class HorseDie:

	def __init__(self, Name, DyingFrames, ASName, CheckIfStable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DyingFrames = DyingFrames
		self.ASName = ASName
		self.CheckIfStable = CheckIfStable


class HorseEatAction:

	def __init__(self, Name, TargetDirToStickX, TargetDistOffset, TargetDistToStickY, MaxStickXForEat, MaxStickYForEat, DelayFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetDirToStickX = TargetDirToStickX
		self.TargetDistOffset = TargetDistOffset
		self.TargetDistToStickY = TargetDistToStickY
		self.MaxStickXForEat = MaxStickXForEat
		self.MaxStickYForEat = MaxStickYForEat
		self.DelayFrames = DelayFrames


class HorseEatCarriedItem:

	def __init__(self, Name, CarriedItemPosRTYOffset, CarriedItemPosRTYWidth, ThresholdForEat, DelayFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CarriedItemPosRTYOffset = CarriedItemPosRTYOffset
		self.CarriedItemPosRTYWidth = CarriedItemPosRTYWidth
		self.ThresholdForEat = ThresholdForEat
		self.DelayFrames = DelayFrames


class HorseElectricParalysis:

	def __init__(self, Name, PauseDelayFrames, ASName, ThrowOffAttackRigidBodyName, CanRiddenWhenLeave, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PauseDelayFrames = PauseDelayFrames
		self.ASName = ASName
		self.ThrowOffAttackRigidBodyName = ThrowOffAttackRigidBodyName
		self.CanRiddenWhenLeave = CanRiddenWhenLeave
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class HorseFallAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseFollow:

	def __init__(self, Name, UseGearType, WaitDistanceToLeader, Gear1DistanceToLeader, Gear2DistanceToLeader, Gear3DistanceToLeader, DistanceFactorAtGearDown, WaitDistanceIncreaseDistance, WaitDistanceIncreasePerFrame, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnDistance, IsEndAtAutoStop, UseMinRadius, DesiredDirAngleDeltaSecMax, IsAvoidNavMeshActor, IsTargetPosEqualToLeaderPos, NavMeshCharacterRadiusScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseGearType = UseGearType
		self.WaitDistanceToLeader = WaitDistanceToLeader
		self.Gear1DistanceToLeader = Gear1DistanceToLeader
		self.Gear2DistanceToLeader = Gear2DistanceToLeader
		self.Gear3DistanceToLeader = Gear3DistanceToLeader
		self.DistanceFactorAtGearDown = DistanceFactorAtGearDown
		self.WaitDistanceIncreaseDistance = WaitDistanceIncreaseDistance
		self.WaitDistanceIncreasePerFrame = WaitDistanceIncreasePerFrame
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnDistance = AutoStopAndTurnDistance
		self.IsEndAtAutoStop = IsEndAtAutoStop
		self.UseMinRadius = UseMinRadius
		self.DesiredDirAngleDeltaSecMax = DesiredDirAngleDeltaSecMax
		self.IsAvoidNavMeshActor = IsAvoidNavMeshActor
		self.IsTargetPosEqualToLeaderPos = IsTargetPosEqualToLeaderPos
		self.NavMeshCharacterRadiusScale = NavMeshCharacterRadiusScale


class HorseFreeze:

	def __init__(self, Name, PauseDelayFrames, ASName, ThrowOffAttackRigidBodyName, CanRiddenWhenLeave, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PauseDelayFrames = PauseDelayFrames
		self.ASName = ASName
		self.ThrowOffAttackRigidBodyName = ThrowOffAttackRigidBodyName
		self.CanRiddenWhenLeave = CanRiddenWhenLeave
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class HorseKickBackAction:

	def __init__(self, Name, ASName, SucceedGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.SucceedGear = SucceedGear


class HorseManeCollarSyncAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseManeGrabbedAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseMoveToSafePos:

	def __init__(self, Name, SearchRadius, AreaThreshold, ResolvePenetrationRadiusScale, ResolvePenetrationSearchRadius, SetEndIfCurrentFaceIsSafe, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnMode, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, WaitUntilPathSucceeded, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchRadius = SearchRadius
		self.AreaThreshold = AreaThreshold
		self.ResolvePenetrationRadiusScale = ResolvePenetrationRadiusScale
		self.ResolvePenetrationSearchRadius = ResolvePenetrationSearchRadius
		self.SetEndIfCurrentFaceIsSafe = SetEndIfCurrentFaceIsSafe
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnMode = AutoStopAndTurnMode
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.WaitUntilPathSucceeded = WaitUntilPathSucceeded


class HorseMoveToTargetAction:

	def __init__(self, Name, IsCancelRequestedPathFirst, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnMode, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, WaitUntilPathSucceeded, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCancelRequestedPathFirst = IsCancelRequestedPathFirst
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnMode = AutoStopAndTurnMode
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.WaitUntilPathSucceeded = WaitUntilPathSucceeded


class HorseRandomMoveAction:

	def __init__(self, Name, RadiusLimit, ForwardDirDistCoefficient, DirRandomValue, DirRangeDegree, RejectDistRatioByNavMeshQuery, IsCancelRequestedPathFirst, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnMode, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, WaitUntilPathSucceeded, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RadiusLimit = RadiusLimit
		self.ForwardDirDistCoefficient = ForwardDirDistCoefficient
		self.DirRandomValue = DirRandomValue
		self.DirRangeDegree = DirRangeDegree
		self.RejectDistRatioByNavMeshQuery = RejectDistRatioByNavMeshQuery
		self.IsCancelRequestedPathFirst = IsCancelRequestedPathFirst
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnMode = AutoStopAndTurnMode
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.WaitUntilPathSucceeded = WaitUntilPathSucceeded


class HorseReinsBindAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseReinsDefaultAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseReturnToSafePos:

	def __init__(self, Name, ASName, StartFadeOutFrame, HiddenFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.StartFadeOutFrame = StartFadeOutFrame
		self.HiddenFrames = HiddenFrames


class HorseRiddenByPlayer:

	def __init__(self, Name, MaxAcceleration, SlideToCurveRatio, TiredFramesAfterGearTop, CheckFramesSootheAtFirstRun, CheckFramesSootheAfterRun, CheckFramesSootheAfterGearTop, CheckFramesSootheAfterJump, CheckFramesSootheAfterResist, CheckFramesAccInputAfterResist, MinFramesForRunSoothe, FamiliarityEffectDelayFrames, ChargeRecoveryFrames, ChargeRecoveryFramesSecondly, ChargePenaltyFrames, SwitchFramesByTemperature, ForwardBentFramesAtGearTop, FallHeightForPlayingAS, FallHeightForPlayingASInRunning, FallRayCastLength, FamiliarityThresholdOfRailTrace, FamiliarityThresholdOfResist, FamiliarityThresholdOfWaitAngry, ResistGearDownProbability, ResistChangeSteeringProbability, ResistChangeSteeringMinFrames, ResistChangeSteeringMaxFrames, ResistChangeSteeringInputRange, FramesPlayAngryWhileResist, DelayFramesResistGearDown, DelayFramesResistChangeSteering, StressDecBySoothe, StressIncByImpossibleAcc, StressIncByEnemy, StressIncByDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxAcceleration = MaxAcceleration
		self.SlideToCurveRatio = SlideToCurveRatio
		self.TiredFramesAfterGearTop = TiredFramesAfterGearTop
		self.CheckFramesSootheAtFirstRun = CheckFramesSootheAtFirstRun
		self.CheckFramesSootheAfterRun = CheckFramesSootheAfterRun
		self.CheckFramesSootheAfterGearTop = CheckFramesSootheAfterGearTop
		self.CheckFramesSootheAfterJump = CheckFramesSootheAfterJump
		self.CheckFramesSootheAfterResist = CheckFramesSootheAfterResist
		self.CheckFramesAccInputAfterResist = CheckFramesAccInputAfterResist
		self.MinFramesForRunSoothe = MinFramesForRunSoothe
		self.FamiliarityEffectDelayFrames = FamiliarityEffectDelayFrames
		self.ChargeRecoveryFrames = ChargeRecoveryFrames
		self.ChargeRecoveryFramesSecondly = ChargeRecoveryFramesSecondly
		self.ChargePenaltyFrames = ChargePenaltyFrames
		self.SwitchFramesByTemperature = SwitchFramesByTemperature
		self.ForwardBentFramesAtGearTop = ForwardBentFramesAtGearTop
		self.FallHeightForPlayingAS = FallHeightForPlayingAS
		self.FallHeightForPlayingASInRunning = FallHeightForPlayingASInRunning
		self.FallRayCastLength = FallRayCastLength
		self.FamiliarityThresholdOfRailTrace = FamiliarityThresholdOfRailTrace
		self.FamiliarityThresholdOfResist = FamiliarityThresholdOfResist
		self.FamiliarityThresholdOfWaitAngry = FamiliarityThresholdOfWaitAngry
		self.ResistGearDownProbability = ResistGearDownProbability
		self.ResistChangeSteeringProbability = ResistChangeSteeringProbability
		self.ResistChangeSteeringMinFrames = ResistChangeSteeringMinFrames
		self.ResistChangeSteeringMaxFrames = ResistChangeSteeringMaxFrames
		self.ResistChangeSteeringInputRange = ResistChangeSteeringInputRange
		self.FramesPlayAngryWhileResist = FramesPlayAngryWhileResist
		self.DelayFramesResistGearDown = DelayFramesResistGearDown
		self.DelayFramesResistChangeSteering = DelayFramesResistChangeSteering
		self.StressDecBySoothe = StressDecBySoothe
		self.StressIncByImpossibleAcc = StressIncByImpossibleAcc
		self.StressIncByEnemy = StressIncByEnemy
		self.StressIncByDamage = StressIncByDamage


class HorseRideAngryGear1Coomand:

	def __init__(self, Name, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideArrowReload:

	def __init__(self, Name, ASName, WeaponIdx, RotRatio, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx = WeaponIdx
		self.RotRatio = RotRatio
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideAttack:

	def __init__(self, Name, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideCancelCommand:

	def __init__(self, Name, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideChargeCommand:

	def __init__(self, Name, Gear, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Gear = Gear
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideChaseCommand:

	def __init__(self, Name, ChaseKeepDist, Gear, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChaseKeepDist = ChaseKeepDist
		self.Gear = Gear
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideDynSetGearCommand:

	def __init__(self, Name, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideLookWait:

	def __init__(self, Name, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideLoopAttack:

	def __init__(self, Name, FinishAS, LoopAttackTime, IsFinishByAtHit, ASName, WeaponIdx, IsNoRodAttack, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FinishAS = FinishAS
		self.LoopAttackTime = LoopAttackTime
		self.IsFinishByAtHit = IsFinishByAtHit
		self.ASName = ASName
		self.WeaponIdx = WeaponIdx
		self.IsNoRodAttack = IsNoRodAttack
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideMoveToCommand:

	def __init__(self, Name, Gear, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Gear = Gear
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideOneTimeASPlay:

	def __init__(self, Name, ASName, IgnoreSameAS, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IgnoreSameAS = IgnoreSameAS
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideOneTimeViewASPlay:

	def __init__(self, Name, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideSearch:

	def __init__(self, Name, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideShoot:

	def __init__(self, Name, ASName, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideStopCommand:

	def __init__(self, Name, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideTurnCommand:

	def __init__(self, Name, CommandTiming, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CommandTiming = CommandTiming
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideViewWait:

	def __init__(self, Name, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRideWait:

	def __init__(self, Name, Time, TimeRand, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class HorseRodeo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseSaddleBindAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseSaddleDefaultAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseSwimAction:

	def __init__(self, Name, LandSearchRadius, LandSearchNormalCos, LandSearchMinArea, LandSearchIntervalFrames, ResolvePenetrationRadiusScale, ResolvePenetrationSearchRadius, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LandSearchRadius = LandSearchRadius
		self.LandSearchNormalCos = LandSearchNormalCos
		self.LandSearchMinArea = LandSearchMinArea
		self.LandSearchIntervalFrames = LandSearchIntervalFrames
		self.ResolvePenetrationRadiusScale = ResolvePenetrationRadiusScale
		self.ResolvePenetrationSearchRadius = ResolvePenetrationSearchRadius


class HorseSwimToTargetActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseTurnAction:

	def __init__(self, Name, GoalDegToleranceAtEnter, GoalDegTolerance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GoalDegToleranceAtEnter = GoalDegToleranceAtEnter
		self.GoalDegTolerance = GoalDegTolerance


class HorseVanish:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseWaitAction:

	def __init__(self, Name, UseGearType, SmoothStopFrames, SmoothStopFramesGear3, MinFramesGear1, IsCourbetteEnabled, IsLight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseGearType = UseGearType
		self.SmoothStopFrames = SmoothStopFrames
		self.SmoothStopFramesGear3 = SmoothStopFramesGear3
		self.MinFramesGear1 = MinFramesGear1
		self.IsCourbetteEnabled = IsCourbetteEnabled
		self.IsLight = IsLight


class HorseWaitAndLookAtNPC:

	def __init__(self, Name, UseGearType, SmoothStopFrames, SmoothStopFramesGear3, MinFramesGear1, IsCourbetteEnabled, IsLight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UseGearType = UseGearType
		self.SmoothStopFrames = SmoothStopFrames
		self.SmoothStopFramesGear3 = SmoothStopFramesGear3
		self.MinFramesGear1 = MinFramesGear1
		self.IsCourbetteEnabled = IsCourbetteEnabled
		self.IsLight = IsLight


class HorseWaitEx:

	def __init__(self, Name, KeepFrame, UseGearType, SmoothStopFrames, SmoothStopFramesGear3, MinFramesGear1, IsCourbetteEnabled, IsLight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepFrame = KeepFrame
		self.UseGearType = UseGearType
		self.SmoothStopFrames = SmoothStopFrames
		self.SmoothStopFramesGear3 = SmoothStopFramesGear3
		self.MinFramesGear1 = MinFramesGear1
		self.IsCourbetteEnabled = IsCourbetteEnabled
		self.IsLight = IsLight


class HorseWaitForEventAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class HorseWaitThrowOffAction:

	def __init__(self, Name, SucceedGear, SetRideAttentionInvalid, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SucceedGear = SucceedGear
		self.SetRideAttentionInvalid = SetRideAttentionInvalid


class Hover:

	def __init__(self, Name, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class HoverNoticeTurn:

	def __init__(self, Name, NoDoubleNoticeTime, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoDoubleNoticeTime = NoDoubleNoticeTime
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class HoverPredictVacuumShoot:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, PartsKey, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, RotSpd, IsReuseBullet, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.PartsKey = PartsKey
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.RotSpd = RotSpd
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class HoverTurn:

	def __init__(self, Name, ASKeyName, IsIgnoreSameAS, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class HuntingDead:

	def __init__(self, Name, OffsetBoneName, IsUseOffsetY, ExtraOffset, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetBoneName = OffsetBoneName
		self.IsUseOffsetY = IsUseOffsetY
		self.ExtraOffset = ExtraOffset
		self.InWaterDepth = InWaterDepth


class IceBroken:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IchigekiHeartDecrease:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IchigekiHeartUiClose:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IchigekiHeartUiOpen:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IdleAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IgniteGrabAndShoot:

	def __init__(self, Name, RotSpd, ShootSpd, ShootAng, BlurMax, GrabIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.ShootSpd = ShootSpd
		self.ShootAng = ShootAng
		self.BlurMax = BlurMax
		self.GrabIdx = GrabIdx


class IgniteThreeActorAttack:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, BaseNode, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.BaseNode = BaseNode
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class IgniteToTarget:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class IgniteToTargetDir:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, OffsetHeight, BaseNode, IsConnectChild, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.IsConnectChild = IsConnectChild
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class IgniteToTargetSimple:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, OffsetHeight, BaseNode, IsConnectChild, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.IsConnectChild = IsConnectChild
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class IgnitedThrown:

	def __init__(self, Name, AS, IsScaling, IsFinishedByOneHit, IsFadeIn, IsAbleGuard, IsForceOnly, ReactionLevel, DamageScale, FinishWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS
		self.IsScaling = IsScaling
		self.IsFinishedByOneHit = IsFinishedByOneHit
		self.IsFadeIn = IsFadeIn
		self.IsAbleGuard = IsAbleGuard
		self.IsForceOnly = IsForceOnly
		self.ReactionLevel = ReactionLevel
		self.DamageScale = DamageScale
		self.FinishWaterDepth = FinishWaterDepth


class ImmediateStopOwnedHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class InCarryBox:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IncreaseNumDungeonClearSeal:

	def __init__(self, Name, ActorName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorName = ActorName


class IncreaseNumHeroSeal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IncreaseNumKorokNuts:

	def __init__(self, Name, ActorName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActorName = ActorName


class IncreasePlayerMaxHeart:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class IncreasePlayerMaxStamina:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class InitPouchForQuest:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class InsectLevelFlyMove:

	def __init__(self, Name, ReduceSpeedRateWithWind, WindVelocityLimit4Reduce, ASName, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, IsOverRise, CheckStopSpeed, IsSlowDownNearGoal, VibrateMemoryStep, VibrateCheckFrame, VibrateStopCheck, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReduceSpeedRateWithWind = ReduceSpeedRateWithWind
		self.WindVelocityLimit4Reduce = WindVelocityLimit4Reduce
		self.ASName = ASName
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.IsOverRise = IsOverRise
		self.CheckStopSpeed = CheckStopSpeed
		self.IsSlowDownNearGoal = IsSlowDownNearGoal
		self.VibrateMemoryStep = VibrateMemoryStep
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateStopCheck = VibrateStopCheck
		self.FlyHeightMin = FlyHeightMin


class InvisibleKorokMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class InvisibleKorokWait:

	def __init__(self, Name, SpeedDecreRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedDecreRate = SpeedDecreRate


class IsMorphEndASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ItemAmiiboCreateFromDropTable:

	def __init__(self, Name, CreateOffset, CreateArea, CreateInterval, ClearSealNum, BigHitRate1st, BigHitRate2nd, BigHitRate3rd, GreatHitRate1st, GreatHitRate2nd, GreatHitRate3rd, DropNumRate1st, DropNumRate2nd, DropNumRate3rd, HitRateAdjustStart, HitRateAdjustEnd, SmallHitRate1st, SmallHitRate2nd, SmallHitRate3rd, PairActor_0, PairActor_1, PairActor_2, FlagActor_0, FlagActor_1, FlagActor_2, NotFlagActor_0, NotFlagActor_1, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateOffset = CreateOffset
		self.CreateArea = CreateArea
		self.CreateInterval = CreateInterval
		self.ClearSealNum = ClearSealNum
		self.BigHitRate1st = BigHitRate1st
		self.BigHitRate2nd = BigHitRate2nd
		self.BigHitRate3rd = BigHitRate3rd
		self.GreatHitRate1st = GreatHitRate1st
		self.GreatHitRate2nd = GreatHitRate2nd
		self.GreatHitRate3rd = GreatHitRate3rd
		self.DropNumRate1st = DropNumRate1st
		self.DropNumRate2nd = DropNumRate2nd
		self.DropNumRate3rd = DropNumRate3rd
		self.HitRateAdjustStart = HitRateAdjustStart
		self.HitRateAdjustEnd = HitRateAdjustEnd
		self.SmallHitRate1st = SmallHitRate1st
		self.SmallHitRate2nd = SmallHitRate2nd
		self.SmallHitRate3rd = SmallHitRate3rd
		self.PairActor_0 = PairActor_0
		self.PairActor_1 = PairActor_1
		self.PairActor_2 = PairActor_2
		self.FlagActor_0 = FlagActor_0
		self.FlagActor_1 = FlagActor_1
		self.FlagActor_2 = FlagActor_2
		self.NotFlagActor_0 = NotFlagActor_0
		self.NotFlagActor_1 = NotFlagActor_1


class ItemAmiiboSelectDropTable:

	def __init__(self, Name, TableCommon, TableGanondorf, TableToonLink, TableSheik, TableLink, TableZelda, TableWolfLink, TableGuardian, TableBokoblin, TableCross_Ganondorf, TableCross_ToonLink, TableCross_Sheik, TableCross_Link, TableCross_Zelda, TableKing_WolfLink, TableKing_Link_Bow, TableKing_Link_Horse, TableKing_Zelda_Doctor, TableKing_Guardian, TableKing_Bokoblin, TableKing30th_Link_Ocarina, TableKing30th_Link_Majora, TableKing30th_Link_Takt, TableKing30th_Zelda_Takt, TableKing30th_Link_Twilight, TableKing30th_Link_Skyward, TableKing30th_Link_Dot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TableCommon = TableCommon
		self.TableGanondorf = TableGanondorf
		self.TableToonLink = TableToonLink
		self.TableSheik = TableSheik
		self.TableLink = TableLink
		self.TableZelda = TableZelda
		self.TableWolfLink = TableWolfLink
		self.TableGuardian = TableGuardian
		self.TableBokoblin = TableBokoblin
		self.TableCross_Ganondorf = TableCross_Ganondorf
		self.TableCross_ToonLink = TableCross_ToonLink
		self.TableCross_Sheik = TableCross_Sheik
		self.TableCross_Link = TableCross_Link
		self.TableCross_Zelda = TableCross_Zelda
		self.TableKing_WolfLink = TableKing_WolfLink
		self.TableKing_Link_Bow = TableKing_Link_Bow
		self.TableKing_Link_Horse = TableKing_Link_Horse
		self.TableKing_Zelda_Doctor = TableKing_Zelda_Doctor
		self.TableKing_Guardian = TableKing_Guardian
		self.TableKing_Bokoblin = TableKing_Bokoblin
		self.TableKing30th_Link_Ocarina = TableKing30th_Link_Ocarina
		self.TableKing30th_Link_Majora = TableKing30th_Link_Majora
		self.TableKing30th_Link_Takt = TableKing30th_Link_Takt
		self.TableKing30th_Zelda_Takt = TableKing30th_Zelda_Takt
		self.TableKing30th_Link_Twilight = TableKing30th_Link_Twilight
		self.TableKing30th_Link_Skyward = TableKing30th_Link_Skyward
		self.TableKing30th_Link_Dot = TableKing30th_Link_Dot


class ItemConductorDemoBind:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class JumpAttack:

	def __init__(self, Name, MaxSpeed, WeaponIdx, JumpHeight, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsForceGuardBreak, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.WeaponIdx = WeaponIdx
		self.JumpHeight = JumpHeight
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsForceGuardBreak = IsForceGuardBreak


class JumpMainRigidBody:

	def __init__(self, Name, Power, PostBoundReactionKeys, JumpDir, IsRotJumpDir, VibrateStopCheck, VibrateCheckFrame, VibrateMemoryStep, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Power = Power
		self.PostBoundReactionKeys = PostBoundReactionKeys
		self.JumpDir = JumpDir
		self.IsRotJumpDir = IsRotJumpDir
		self.VibrateStopCheck = VibrateStopCheck
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateMemoryStep = VibrateMemoryStep


class JumpMove:

	def __init__(self, Name, ASKey, PreJumpWait, MaxMoveSpeed, MinMoveSpeed, RandAngleLimit, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKey = ASKey
		self.PreJumpWait = PreJumpWait
		self.MaxMoveSpeed = MaxMoveSpeed
		self.MinMoveSpeed = MinMoveSpeed
		self.RandAngleLimit = RandAngleLimit
		self.JumpHeight = JumpHeight


class JumpToTarget:

	def __init__(self, Name, PreJumpAS, JumpAS, LandAS, MaxSpeed, JumpHeight, JumpGravity, PosReduceRatioOnGround, RotReduceRatioOnGround, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreJumpAS = PreJumpAS
		self.JumpAS = JumpAS
		self.LandAS = LandAS
		self.MaxSpeed = MaxSpeed
		self.JumpHeight = JumpHeight
		self.JumpGravity = JumpGravity
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.InWaterDepth = InWaterDepth


class JumpToTargetFromWater:

	def __init__(self, Name, PreJumpAS, JumpAS, LandAS, FloatCycleTime, FloatDepth, FloatRadius, MaxSpeed, JumpHeight, JumpGravity, PosReduceRatioOnGround, RotReduceRatioOnGround, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreJumpAS = PreJumpAS
		self.JumpAS = JumpAS
		self.LandAS = LandAS
		self.FloatCycleTime = FloatCycleTime
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.MaxSpeed = MaxSpeed
		self.JumpHeight = JumpHeight
		self.JumpGravity = JumpGravity
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.InWaterDepth = InWaterDepth


class KeepPosInWater:

	def __init__(self, Name, ASKeyName, ForceTurnLimitSpeedStream, ChaceFrontRate, ChaceAngSpeedMax, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.ForceTurnLimitSpeedStream = ForceTurnLimitSpeedStream
		self.ChaceFrontRate = ChaceFrontRate
		self.ChaceAngSpeedMax = ChaceAngSpeedMax
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class KeepStandingPosture:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Kick:

	def __init__(self, Name, Power, UpRate, DirAngle, CanKickArea, RotSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Power = Power
		self.UpRate = UpRate
		self.DirAngle = DirAngle
		self.CanKickArea = CanKickArea
		self.RotSpeed = RotSpeed


class KillAllDemoSoundAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KillSelectActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KillUIScreenAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KokkoCreateDrop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KokkoMove:

	def __init__(self, Name, Speed, ASName, AngularSpeed, IsIgnoreSameAS, IsCancelRequestedPathFirst, IsChangeable, NavMeshGoalDistanceTolerance, AvoidPlayer, UseLocalSteering, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.ASName = ASName
		self.AngularSpeed = AngularSpeed
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.IsCancelRequestedPathFirst = IsCancelRequestedPathFirst
		self.IsChangeable = IsChangeable
		self.NavMeshGoalDistanceTolerance = NavMeshGoalDistanceTolerance
		self.AvoidPlayer = AvoidPlayer
		self.UseLocalSteering = UseLocalSteering


class KokkoMoveWithJump:

	def __init__(self, Name, JumpDir, JumpSpeed, Speed, ASName, AngularSpeed, IsIgnoreSameAS, IsCancelRequestedPathFirst, IsChangeable, NavMeshGoalDistanceTolerance, AvoidPlayer, UseLocalSteering, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpDir = JumpDir
		self.JumpSpeed = JumpSpeed
		self.Speed = Speed
		self.ASName = ASName
		self.AngularSpeed = AngularSpeed
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.IsCancelRequestedPathFirst = IsCancelRequestedPathFirst
		self.IsChangeable = IsChangeable
		self.NavMeshGoalDistanceTolerance = NavMeshGoalDistanceTolerance
		self.AvoidPlayer = AvoidPlayer
		self.UseLocalSteering = UseLocalSteering


class KokkoThrown:

	def __init__(self, Name, GravityScale, AS, RotSpd, ReactionLevel, IsForceOnly, IsOnImpact, ThrownKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GravityScale = GravityScale
		self.AS = AS
		self.RotSpd = RotSpd
		self.ReactionLevel = ReactionLevel
		self.IsForceOnly = IsForceOnly
		self.IsOnImpact = IsOnImpact
		self.ThrownKey = ThrownKey


class KorokFlowerAppear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokFlowerVanish:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokFlowerWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokTargetMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class KorokTargetWait:

	def __init__(self, Name, SpeedDecreRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedDecreRate = SpeedDecreRate


class LandOnCeil:

	def __init__(self, Name, RotRatio, GravityScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRatio = RotRatio
		self.GravityScale = GravityScale


class LandRagdoll:

	def __init__(self, Name, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class LandTeleport:

	def __init__(self, Name, DistXZ, DistY, IsNormalizeAxisY, SearchClosestPointRadius, WaitTime, TimeRand, IsUseChangePos, EffectName, IsLifeGageKeep, IsLand, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistXZ = DistXZ
		self.DistY = DistY
		self.IsNormalizeAxisY = IsNormalizeAxisY
		self.SearchClosestPointRadius = SearchClosestPointRadius
		self.WaitTime = WaitTime
		self.TimeRand = TimeRand
		self.IsUseChangePos = IsUseChangePos
		self.EffectName = EffectName
		self.IsLifeGageKeep = IsLifeGageKeep
		self.IsLand = IsLand


class LandTeleportConsiderCameraDir:

	def __init__(self, Name, CameraDirCoeff, DistXZ, DistY, IsNormalizeAxisY, SearchClosestPointRadius, WaitTime, TimeRand, IsUseChangePos, EffectName, IsLifeGageKeep, IsLand, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CameraDirCoeff = CameraDirCoeff
		self.DistXZ = DistXZ
		self.DistY = DistY
		self.IsNormalizeAxisY = IsNormalizeAxisY
		self.SearchClosestPointRadius = SearchClosestPointRadius
		self.WaitTime = WaitTime
		self.TimeRand = TimeRand
		self.IsUseChangePos = IsUseChangePos
		self.EffectName = EffectName
		self.IsLifeGageKeep = IsLifeGageKeep
		self.IsLand = IsLand


class LargeAttack:

	def __init__(self, Name, Speed, RotSpd, RushRadius, AttackRatio, WeaponIdx, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RushRadius = RushRadius
		self.AttackRatio = AttackRatio
		self.WeaponIdx = WeaponIdx
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle


class LargeDamage:

	def __init__(self, Name, ActionTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ActionTime = ActionTime


class LastBossChemicalPillarAttack:

	def __init__(self, Name, PillarNum, AttackEndWait, CreateInterval, PillarYOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PillarNum = PillarNum
		self.AttackEndWait = AttackEndWait
		self.CreateInterval = CreateInterval
		self.PillarYOffset = PillarYOffset


class LastBossDemoWarp:

	def __init__(self, Name, WarpAnchorUniqName, WarpTime, IsUpdateHomePos, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpAnchorUniqName = WarpAnchorUniqName
		self.WarpTime = WarpTime
		self.IsUpdateHomePos = IsUpdateHomePos


class LastBossFlyWait:

	def __init__(self, Name, Amplitude, Time, MoveRate, EndTime, EndTimeRandRange, BaseYOffset, DamageCounter, WaitAS, IsChemicalOff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Amplitude = Amplitude
		self.Time = Time
		self.MoveRate = MoveRate
		self.EndTime = EndTime
		self.EndTimeRandRange = EndTimeRandRange
		self.BaseYOffset = BaseYOffset
		self.DamageCounter = DamageCounter
		self.WaitAS = WaitAS
		self.IsChemicalOff = IsChemicalOff


class LastBossFlyWaitTurnToTarget:

	def __init__(self, Name, TurnStartDiffAng, TurnASName, TurnRate, Amplitude, Time, MoveRate, EndTime, EndTimeRandRange, BaseYOffset, DamageCounter, WaitAS, IsChemicalOff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartDiffAng = TurnStartDiffAng
		self.TurnASName = TurnASName
		self.TurnRate = TurnRate
		self.Amplitude = Amplitude
		self.Time = Time
		self.MoveRate = MoveRate
		self.EndTime = EndTime
		self.EndTimeRandRange = EndTimeRandRange
		self.BaseYOffset = BaseYOffset
		self.DamageCounter = DamageCounter
		self.WaitAS = WaitAS
		self.IsChemicalOff = IsChemicalOff


class LastBossJustGuard:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LastBossNormalWarp:

	def __init__(self, Name, OffsetLength, OffsetY, WarpTime, ChaseDist, IsUseChangePos, ChaseDistOffset, IsEscapeFromPlayer, HomePosOffset, IsWarpAtGround, CheckShapeRadius, IsChasePlayer, DisableGroundHit, DisableAirWallHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OffsetLength = OffsetLength
		self.OffsetY = OffsetY
		self.WarpTime = WarpTime
		self.ChaseDist = ChaseDist
		self.IsUseChangePos = IsUseChangePos
		self.ChaseDistOffset = ChaseDistOffset
		self.IsEscapeFromPlayer = IsEscapeFromPlayer
		self.HomePosOffset = HomePosOffset
		self.IsWarpAtGround = IsWarpAtGround
		self.CheckShapeRadius = CheckShapeRadius
		self.IsChasePlayer = IsChasePlayer
		self.DisableGroundHit = DisableGroundHit
		self.DisableAirWallHit = DisableAirWallHit


class LastBossPostNormalWarp:

	def __init__(self, Name, WaitTime, NoCryAnime, IsTurnToTarget, ASName, IsCheckDistFromTarget, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.NoCryAnime = NoCryAnime
		self.IsTurnToTarget = IsTurnToTarget
		self.ASName = ASName
		self.IsCheckDistFromTarget = IsCheckDistFromTarget


class LastBossPreNormalWarp:

	def __init__(self, Name, PreWarpWaitTime, IsDeleteEffect, ASName, PosReduce, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreWarpWaitTime = PreWarpWaitTime
		self.IsDeleteEffect = IsDeleteEffect
		self.ASName = ASName
		self.PosReduce = PosReduce


class LastBossRailWarpAction:

	def __init__(self, Name, WarpTime, YOffset, IsUpdateHomePos, IsTurnToPlayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpTime = WarpTime
		self.YOffset = YOffset
		self.IsUpdateHomePos = IsUpdateHomePos
		self.IsTurnToPlayer = IsTurnToPlayer


class LastBossRandomHighWarp:

	def __init__(self, Name, HighPosWarpRate, RandomRate, HighOffsetY, LifeCondition, OffsetLength, OffsetY, WarpTime, ChaseDist, IsUseChangePos, ChaseDistOffset, IsEscapeFromPlayer, HomePosOffset, IsWarpAtGround, CheckShapeRadius, IsChasePlayer, DisableGroundHit, DisableAirWallHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HighPosWarpRate = HighPosWarpRate
		self.RandomRate = RandomRate
		self.HighOffsetY = HighOffsetY
		self.LifeCondition = LifeCondition
		self.OffsetLength = OffsetLength
		self.OffsetY = OffsetY
		self.WarpTime = WarpTime
		self.ChaseDist = ChaseDist
		self.IsUseChangePos = IsUseChangePos
		self.ChaseDistOffset = ChaseDistOffset
		self.IsEscapeFromPlayer = IsEscapeFromPlayer
		self.HomePosOffset = HomePosOffset
		self.IsWarpAtGround = IsWarpAtGround
		self.CheckShapeRadius = CheckShapeRadius
		self.IsChasePlayer = IsChasePlayer
		self.DisableGroundHit = DisableGroundHit
		self.DisableAirWallHit = DisableAirWallHit


class LastBossStun:

	def __init__(self, Name, StunTime, AddStunTime, ShockWaveDownTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StunTime = StunTime
		self.AddStunTime = AddStunTime
		self.ShockWaveDownTime = ShockWaveDownTime


class LastBossThunderAppear:

	def __init__(self, Name, AppearTime, AtMinDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AppearTime = AppearTime
		self.AtMinDamage = AtMinDamage


class LastBossThunderSign:

	def __init__(self, Name, SignTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SignTime = SignTime


class LevelFlyLookDownToTgtHeight:

	def __init__(self, Name, Height, Speed, RotSpeed, PosReduceRatio, RotRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Height = Height
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.PosReduceRatio = PosReduceRatio
		self.RotRatio = RotRatio
		self.ASName = ASName


class LevelFlyLookRisingToTgtHeight:

	def __init__(self, Name, Height, Speed, RotSpeed, PosReduceRatio, RotRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Height = Height
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.PosReduceRatio = PosReduceRatio
		self.RotRatio = RotRatio
		self.ASName = ASName


class LevelFlyMove:

	def __init__(self, Name, ASName, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, IsOverRise, CheckStopSpeed, IsSlowDownNearGoal, VibrateMemoryStep, VibrateCheckFrame, VibrateStopCheck, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.IsOverRise = IsOverRise
		self.CheckStopSpeed = CheckStopSpeed
		self.IsSlowDownNearGoal = IsSlowDownNearGoal
		self.VibrateMemoryStep = VibrateMemoryStep
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateStopCheck = VibrateStopCheck
		self.FlyHeightMin = FlyHeightMin


class LevelFlyRise:

	def __init__(self, Name, Height, Speed, PosReduceRatio, RotRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Height = Height
		self.Speed = Speed
		self.PosReduceRatio = PosReduceRatio
		self.RotRatio = RotRatio
		self.ASName = ASName


class LevelFlyRiseLookingTarget:

	def __init__(self, Name, Height, Speed, RotSpeed, PosReduceRatio, RotRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Height = Height
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.PosReduceRatio = PosReduceRatio
		self.RotRatio = RotRatio
		self.ASName = ASName


class LiftTurn:

	def __init__(self, Name, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class LiftWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class LinearFlyAttack:

	def __init__(self, Name, AttackSpeed, AttackSlowDownRatio, Time, TargetHeightOffset, ThroughDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackSpeed = AttackSpeed
		self.AttackSlowDownRatio = AttackSlowDownRatio
		self.Time = Time
		self.TargetHeightOffset = TargetHeightOffset
		self.ThroughDist = ThroughDist


class LinkTagBaseAction:

	def __init__(self, Name, CheckType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckType = CheckType


class LinkTagCountAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LinkTagPulseAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ListenerFixPositionAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ListenerSetModeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LoadSaveDataFromGameOver:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LookAtObject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LookAtObjectSeachAwareness:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LookAtTarget:

	def __init__(self, Name, ASKeyName, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class LookAtTheFront:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LynelAttackASPlay:

	def __init__(self, Name, RotSpeed, Speed, TransAccRatio, RotAccRatio, Range, WeaponIdx, IsIgnoreSame, ASName, EndState, ChangeableTiming, PosReduceRatio, RotReduceRatio, UseAnimeDriven, IsCheckNavMesh, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.Speed = Speed
		self.TransAccRatio = TransAccRatio
		self.RotAccRatio = RotAccRatio
		self.Range = Range
		self.WeaponIdx = WeaponIdx
		self.IsIgnoreSame = IsIgnoreSame
		self.ASName = ASName
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.UseAnimeDriven = UseAnimeDriven
		self.IsCheckNavMesh = IsCheckNavMesh
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class LynelBreathMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class LynelDrawWeapon:

	def __init__(self, Name, ASName, WeaponIdx0, WeaponIdx1, SeqBank, TargetBone, ASWeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx0 = WeaponIdx0
		self.WeaponIdx1 = WeaponIdx1
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.ASWeaponIdx = ASWeaponIdx


class LynelHighJumpAttack:

	def __init__(self, Name, MaxSpeed, WeaponIdx, JumpHeight, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, IsForceGuardBreak, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.WeaponIdx = WeaponIdx
		self.JumpHeight = JumpHeight
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle
		self.IsForceGuardBreak = IsForceGuardBreak


class LynelMove:

	def __init__(self, Name, TimeForCalcCheckCliffDist, FinRadius, WeaponIdx, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TimeForCalcCheckCliffDist = TimeForCalcCheckCliffDist
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance


class LynelNavMeshMove:

	def __init__(self, Name, MinUseGear, MaxUseGear, UseGearType, CanUseHorseGearInput, IsAutoGearDownEnabled, AutoStopAndTurnMode, MinGearAtAutoGearDown, HasToDecelerateNearGoal, GoalDistanceTolerance, WaitUntilPathSucceeded, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinUseGear = MinUseGear
		self.MaxUseGear = MaxUseGear
		self.UseGearType = UseGearType
		self.CanUseHorseGearInput = CanUseHorseGearInput
		self.IsAutoGearDownEnabled = IsAutoGearDownEnabled
		self.AutoStopAndTurnMode = AutoStopAndTurnMode
		self.MinGearAtAutoGearDown = MinGearAtAutoGearDown
		self.HasToDecelerateNearGoal = HasToDecelerateNearGoal
		self.GoalDistanceTolerance = GoalDistanceTolerance
		self.WaitUntilPathSucceeded = WaitUntilPathSucceeded


class LynelRodeo:

	def __init__(self, Name, ForwardSpeed, SideSpeed, RotSpeed, TurnCheckAngleStep, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForwardSpeed = ForwardSpeed
		self.SideSpeed = SideSpeed
		self.RotSpeed = RotSpeed
		self.TurnCheckAngleStep = TurnCheckAngleStep


class LynelSpinAttack:

	def __init__(self, Name, StartASName, LoopASName, EndASName, MinLoopTime, LoopEndAngle, WeaponIdx, IsNoRod, SeqBank, TargetBone, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsHeavy, IsHammer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartASName = StartASName
		self.LoopASName = LoopASName
		self.EndASName = EndASName
		self.MinLoopTime = MinLoopTime
		self.LoopEndAngle = LoopEndAngle
		self.WeaponIdx = WeaponIdx
		self.IsNoRod = IsNoRod
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer


class LyzalfosFlame:

	def __init__(self, Name, ChaseMax, ChaseRate, LengthFrame, AtResetTime, AtChaseFrame, BindGrabNodeIdx, OffsetRot, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChaseMax = ChaseMax
		self.ChaseRate = ChaseRate
		self.LengthFrame = LengthFrame
		self.AtResetTime = AtResetTime
		self.AtChaseFrame = AtChaseFrame
		self.BindGrabNodeIdx = BindGrabNodeIdx
		self.OffsetRot = OffsetRot
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class MagneGearEmbeded:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MagneGearGrabbed:

	def __init__(self, Name, ConnectDistance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ConnectDistance = ConnectDistance


class MamonoShopStand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MarkPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MarkPositionFromGameData:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Mimic:

	def __init__(self, Name, MimicStartASName, MimicLoopASName, MimicEndASName, MimicRate, MimicTime, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MimicStartASName = MimicStartASName
		self.MimicLoopASName = MimicLoopASName
		self.MimicEndASName = MimicEndASName
		self.MimicRate = MimicRate
		self.MimicTime = MimicTime
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class MimicFreeze:

	def __init__(self, Name, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class MoonMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MotorcycleAppear:

	def __init__(self, Name, HideFrames, ModelWarpEffectFrames, EndFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HideFrames = HideFrames
		self.ModelWarpEffectFrames = ModelWarpEffectFrames
		self.EndFrames = EndFrames


class MotorcycleDisappear:

	def __init__(self, Name, ModelWarpEffectFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ModelWarpEffectFrames = ModelWarpEffectFrames


class MotorcycleRiddenByPlayer:

	def __init__(self, Name, RideOnDelayFrames, FallThresholdForThrowOff, CrashVelocityDeltaThreshold, ChargeVelocityThreshold, DriftCutGrassRange, DriftCutGrassIntensity, CutLowTreeVelocityThreshold, CutLowTreeVelocitySize, TerrorVelocityThreshold1, TerrorVelocityThreshold2, TerrorVelocityThreshold3, TerrorVelocityThreshold4, TerrorRadius, TerrorOffsetDistanceSec, AttackChargeBoneOffset, ForbidSpinturnAngleRange, PermitManualWheelieAngleRange, CrashVelocityThreshold, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RideOnDelayFrames = RideOnDelayFrames
		self.FallThresholdForThrowOff = FallThresholdForThrowOff
		self.CrashVelocityDeltaThreshold = CrashVelocityDeltaThreshold
		self.ChargeVelocityThreshold = ChargeVelocityThreshold
		self.DriftCutGrassRange = DriftCutGrassRange
		self.DriftCutGrassIntensity = DriftCutGrassIntensity
		self.CutLowTreeVelocityThreshold = CutLowTreeVelocityThreshold
		self.CutLowTreeVelocitySize = CutLowTreeVelocitySize
		self.TerrorVelocityThreshold1 = TerrorVelocityThreshold1
		self.TerrorVelocityThreshold2 = TerrorVelocityThreshold2
		self.TerrorVelocityThreshold3 = TerrorVelocityThreshold3
		self.TerrorVelocityThreshold4 = TerrorVelocityThreshold4
		self.TerrorRadius = TerrorRadius
		self.TerrorOffsetDistanceSec = TerrorOffsetDistanceSec
		self.AttackChargeBoneOffset = AttackChargeBoneOffset
		self.ForbidSpinturnAngleRange = ForbidSpinturnAngleRange
		self.PermitManualWheelieAngleRange = PermitManualWheelieAngleRange
		self.CrashVelocityThreshold = CrashVelocityThreshold


class MotorcycleWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MotorcycleWaitForEvent:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MotorcycleWaitUntilFellOver:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Move2HomePos:

	def __init__(self, Name, IsVibration, VibPower, VibRange, VibPattern, VibDirection, IsReturn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsVibration = IsVibration
		self.VibPower = VibPower
		self.VibRange = VibRange
		self.VibPattern = VibPattern
		self.VibDirection = VibDirection
		self.IsReturn = IsReturn


class MoveByAnimeDriven:

	def __init__(self, Name, ASKeyName, TargetBoneName, IsChangeable, IsIgnoreSameAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.TargetBoneName = TargetBoneName
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS


class MoveByAnimeDrivenCheckNavMesh:

	def __init__(self, Name, ASKeyName, TargetBoneName, IsChangeable, IsIgnoreSameAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.TargetBoneName = TargetBoneName
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS


class MoveByAnimeDrivenDynAS:

	def __init__(self, Name, ASKeyName, TargetBoneName, IsChangeable, IsIgnoreSameAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.TargetBoneName = TargetBoneName
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS


class MoveByAnimeDrivenToTarget:

	def __init__(self, Name, AnimRotateMax, ASKeyName, TargetBoneName, IsChangeable, IsIgnoreSameAS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimRotateMax = AnimRotateMax
		self.ASKeyName = ASKeyName
		self.TargetBoneName = TargetBoneName
		self.IsChangeable = IsChangeable
		self.IsIgnoreSameAS = IsIgnoreSameAS


class MoveKeyFramed:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MoveMainRidigBody:

	def __init__(self, Name, TargetPosOffset, FinLength, MaxSpeed, VibrateStopCheck, VibrateCheckFrame, VibrateMemoryStep, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetPosOffset = TargetPosOffset
		self.FinLength = FinLength
		self.MaxSpeed = MaxSpeed
		self.VibrateStopCheck = VibrateStopCheck
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateMemoryStep = VibrateMemoryStep


class MoveToHomeMtx:

	def __init__(self, Name, ToHomeMtxLocal, SetEnd, DisableModelDraw, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ToHomeMtxLocal = ToHomeMtxLocal
		self.SetEnd = SetEnd
		self.DisableModelDraw = DisableModelDraw


class MoveToTarget:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MoveToTargetCurve:

	def __init__(self, Name, MaxHeight, TimeScale, IsDebugDrawTargetPos, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxHeight = MaxHeight
		self.TimeScale = TimeScale
		self.IsDebugDrawTargetPos = IsDebugDrawTargetPos


class MoveToTargetDir:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MoveWithAS:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class MoveWithDynAS:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class Msg2CameraKeepState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Msg2CameraReset:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Msg2CameraResetInterpolate:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Msg2CameraResetNoConnect:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class MultiVacuumRotScaleTimeByDist:

	def __init__(self, Name, MaxTimeDist, RotSpd, PosReduceRatio, EndDist, MaxDist, TargetAccRate, TargetSpeed, BaseWeight, VacuumPosOffset, Time, AddTimeVacuuming, AddTimeNearVacuuming, VacuumAngle, VacuumNum, StartAS, LoopAS, EndAS, NearDist, ChangeableTiming, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxTimeDist = MaxTimeDist
		self.RotSpd = RotSpd
		self.PosReduceRatio = PosReduceRatio
		self.EndDist = EndDist
		self.MaxDist = MaxDist
		self.TargetAccRate = TargetAccRate
		self.TargetSpeed = TargetSpeed
		self.BaseWeight = BaseWeight
		self.VacuumPosOffset = VacuumPosOffset
		self.Time = Time
		self.AddTimeVacuuming = AddTimeVacuuming
		self.AddTimeNearVacuuming = AddTimeNearVacuuming
		self.VacuumAngle = VacuumAngle
		self.VacuumNum = VacuumNum
		self.StartAS = StartAS
		self.LoopAS = LoopAS
		self.EndAS = EndAS
		self.NearDist = NearDist
		self.ChangeableTiming = ChangeableTiming


class MusicianSpotBgmTriggerAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCAnchorWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCArmorProcessing:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCArtistAnchorWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCBuyHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCBuyItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCCalculateMaterialValue:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCChangeBoots:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCCheckHorseAssociated:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCCloseHorseCustom:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCDeliverHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCDyeGoods:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCDyeShopCloseMaterial:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCDyeShopReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCDyeShopSelectMaterial:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCEndHorseReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCEscape:

	def __init__(self, Name, MaxDistance, MinDistance, AngularRange, ASName, VerticalEscapeSpeed, WallHitTime, StopTime, IsTurnToTargetPos, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDistance = MaxDistance
		self.MinDistance = MinDistance
		self.AngularRange = AngularRange
		self.ASName = ASName
		self.VerticalEscapeSpeed = VerticalEscapeSpeed
		self.WallHitTime = WallHitTime
		self.StopTime = StopTime
		self.IsTurnToTargetPos = IsTurnToTargetPos
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class NPCEventWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCGiveReward:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCHorseCustomReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCHorseReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCHorseReceptionRelease:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCHorseReceptionResurrect:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCHorseResurrect:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCInfoOffHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCInfoOnHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCInfoOnNamedHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCKnockBackMove:

	def __init__(self, Name, ASKeyName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName


class NPCLerpAction:

	def __init__(self, Name, ASName, RotateSpeed, ArriveDist, IsRotateByRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.RotateSpeed = RotateSpeed
		self.ArriveDist = ArriveDist
		self.IsRotateByRot = IsRotateByRot


class NPCLerpDynAS:

	def __init__(self, Name, ASName, RotateSpeed, ArriveDist, IsRotateByRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.RotateSpeed = RotateSpeed
		self.ArriveDist = ArriveDist
		self.IsRotateByRot = IsRotateByRot


class NPCMakeArtifact:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCMakeItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCManufactItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCNameHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCPurchase:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCPurchaseEnemyMaterial:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCPurchaseMaterial:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCReceiveHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCRegisterAndReceiveHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCRegisterHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCReleaseHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSale:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSaleAppReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSaleCollectedItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSalePictureReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSaleReception:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSellApp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSellHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCSellItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCStartTurnToPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTalk:

	def __init__(self, Name, IsRemainOpeningDialog, MinTalkTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsRemainOpeningDialog = IsRemainOpeningDialog
		self.MinTalkTime = MinTalkTime


class NPCTalkASyncAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTalkNoMessageStepperAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTalkToPlayerAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTargetMove:

	def __init__(self, Name, ASKeyName, GoalDistance, RunGoalDistance, DistOnFailure, UpdateTargetPosInterval, WallHitTime, StopTime, IsPathOptimization, IsShelterFromRain, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.GoalDistance = GoalDistance
		self.RunGoalDistance = RunGoalDistance
		self.DistOnFailure = DistOnFailure
		self.UpdateTargetPosInterval = UpdateTargetPosInterval
		self.WallHitTime = WallHitTime
		self.StopTime = StopTime
		self.IsPathOptimization = IsPathOptimization
		self.IsShelterFromRain = IsShelterFromRain
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class NPCTargetMoveDynAs:

	def __init__(self, Name, ASKeyName, GoalDistance, RunGoalDistance, DistOnFailure, UpdateTargetPosInterval, WallHitTime, StopTime, IsPathOptimization, IsShelterFromRain, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.GoalDistance = GoalDistance
		self.RunGoalDistance = RunGoalDistance
		self.DistOnFailure = DistOnFailure
		self.UpdateTargetPosInterval = UpdateTargetPosInterval
		self.WallHitTime = WallHitTime
		self.StopTime = StopTime
		self.IsPathOptimization = IsPathOptimization
		self.IsShelterFromRain = IsShelterFromRain
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class NPCTebaApproachPlayer:

	def __init__(self, Name, PlayerMaxHeight, MaxMoveSpeed, TurnSpeed, TurnRadius, UpdateTargetFrame, ReduceMaxSpeedChasePlayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayerMaxHeight = PlayerMaxHeight
		self.MaxMoveSpeed = MaxMoveSpeed
		self.TurnSpeed = TurnSpeed
		self.TurnRadius = TurnRadius
		self.UpdateTargetFrame = UpdateTargetFrame
		self.ReduceMaxSpeedChasePlayer = ReduceMaxSpeedChasePlayer


class NPCTravelerRest:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTurnAction:

	def __init__(self, Name, TurnFrame, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnFrame = TurnFrame
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCTurnToObject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTurnToObjectGreeting:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCTurnToPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NPCWait:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCWaitAction:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCWaitDynAS:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCWaitDynFrame:

	def __init__(self, Name, WaitFrame, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCWaitFrame:

	def __init__(self, Name, WaitFrame, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NPCWaitOneTimeAction:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NavMeshBattleWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshConnectAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NavMeshEscape:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshFly:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshGrabLeftWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshGrabRightWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshGuardRun:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshGuardWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshJump:

	def __init__(self, Name, MaxSpeed, JumpHeight, JumpGravity, PosReduceRatioOnGround, RotReduceRatioOnGround, InWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.JumpHeight = JumpHeight
		self.JumpGravity = JumpGravity
		self.PosReduceRatioOnGround = PosReduceRatioOnGround
		self.RotReduceRatioOnGround = RotReduceRatioOnGround
		self.InWaterDepth = InWaterDepth


class NavMeshLiftWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshMoveWithAS:

	def __init__(self, Name, ASName, IsIgnoreSameAS, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshRun:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshSlippedWalk:

	def __init__(self, Name, AccRatio, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AccRatio = AccRatio
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.IsCheckCliff = IsCheckCliff


class NavMeshSwim:

	def __init__(self, Name, InWaterDepth, FloatDepth, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NavMeshWalk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class NearHomePosTeleport:

	def __init__(self, Name, DistXZ, DistY, IsNormalizeAxisY, SearchClosestPointRadius, WaitTime, TimeRand, IsUseChangePos, EffectName, IsLifeGageKeep, IsLand, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistXZ = DistXZ
		self.DistY = DistY
		self.IsNormalizeAxisY = IsNormalizeAxisY
		self.SearchClosestPointRadius = SearchClosestPointRadius
		self.WaitTime = WaitTime
		self.TimeRand = TimeRand
		self.IsUseChangePos = IsUseChangePos
		self.EffectName = EffectName
		self.IsLifeGageKeep = IsLifeGageKeep
		self.IsLand = IsLand


class NoAtTackleMove:

	def __init__(self, Name, AS, Speed, RotSpd, FailAngle, BaseRotRatio, FinRadius, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FailAngle = FailAngle
		self.BaseRotRatio = BaseRotRatio
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx


class NoAutoPlacementEnemyDeadlyQuest:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NoCountDead:

	def __init__(self, Name, IsFadeout, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsFadeout = IsFadeout


class NoDeleteCurrentActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class NotStopXLinkWithDemoVisibleOff:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Notice:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class NoticeTurn:

	def __init__(self, Name, NoDoubleNoticeTime, AngSpd, ASName, IsJumpType, IsChangeable, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoDoubleNoticeTime = NoDoubleNoticeTime
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.IsJumpType = IsJumpType
		self.IsChangeable = IsChangeable


class NpcRideWaitAction:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey


class NpcSwimMove:

	def __init__(self, Name, RotRadPerSec, ASName, WallHitTime, FinRadius, FinHeight, FinRotate, AddCalcStickX, IsClampRotVel, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRadPerSec = RotRadPerSec
		self.ASName = ASName
		self.WallHitTime = WallHitTime
		self.FinRadius = FinRadius
		self.FinHeight = FinHeight
		self.FinRotate = FinRotate
		self.AddCalcStickX = AddCalcStickX
		self.IsClampRotVel = IsClampRotVel
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed


class NpcSwimNavMove:

	def __init__(self, Name, ASName, UpdateTargetPosInterval, RotRadPerSec, WallHitTime, FinRadius, FinHeight, FinRotate, AddCalcStickX, IsClampRotVel, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsSuccessWhenGoalReached, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.UpdateTargetPosInterval = UpdateTargetPosInterval
		self.RotRadPerSec = RotRadPerSec
		self.WallHitTime = WallHitTime
		self.FinRadius = FinRadius
		self.FinHeight = FinHeight
		self.FinRotate = FinRotate
		self.AddCalcStickX = AddCalcStickX
		self.IsClampRotVel = IsClampRotVel
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsSuccessWhenGoalReached = IsSuccessWhenGoalReached


class NpcTebaFly:

	def __init__(self, Name, StartTurnDist, TurnSpeed, InterpolateTurnFrameForMaxSpeed, InterpolateMoveFrameForMaxSpeed, TurnEndRad, MoveSpeedMin, MoveSpeedMax, TurnEnableFrame, TurnReduceSpeedRatio, EvacuateRemainsDist, TargetPosRatio, PlayerApproachCannonDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartTurnDist = StartTurnDist
		self.TurnSpeed = TurnSpeed
		self.InterpolateTurnFrameForMaxSpeed = InterpolateTurnFrameForMaxSpeed
		self.InterpolateMoveFrameForMaxSpeed = InterpolateMoveFrameForMaxSpeed
		self.TurnEndRad = TurnEndRad
		self.MoveSpeedMin = MoveSpeedMin
		self.MoveSpeedMax = MoveSpeedMax
		self.TurnEnableFrame = TurnEnableFrame
		self.TurnReduceSpeedRatio = TurnReduceSpeedRatio
		self.EvacuateRemainsDist = EvacuateRemainsDist
		self.TargetPosRatio = TargetPosRatio
		self.PlayerApproachCannonDist = PlayerApproachCannonDist


class NullASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class ObjBoardWoodTriangle01:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ObservationPointAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OctarockBalloon:

	def __init__(self, Name, StartASName, SignASName, TargetScale, StartSignTimer, ConnectReleaseTimer, ClampWindForceScale, ReduceVel, UpLimitSpeed, MaxAccel, MassScale, IsChaseInitHeight, HeightLimit, BreakTimer, WindAccScale, WindSpdScale, StayAccScale, ReturnToOriginalPos, ReturnStrengthFactor, RemainsHeightLimit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartASName = StartASName
		self.SignASName = SignASName
		self.TargetScale = TargetScale
		self.StartSignTimer = StartSignTimer
		self.ConnectReleaseTimer = ConnectReleaseTimer
		self.ClampWindForceScale = ClampWindForceScale
		self.ReduceVel = ReduceVel
		self.UpLimitSpeed = UpLimitSpeed
		self.MaxAccel = MaxAccel
		self.MassScale = MassScale
		self.IsChaseInitHeight = IsChaseInitHeight
		self.HeightLimit = HeightLimit
		self.BreakTimer = BreakTimer
		self.WindAccScale = WindAccScale
		self.WindSpdScale = WindSpdScale
		self.StayAccScale = StayAccScale
		self.ReturnToOriginalPos = ReturnToOriginalPos
		self.ReturnStrengthFactor = ReturnStrengthFactor
		self.RemainsHeightLimit = RemainsHeightLimit


class OctarockBulletLExplode:

	def __init__(self, Name, SizeUpTime, ExplodeTime, UseDefaultEffect, IsDelete, IsDamageGuarantee, AttackIntensity, IsVanish, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SizeUpTime = SizeUpTime
		self.ExplodeTime = ExplodeTime
		self.UseDefaultEffect = UseDefaultEffect
		self.IsDelete = IsDelete
		self.IsDamageGuarantee = IsDamageGuarantee
		self.AttackIntensity = AttackIntensity
		self.IsVanish = IsVanish


class OctarockReloadWig:

	def __init__(self, Name, GrabIdx, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.GrabIdx = GrabIdx
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class Off:

	def __init__(self, Name, LinkTagType, OffWaitRevival, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.OffWaitRevival = OffWaitRevival
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class OffMiss:

	def __init__(self, Name, LinkTagType, OffWaitRevival, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.OffWaitRevival = OffWaitRevival
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class OkAutoPlacementEnemyDeadlyQuest:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class On:

	def __init__(self, Name, LinkTagType, OnWaitRevival, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.OnWaitRevival = OnWaitRevival
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class OnCliffTurn:

	def __init__(self, Name, ASName, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class OnCliffWait:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.ASName = ASName


class OnCorrect:

	def __init__(self, Name, LinkTagType, OnWaitRevival, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LinkTagType = LinkTagType
		self.OnWaitRevival = OnWaitRevival
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class OnEnterSwapDropTableActor:

	def __init__(self, Name, DieType, TableName, OnGroundPos, IsChangeable, EndState, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DieType = DieType
		self.TableName = TableName
		self.OnGroundPos = OnGroundPos
		self.IsChangeable = IsChangeable
		self.EndState = EndState


class OnLeaveAttackInterval:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OnMUAssignSaveForUsed:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OneTimeEffectLocaterAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OneTimeStopASPlayerNoEnd:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OneTimeWaterFloatStopASPlay:

	def __init__(self, Name, ASName, IgnoreSameAS, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IgnoreSameAS = IgnoreSameAS
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class OnetimeChangeableASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OnetimeHoverASPlay:

	def __init__(self, Name, ASName, IsIgnoreSameAS, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OnetimeMoveASPlay:

	def __init__(self, Name, IsChangable, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsChangable = IsChangable
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OnetimeStopASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OnetimeStopASSyncPlay:

	def __init__(self, Name, SyncASName, SyncASSlot, SyncASSequenceBank, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SyncASName = SyncASName
		self.SyncASSlot = SyncASSlot
		self.SyncASSequenceBank = SyncASSequenceBank
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class OpenClockTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenDungeonMessage:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenDungeonSmallTitle:

	def __init__(self, Name, Mstxt, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Mstxt = Mstxt


class OpenDungeonSmallTitleSetLabel:

	def __init__(self, Name, Mstxt, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Mstxt = Mstxt


class OpenDungeonTitle:

	def __init__(self, Name, Mstxt, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Mstxt = Mstxt


class OpenDungeonTitleSetLabel:

	def __init__(self, Name, Mstxt, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Mstxt = Mstxt


class OpenEnduranceFloorNumber:

	def __init__(self, Name, Mstxt, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Mstxt = Mstxt


class OpenGetDemoDialog:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenGetDemoDialogDressFairy:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenItemCategory:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenItemDownloadDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenItemMenu:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenMap:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenMessageDialog:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenMessageDialogTrig:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenMessageDialogWithSkelAnm:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenPickup:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenPorch:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenPouchAddStockNum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OpenThanksE3:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class OwnedHorseObserveAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PauseMenuPlayerWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PhysBodyPartLod:

	def __init__(self, Name, LodType, RemoveDistance, RemoveDistanceOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LodType = LodType
		self.RemoveDistance = RemoveDistance
		self.RemoveDistanceOffset = RemoveDistanceOffset


class PlayASForAnimalUnit:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class PlayASForAnimalUnitRestricted:

	def __init__(self, Name, ASKeyName, AllowChangeableFrame, IsIgnoreSameAS, SelectNextGearType, SelectNextGear, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.AllowChangeableFrame = AllowChangeableFrame
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.SelectNextGearType = SelectNextGearType
		self.SelectNextGear = SelectNextGear


class PlayASForDemo:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayASForDemoPreMove:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayASForDemoWithSword:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayASForTimeline:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayASForTimelineWithSword:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayerActionClimb:

	def __init__(self, Name, RayCastOffsetY, EndGroundAngle, BodyFixedOffset, RayCastLength, DashAnmSpdRate, FlickThresholdMin, FlickThresholdMax, FlickWaitToOverMaxTime, FlickOverMaxToReturnTime, LockingAfterJumpCnt, StaminaDownAlways, StaminaDownTriggerJump, StaminaDownWait, ForceStartMoveVelYMin, ChargeJumpScaleMin, ChargeJumpScaleMax, ChargeJumpLevel1Frame, ChageJumpLevel2Frame, StaminaDownScaleInRain, StaminaScaleTriggerJumpLv1, StaminaScaleTriggerJumpLv2, StaminaScaleTriggerJumpLv3, JumpScaleWhenLitteleStamina, NoiseMaxSpeedMove, NoiseMaxValueMove, NoiseMaxValueJump, FallLimitWallAngle, StaminaRateMovingUp, StaminaRateMovingSide, StaminaRateMovingDown, StaminaRateSlopeCenter, StaminaRateSlopeMin, StaminaRateSlopeMax, BodyDiffLengthMaxNormal, BodyDiffLengthMaxJump, EndWaitRate, BaseCountSlipInRain, RandomCountSlipInRain, BaseSpeedSlipInRain, RandomSpeedSlipInRain, DownStaminaSlipInRain, OcclusionCheckLength, StaminaDownAlwaysMaxSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RayCastOffsetY = RayCastOffsetY
		self.EndGroundAngle = EndGroundAngle
		self.BodyFixedOffset = BodyFixedOffset
		self.RayCastLength = RayCastLength
		self.DashAnmSpdRate = DashAnmSpdRate
		self.FlickThresholdMin = FlickThresholdMin
		self.FlickThresholdMax = FlickThresholdMax
		self.FlickWaitToOverMaxTime = FlickWaitToOverMaxTime
		self.FlickOverMaxToReturnTime = FlickOverMaxToReturnTime
		self.LockingAfterJumpCnt = LockingAfterJumpCnt
		self.StaminaDownAlways = StaminaDownAlways
		self.StaminaDownTriggerJump = StaminaDownTriggerJump
		self.StaminaDownWait = StaminaDownWait
		self.ForceStartMoveVelYMin = ForceStartMoveVelYMin
		self.ChargeJumpScaleMin = ChargeJumpScaleMin
		self.ChargeJumpScaleMax = ChargeJumpScaleMax
		self.ChargeJumpLevel1Frame = ChargeJumpLevel1Frame
		self.ChageJumpLevel2Frame = ChageJumpLevel2Frame
		self.StaminaDownScaleInRain = StaminaDownScaleInRain
		self.StaminaScaleTriggerJumpLv1 = StaminaScaleTriggerJumpLv1
		self.StaminaScaleTriggerJumpLv2 = StaminaScaleTriggerJumpLv2
		self.StaminaScaleTriggerJumpLv3 = StaminaScaleTriggerJumpLv3
		self.JumpScaleWhenLitteleStamina = JumpScaleWhenLitteleStamina
		self.NoiseMaxSpeedMove = NoiseMaxSpeedMove
		self.NoiseMaxValueMove = NoiseMaxValueMove
		self.NoiseMaxValueJump = NoiseMaxValueJump
		self.FallLimitWallAngle = FallLimitWallAngle
		self.StaminaRateMovingUp = StaminaRateMovingUp
		self.StaminaRateMovingSide = StaminaRateMovingSide
		self.StaminaRateMovingDown = StaminaRateMovingDown
		self.StaminaRateSlopeCenter = StaminaRateSlopeCenter
		self.StaminaRateSlopeMin = StaminaRateSlopeMin
		self.StaminaRateSlopeMax = StaminaRateSlopeMax
		self.BodyDiffLengthMaxNormal = BodyDiffLengthMaxNormal
		self.BodyDiffLengthMaxJump = BodyDiffLengthMaxJump
		self.EndWaitRate = EndWaitRate
		self.BaseCountSlipInRain = BaseCountSlipInRain
		self.RandomCountSlipInRain = RandomCountSlipInRain
		self.BaseSpeedSlipInRain = BaseSpeedSlipInRain
		self.RandomSpeedSlipInRain = RandomSpeedSlipInRain
		self.DownStaminaSlipInRain = DownStaminaSlipInRain
		self.OcclusionCheckLength = OcclusionCheckLength
		self.StaminaDownAlwaysMaxSpeed = StaminaDownAlwaysMaxSpeed


class PlayerAnchorMove:

	def __init__(self, Name, DecSpdDist, DecStickValue, ForceTurnDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DecSpdDist = DecSpdDist
		self.DecStickValue = DecStickValue
		self.ForceTurnDist = ForceTurnDist


class PlayerAreaInOutSendMessage:

	def __init__(self, Name, MessageSet, BufferNum, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MessageSet = MessageSet
		self.BufferNum = BufferNum


class PlayerAtnMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerAtnWait:

	def __init__(self, Name, AtnTurnDiffAng, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtnTurnDiffAng = AtnTurnDiffAng


class PlayerBackJump:

	def __init__(self, Name, BJSpeedF, NoDamageTime, MySlowStartFrame, ForceSlowTime, JustAvoidTime, BJHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BJSpeedF = BJSpeedF
		self.NoDamageTime = NoDamageTime
		self.MySlowStartFrame = MySlowStartFrame
		self.ForceSlowTime = ForceSlowTime
		self.JustAvoidTime = JustAvoidTime
		self.BJHeight = BJHeight


class PlayerBackJumpLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerBeamMove:

	def __init__(self, Name, LevelRangeMult, LevelAtkMult, LevelScaleMult, IsLevelOneScaleOne, LevelBaseScaleAdd, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LevelRangeMult = LevelRangeMult
		self.LevelAtkMult = LevelAtkMult
		self.LevelScaleMult = LevelScaleMult
		self.IsLevelOneScaleOne = IsLevelOneScaleOne
		self.LevelBaseScaleAdd = LevelBaseScaleAdd
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class PlayerBeetleSubject:

	def __init__(self, Name, AimRange, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AimRange = AimRange


class PlayerBindSheikPad:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerBow:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerBowFall:

	def __init__(self, Name, NoClimbTime, NoClimbTimeTired, NoDispDisableAppTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoClimbTime = NoClimbTime
		self.NoClimbTimeTired = NoClimbTimeTired
		self.NoDispDisableAppTime = NoDispDisableAppTime


class PlayerCalmHorseDown:

	def __init__(self, Name, PlayCalmDownAnimFrames, EnergyDecreasePerSec, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PlayCalmDownAnimFrames = PlayCalmDownAnimFrames
		self.EnergyDecreasePerSec = EnergyDecreasePerSec


class PlayerCaught:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerCleaningAround:

	def __init__(self, Name, CleaningTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CleaningTime = CleaningTime


class PlayerClimbRest:

	def __init__(self, Name, EnergyClimb, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyClimb = EnergyClimb


class PlayerControl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerCutAfterJump:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerCutAfterJust:

	def __init__(self, Name, SlowContTime, LastCutAcceptTime, LastCutAcceptTimeLSword, LastCutAcceptTimeSpear, ForceSlowTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SlowContTime = SlowContTime
		self.LastCutAcceptTime = LastCutAcceptTime
		self.LastCutAcceptTimeLSword = LastCutAcceptTimeLSword
		self.LastCutAcceptTimeSpear = LastCutAcceptTimeSpear
		self.ForceSlowTime = ForceSlowTime


class PlayerCutDash:

	def __init__(self, Name, SearchAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SearchAngle = SearchAngle


class PlayerCutFall:

	def __init__(self, Name, ParashawlInvalidTime, FallSpAttackHeight, FallSpAttackRadiusMin, FallSpAttackRadiusMax, FallSpAttackRadiusAdd, FallSpAttackRadiusAddLSword, FallSpLargeAttackRadius, RumbleType, RumblePowerMin, RumblePowerMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ParashawlInvalidTime = ParashawlInvalidTime
		self.FallSpAttackHeight = FallSpAttackHeight
		self.FallSpAttackRadiusMin = FallSpAttackRadiusMin
		self.FallSpAttackRadiusMax = FallSpAttackRadiusMax
		self.FallSpAttackRadiusAdd = FallSpAttackRadiusAdd
		self.FallSpAttackRadiusAddLSword = FallSpAttackRadiusAddLSword
		self.FallSpLargeAttackRadius = FallSpLargeAttackRadius
		self.RumbleType = RumbleType
		self.RumblePowerMin = RumblePowerMin
		self.RumblePowerMax = RumblePowerMax


class PlayerCutHorseJump:

	def __init__(self, Name, AttackRate, FallSpAttackHeight, FallSpAttackRadiusMin, FallSpAttackRadiusMax, FallSpAttackRadiusAdd, FallSpAttackRadiusAddLSword, FallSpAttackCheckUnderDist, ParashawlInvalidTime, FallSpLargeAttackRadius, RumbleType, RumblePowerMin, RumblePowerMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRate = AttackRate
		self.FallSpAttackHeight = FallSpAttackHeight
		self.FallSpAttackRadiusMin = FallSpAttackRadiusMin
		self.FallSpAttackRadiusMax = FallSpAttackRadiusMax
		self.FallSpAttackRadiusAdd = FallSpAttackRadiusAdd
		self.FallSpAttackRadiusAddLSword = FallSpAttackRadiusAddLSword
		self.FallSpAttackCheckUnderDist = FallSpAttackCheckUnderDist
		self.ParashawlInvalidTime = ParashawlInvalidTime
		self.FallSpLargeAttackRadius = FallSpLargeAttackRadius
		self.RumbleType = RumbleType
		self.RumblePowerMin = RumblePowerMin
		self.RumblePowerMax = RumblePowerMax


class PlayerCutHorseJumpLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerCutJump:

	def __init__(self, Name, AttackRatioNSword, AttackRatioLSword, AttackRatioSpear, CutJumpSpeedF, CutJumpShortSpeedF, CutJumpSpeedFLSword, CutJumpHeight, CutJumpShortHeight, FallSpAttackHeight, FallSpAttackRadiusMin, FallSpAttackRadiusMax, FallSpAttackRadiusAdd, FallSpAttackRadiusAddLSword, FallSpAttackCheckUnderDist, FallSpLargeAttackRadius, AimDistOffset, ParashawlInvalidTime, SwingFrameBeforeGround, RumbleType, RumblePowerMin, RumblePowerMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRatioNSword = AttackRatioNSword
		self.AttackRatioLSword = AttackRatioLSword
		self.AttackRatioSpear = AttackRatioSpear
		self.CutJumpSpeedF = CutJumpSpeedF
		self.CutJumpShortSpeedF = CutJumpShortSpeedF
		self.CutJumpSpeedFLSword = CutJumpSpeedFLSword
		self.CutJumpHeight = CutJumpHeight
		self.CutJumpShortHeight = CutJumpShortHeight
		self.FallSpAttackHeight = FallSpAttackHeight
		self.FallSpAttackRadiusMin = FallSpAttackRadiusMin
		self.FallSpAttackRadiusMax = FallSpAttackRadiusMax
		self.FallSpAttackRadiusAdd = FallSpAttackRadiusAdd
		self.FallSpAttackRadiusAddLSword = FallSpAttackRadiusAddLSword
		self.FallSpAttackCheckUnderDist = FallSpAttackCheckUnderDist
		self.FallSpLargeAttackRadius = FallSpLargeAttackRadius
		self.AimDistOffset = AimDistOffset
		self.ParashawlInvalidTime = ParashawlInvalidTime
		self.SwingFrameBeforeGround = SwingFrameBeforeGround
		self.RumbleType = RumbleType
		self.RumblePowerMin = RumblePowerMin
		self.RumblePowerMax = RumblePowerMax


class PlayerCutNormal:

	def __init__(self, Name, AttackRatioNSwordS2, AttackRatioNSwordS3, AttackRatioLSwordS2, AttackRatioLSwordS3, AttackRatioSpearS2, AttackRatioSpearS3, SwordSearchFrame, SwordSearchAngle, AttackRatioSpearS4, AttackRatioSpearS5, AttackRatioNSwordS1, AttackRatioLSwordS1, AttackRatioSpearS1, SwordSearchAddDistByHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRatioNSwordS2 = AttackRatioNSwordS2
		self.AttackRatioNSwordS3 = AttackRatioNSwordS3
		self.AttackRatioLSwordS2 = AttackRatioLSwordS2
		self.AttackRatioLSwordS3 = AttackRatioLSwordS3
		self.AttackRatioSpearS2 = AttackRatioSpearS2
		self.AttackRatioSpearS3 = AttackRatioSpearS3
		self.SwordSearchFrame = SwordSearchFrame
		self.SwordSearchAngle = SwordSearchAngle
		self.AttackRatioSpearS4 = AttackRatioSpearS4
		self.AttackRatioSpearS5 = AttackRatioSpearS5
		self.AttackRatioNSwordS1 = AttackRatioNSwordS1
		self.AttackRatioLSwordS1 = AttackRatioLSwordS1
		self.AttackRatioSpearS1 = AttackRatioSpearS1
		self.SwordSearchAddDistByHeight = SwordSearchAddDistByHeight


class PlayerCutReverse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerCutTurn:

	def __init__(self, Name, AttackRatioNSword, AttackRatioLSword, AttackRatioSpear, EnergyAttack, RangeDiam, RangeDiamAdd, MaxChargeLvNSword, RangeDiamAddNSword, EnergyChargeStart, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AttackRatioNSword = AttackRatioNSword
		self.AttackRatioLSword = AttackRatioLSword
		self.AttackRatioSpear = AttackRatioSpear
		self.EnergyAttack = EnergyAttack
		self.RangeDiam = RangeDiam
		self.RangeDiamAdd = RangeDiamAdd
		self.MaxChargeLvNSword = MaxChargeLvNSword
		self.RangeDiamAddNSword = RangeDiamAddNSword
		self.EnergyChargeStart = EnergyChargeStart


class PlayerCutTurnLSword:

	def __init__(self, Name, EnergyMove, EnergyLastAttack, MaxSpeedF, MaxTime, AccSpeed, DecSpeed, SpAttackRadiusMin, SpAttackRadiusMax, SpAttackRadiusAdd, SpAttackCheckUnderDist, EnergyChargeStart, SpLargeAttackRadius, RumbleType, RumblePowerMin, RumblePowerMax, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyMove = EnergyMove
		self.EnergyLastAttack = EnergyLastAttack
		self.MaxSpeedF = MaxSpeedF
		self.MaxTime = MaxTime
		self.AccSpeed = AccSpeed
		self.DecSpeed = DecSpeed
		self.SpAttackRadiusMin = SpAttackRadiusMin
		self.SpAttackRadiusMax = SpAttackRadiusMax
		self.SpAttackRadiusAdd = SpAttackRadiusAdd
		self.SpAttackCheckUnderDist = SpAttackCheckUnderDist
		self.EnergyChargeStart = EnergyChargeStart
		self.SpLargeAttackRadius = SpLargeAttackRadius
		self.RumbleType = RumbleType
		self.RumblePowerMin = RumblePowerMin
		self.RumblePowerMax = RumblePowerMax


class PlayerDamage:

	def __init__(self, Name, BaseInitSpeedNSword, BaseInitSpeedLSword, BaseInitSpeedSpear, BaseInitSpeedOther, AddSpeedNSword, AddSpeedLSword, AddSpeedSpear, AddSpeedOther, MaxSpeedNSword, MaxSpeedLSword, MaxSpeedSpear, MaxSpeedOther, DecSpeedNSword, DecSpeedLSword, DecSpeedSpear, DecSpeedOther, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseInitSpeedNSword = BaseInitSpeedNSword
		self.BaseInitSpeedLSword = BaseInitSpeedLSword
		self.BaseInitSpeedSpear = BaseInitSpeedSpear
		self.BaseInitSpeedOther = BaseInitSpeedOther
		self.AddSpeedNSword = AddSpeedNSword
		self.AddSpeedLSword = AddSpeedLSword
		self.AddSpeedSpear = AddSpeedSpear
		self.AddSpeedOther = AddSpeedOther
		self.MaxSpeedNSword = MaxSpeedNSword
		self.MaxSpeedLSword = MaxSpeedLSword
		self.MaxSpeedSpear = MaxSpeedSpear
		self.MaxSpeedOther = MaxSpeedOther
		self.DecSpeedNSword = DecSpeedNSword
		self.DecSpeedLSword = DecSpeedLSword
		self.DecSpeedSpear = DecSpeedSpear
		self.DecSpeedOther = DecSpeedOther


class PlayerDead:

	def __init__(self, Name, RagdollChangeTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RagdollChangeTime = RagdollChangeTime


class PlayerDeadWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDemoAccelerateHorse:

	def __init__(self, Name, ASName, InputAccelerateFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.InputAccelerateFrame = InputAccelerateFrame


class PlayerDemoAirWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDemoWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDestinationMove:

	def __init__(self, Name, DecSpdDist, DecStickValue, ForceTurnDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DecSpdDist = DecSpdDist
		self.DecStickValue = DecStickValue
		self.ForceTurnDist = ForceTurnDist


class PlayerDestinationTurn:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDestinationTurnRefActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDestinationTurnStarter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDestinationTurnWithAnim:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDisplayWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDiveMove:

	def __init__(self, Name, AnmDrivenDist, FinishDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnmDrivenDist = AnmDrivenDist
		self.FinishDist = FinishDist


class PlayerDoorPullOpen:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDoorPushOpen:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerDrown:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerElectric:

	def __init__(self, Name, JumpSpeedF, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpSpeedF = JumpSpeedF
		self.JumpHeight = JumpHeight


class PlayerEmitEquipmentNoise:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerEquipHaveMasterSword:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerEquipNearMasterSword:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerEventStartWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerFall:

	def __init__(self, Name, NoClimbTime, NoClimbTimeTired, NoDispDisableAppTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoClimbTime = NoClimbTime
		self.NoClimbTimeTired = NoClimbTimeTired
		self.NoDispDisableAppTime = NoDispDisableAppTime


class PlayerForkDropWeaponWithSpeed:

	def __init__(self, Name, WeaponDropSpeedXZ, WeaponDropSpeedY, WeaponIdx, AngleOffsetY, ChemReset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponIdx = WeaponIdx
		self.AngleOffsetY = AngleOffsetY
		self.ChemReset = ChemReset


class PlayerFrontRoll:

	def __init__(self, Name, EnergyDec, SpeedDecByAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyDec = EnergyDec
		self.SpeedDecByAngle = SpeedDecByAngle


class PlayerGrabPut:

	def __init__(self, Name, PutStartFrmae, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PutStartFrmae = PutStartFrmae


class PlayerGrabReady:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGrabStand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGrabThrow:

	def __init__(self, Name, OverThrowSpeedYB, OverThrowSpeedFB, OverThrowSpeedYL, OverThrowSpeedFL, OverThrowInertiaRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OverThrowSpeedYB = OverThrowSpeedYB
		self.OverThrowSpeedFB = OverThrowSpeedFB
		self.OverThrowSpeedYL = OverThrowSpeedYL
		self.OverThrowSpeedFL = OverThrowSpeedFL
		self.OverThrowInertiaRate = OverThrowInertiaRate


class PlayerGrabUp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGrabUpAnmStop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGrabWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGuardBreak:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGuardJust:

	def __init__(self, Name, ForceSlowTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceSlowTime = ForceSlowTime


class PlayerGuardJustFall:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerGuardSlip:

	def __init__(self, Name, BaseInitSpeedNSword, BaseInitSpeedLSword, BaseInitSpeedSpear, BaseInitSpeedOther, AddSpeedNSword, AddSpeedLSword, AddSpeedSpear, AddSpeedOther, MaxSpeedNSword, MaxSpeedLSword, MaxSpeedSpear, MaxSpeedOther, DecSpeedNSword, DecSpeedLSword, DecSpeedSpear, DecSpeedOther, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseInitSpeedNSword = BaseInitSpeedNSword
		self.BaseInitSpeedLSword = BaseInitSpeedLSword
		self.BaseInitSpeedSpear = BaseInitSpeedSpear
		self.BaseInitSpeedOther = BaseInitSpeedOther
		self.AddSpeedNSword = AddSpeedNSword
		self.AddSpeedLSword = AddSpeedLSword
		self.AddSpeedSpear = AddSpeedSpear
		self.AddSpeedOther = AddSpeedOther
		self.MaxSpeedNSword = MaxSpeedNSword
		self.MaxSpeedLSword = MaxSpeedLSword
		self.MaxSpeedSpear = MaxSpeedSpear
		self.MaxSpeedOther = MaxSpeedOther
		self.DecSpeedNSword = DecSpeedNSword
		self.DecSpeedLSword = DecSpeedLSword
		self.DecSpeedSpear = DecSpeedSpear
		self.DecSpeedOther = DecSpeedOther


class PlayerHangWallCatch:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerHell:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerHellNoFade:

	def __init__(self, Name, CleaningTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CleaningTime = CleaningTime


class PlayerHellStartWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerHide:

	def __init__(self, Name, Hidden, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Hidden = Hidden


class PlayerHoldUpDRC:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerHorseGetOff:

	def __init__(self, Name, SideFallSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SideFallSpeed = SideFallSpeed


class PlayerHorseGetOffInDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerHorseJump:

	def __init__(self, Name, JumpHeight, JumpSpeedF, JumpSpeedF2, JumpSpeedF3, JumpSpeedF4, JumpMaxSpeedF, AimDistOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.JumpSpeedF = JumpSpeedF
		self.JumpSpeedF2 = JumpSpeedF2
		self.JumpSpeedF3 = JumpSpeedF3
		self.JumpSpeedF4 = JumpSpeedF4
		self.JumpMaxSpeedF = JumpMaxSpeedF
		self.AimDistOffset = AimDistOffset


class PlayerIce:

	def __init__(self, Name, EnergyIce, CountRate, InputInterval, JumpSpeedF, JumpHeight, JumpSpeedFBlowOff, JumpHeightBlowOff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyIce = EnergyIce
		self.CountRate = CountRate
		self.InputInterval = InputInterval
		self.JumpSpeedF = JumpSpeedF
		self.JumpHeight = JumpHeight
		self.JumpSpeedFBlowOff = JumpSpeedFBlowOff
		self.JumpHeightBlowOff = JumpHeightBlowOff


class PlayerIceBlockRemove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerIceBreak:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerIceGrabReady:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerInAreaAutoEnemyForbidTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerJump:

	def __init__(self, Name, EnergyJump, EnergyDashJump, EnergyUseDiam1, EnergyUseDiam2, EnergyUseDiam3, JumpHeight, JumpHeightAddByAngle, JumpHeightAddBySpeed, JumpHeightMaxDecRateByWater, IgnoreWaterHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyJump = EnergyJump
		self.EnergyDashJump = EnergyDashJump
		self.EnergyUseDiam1 = EnergyUseDiam1
		self.EnergyUseDiam2 = EnergyUseDiam2
		self.EnergyUseDiam3 = EnergyUseDiam3
		self.JumpHeight = JumpHeight
		self.JumpHeightAddByAngle = JumpHeightAddByAngle
		self.JumpHeightAddBySpeed = JumpHeightAddBySpeed
		self.JumpHeightMaxDecRateByWater = JumpHeightMaxDecRateByWater
		self.IgnoreWaterHeight = IgnoreWaterHeight


class PlayerKokkoGlide:

	def __init__(self, Name, EnergyGlide, NoEnergyTime, GlideSpeedMax, Lv2GlideSpeedMax, GlideBodyFrontX, GlideBodyBackX, GlideBodySideZ, GlideRotMax, GlideRotMin, GlideRotRate, WindScale, OverSpeedDec, GlideRotSpeed, GlideNoSideAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyGlide = EnergyGlide
		self.NoEnergyTime = NoEnergyTime
		self.GlideSpeedMax = GlideSpeedMax
		self.Lv2GlideSpeedMax = Lv2GlideSpeedMax
		self.GlideBodyFrontX = GlideBodyFrontX
		self.GlideBodyBackX = GlideBodyBackX
		self.GlideBodySideZ = GlideBodySideZ
		self.GlideRotMax = GlideRotMax
		self.GlideRotMin = GlideRotMin
		self.GlideRotRate = GlideRotRate
		self.WindScale = WindScale
		self.OverSpeedDec = OverSpeedDec
		self.GlideRotSpeed = GlideRotSpeed
		self.GlideNoSideAngle = GlideNoSideAngle


class PlayerLadderDownEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLadderDownStart:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLadderJump:

	def __init__(self, Name, EnergyJump, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyJump = EnergyJump


class PlayerLadderJumpLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLadderMove:

	def __init__(self, Name, MoveAnmSpeedMin, MoveAnmSpeedMax, DownMoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveAnmSpeedMin = MoveAnmSpeedMin
		self.MoveAnmSpeedMax = MoveAnmSpeedMax
		self.DownMoveSpeed = DownMoveSpeed


class PlayerLadderToClimb:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLadderUpEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLadderUpStart:

	def __init__(self, Name, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight


class PlayerLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLandDamage:

	def __init__(self, Name, WaitTimeMin, WaitTimeMax, DeadHeight, DamageMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTimeMin = WaitTimeMin
		self.WaitTimeMax = WaitTimeMax
		self.DeadHeight = DeadHeight
		self.DamageMin = DamageMin


class PlayerLargeDamage:

	def __init__(self, Name, BaseInitSpeedNSword, BaseInitSpeedLSword, BaseInitSpeedSpear, BaseInitSpeedOther, AddSpeedNSword, AddSpeedLSword, AddSpeedSpear, AddSpeedOther, MaxSpeedNSword, MaxSpeedLSword, MaxSpeedSpear, MaxSpeedOther, JumpHeightNSword, JumpHeightLSword, JumpHeightSpear, JumpHeightOther, InitSpeedWind, JumpHeightWind, NoRagdollTime, InitSpeedToss, JumpHeightToss, AddLinearImpulse, AddRollImpulse, InitSpeedHorse, JumpHeightHorse, AddLinearImpulseHorse, InitSpeedRynel, JumpHeightRynel, AddLinearImpulseRynel, AddRollImpulseRynel, InitSpeedSandworm, JumpHeightSandworm, AddLinearImpulseSandworm, InitSpeedShakeOff, JumpHeightShakeOff, AddLinearImpulseShakeOff, InitSpeedWindRemain, JumpHeightWindRemain, AddLinearImpulseWindRemain, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseInitSpeedNSword = BaseInitSpeedNSword
		self.BaseInitSpeedLSword = BaseInitSpeedLSword
		self.BaseInitSpeedSpear = BaseInitSpeedSpear
		self.BaseInitSpeedOther = BaseInitSpeedOther
		self.AddSpeedNSword = AddSpeedNSword
		self.AddSpeedLSword = AddSpeedLSword
		self.AddSpeedSpear = AddSpeedSpear
		self.AddSpeedOther = AddSpeedOther
		self.MaxSpeedNSword = MaxSpeedNSword
		self.MaxSpeedLSword = MaxSpeedLSword
		self.MaxSpeedSpear = MaxSpeedSpear
		self.MaxSpeedOther = MaxSpeedOther
		self.JumpHeightNSword = JumpHeightNSword
		self.JumpHeightLSword = JumpHeightLSword
		self.JumpHeightSpear = JumpHeightSpear
		self.JumpHeightOther = JumpHeightOther
		self.InitSpeedWind = InitSpeedWind
		self.JumpHeightWind = JumpHeightWind
		self.NoRagdollTime = NoRagdollTime
		self.InitSpeedToss = InitSpeedToss
		self.JumpHeightToss = JumpHeightToss
		self.AddLinearImpulse = AddLinearImpulse
		self.AddRollImpulse = AddRollImpulse
		self.InitSpeedHorse = InitSpeedHorse
		self.JumpHeightHorse = JumpHeightHorse
		self.AddLinearImpulseHorse = AddLinearImpulseHorse
		self.InitSpeedRynel = InitSpeedRynel
		self.JumpHeightRynel = JumpHeightRynel
		self.AddLinearImpulseRynel = AddLinearImpulseRynel
		self.AddRollImpulseRynel = AddRollImpulseRynel
		self.InitSpeedSandworm = InitSpeedSandworm
		self.JumpHeightSandworm = JumpHeightSandworm
		self.AddLinearImpulseSandworm = AddLinearImpulseSandworm
		self.InitSpeedShakeOff = InitSpeedShakeOff
		self.JumpHeightShakeOff = JumpHeightShakeOff
		self.AddLinearImpulseShakeOff = AddLinearImpulseShakeOff
		self.InitSpeedWindRemain = InitSpeedWindRemain
		self.JumpHeightWindRemain = JumpHeightWindRemain
		self.AddLinearImpulseWindRemain = AddLinearImpulseWindRemain


class PlayerLargeDamageUp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLaunch:

	def __init__(self, Name, InitSpeed, JumpHeight, AddLinearImpulse, AddRollImpulse, NoRagdollTime, Damage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitSpeed = InitSpeed
		self.JumpHeight = JumpHeight
		self.AddLinearImpulse = AddLinearImpulse
		self.AddRollImpulse = AddRollImpulse
		self.NoRagdollTime = NoRagdollTime
		self.Damage = Damage


class PlayerLookAtObject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLookAtObjectNow:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerLookAtTheFront:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerMagnetSubject:

	def __init__(self, Name, DRCEnergy, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DRCEnergy = DRCEnergy


class PlayerMasterSwordEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerMiddleDamage:

	def __init__(self, Name, BaseInitSpeedNSword, BaseInitSpeedLSword, BaseInitSpeedSpear, BaseInitSpeedOther, AddSpeedNSword, AddSpeedLSword, AddSpeedSpear, AddSpeedOther, MaxSpeedNSword, MaxSpeedLSword, MaxSpeedSpear, MaxSpeedOther, DecSpeedNSword, DecSpeedLSword, DecSpeedSpear, DecSpeedOther, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseInitSpeedNSword = BaseInitSpeedNSword
		self.BaseInitSpeedLSword = BaseInitSpeedLSword
		self.BaseInitSpeedSpear = BaseInitSpeedSpear
		self.BaseInitSpeedOther = BaseInitSpeedOther
		self.AddSpeedNSword = AddSpeedNSword
		self.AddSpeedLSword = AddSpeedLSword
		self.AddSpeedSpear = AddSpeedSpear
		self.AddSpeedOther = AddSpeedOther
		self.MaxSpeedNSword = MaxSpeedNSword
		self.MaxSpeedLSword = MaxSpeedLSword
		self.MaxSpeedSpear = MaxSpeedSpear
		self.MaxSpeedOther = MaxSpeedOther
		self.DecSpeedNSword = DecSpeedNSword
		self.DecSpeedLSword = DecSpeedLSword
		self.DecSpeedSpear = DecSpeedSpear
		self.DecSpeedOther = DecSpeedOther


class PlayerMove:

	def __init__(self, Name, EnergyDash, ForceApplyPushAnm, EnergyDashTrig, PushContinueTime, PushStopDistY, InvalidFallFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyDash = EnergyDash
		self.ForceApplyPushAnm = ForceApplyPushAnm
		self.EnergyDashTrig = EnergyDashTrig
		self.PushContinueTime = PushContinueTime
		self.PushStopDistY = PushStopDistY
		self.InvalidFallFrame = InvalidFallFrame


class PlayerNavMeshMove:

	def __init__(self, Name, DecSpdDist, DecStickValue, ForceTurnDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DecSpdDist = DecSpdDist
		self.DecStickValue = DecStickValue
		self.ForceTurnDist = ForceTurnDist


class PlayerParashawlGlide:

	def __init__(self, Name, EnergyGlide, NoEnergyTime, GlideSpeedMax, Lv2GlideSpeedMax, GlideBodyFrontX, GlideBodyBackX, GlideBodySideZ, GlideRotMax, GlideRotMin, GlideRotRate, WindScale, OverSpeedDec, GlideRotSpeed, GlideNoSideAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyGlide = EnergyGlide
		self.NoEnergyTime = NoEnergyTime
		self.GlideSpeedMax = GlideSpeedMax
		self.Lv2GlideSpeedMax = Lv2GlideSpeedMax
		self.GlideBodyFrontX = GlideBodyFrontX
		self.GlideBodyBackX = GlideBodyBackX
		self.GlideBodySideZ = GlideBodySideZ
		self.GlideRotMax = GlideRotMax
		self.GlideRotMin = GlideRotMin
		self.GlideRotRate = GlideRotRate
		self.WindScale = WindScale
		self.OverSpeedDec = OverSpeedDec
		self.GlideRotSpeed = GlideRotSpeed
		self.GlideNoSideAngle = GlideNoSideAngle


class PlayerPickUp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerPlayASAdapt:

	def __init__(self, Name, AnimeDrivenSettings, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimeDrivenSettings = AnimeDrivenSettings


class PlayerPullSword:

	def __init__(self, Name, LifeDecInterval1, LifeDecInterval2, LifeDecInterval3, LifeDecInterval4, LifeDecInterval5, InterruptInterval, FirstFailureWait, SuccessLife, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LifeDecInterval1 = LifeDecInterval1
		self.LifeDecInterval2 = LifeDecInterval2
		self.LifeDecInterval3 = LifeDecInterval3
		self.LifeDecInterval4 = LifeDecInterval4
		self.LifeDecInterval5 = LifeDecInterval5
		self.InterruptInterval = InterruptInterval
		self.FirstFailureWait = FirstFailureWait
		self.SuccessLife = SuccessLife


class PlayerPullSwordFirstFail:

	def __init__(self, Name, FirstFailureWait, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FirstFailureWait = FirstFailureWait


class PlayerRailMove:

	def __init__(self, Name, DecSpdDist, DecStickValue, ForceTurnDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DecSpdDist = DecSpdDist
		self.DecStickValue = DecStickValue
		self.ForceTurnDist = ForceTurnDist


class PlayerReleaseMasterSowrd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerRemainsBlow:

	def __init__(self, Name, InitSpeed, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitSpeed = InitSpeed
		self.JumpHeight = JumpHeight


class PlayerRequestRecreateDyeArmor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerRideHorse:

	def __init__(self, Name, DecelerateInputThreshold, StopInputFrames, AccelerateInputThreshold, MoveBackInputThreshold, StickXClampAtGear0, TurnStickXInputThreshold, AccelerateInputDelayGear0, AccelerateInputDelayGear1, AccelerateInputDelayGear2, AccelerateInputDelayGear3, AccelerateInputDelayGearTop, AccInputIgnoreFramesGear0, AccInputIgnoreFramesGear1, AccInputIgnoreFramesGear2, AccInputIgnoreFramesGear3, AccInputIgnoreFramesGearTop, ConstraintBreakThreshold, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DecelerateInputThreshold = DecelerateInputThreshold
		self.StopInputFrames = StopInputFrames
		self.AccelerateInputThreshold = AccelerateInputThreshold
		self.MoveBackInputThreshold = MoveBackInputThreshold
		self.StickXClampAtGear0 = StickXClampAtGear0
		self.TurnStickXInputThreshold = TurnStickXInputThreshold
		self.AccelerateInputDelayGear0 = AccelerateInputDelayGear0
		self.AccelerateInputDelayGear1 = AccelerateInputDelayGear1
		self.AccelerateInputDelayGear2 = AccelerateInputDelayGear2
		self.AccelerateInputDelayGear3 = AccelerateInputDelayGear3
		self.AccelerateInputDelayGearTop = AccelerateInputDelayGearTop
		self.AccInputIgnoreFramesGear0 = AccInputIgnoreFramesGear0
		self.AccInputIgnoreFramesGear1 = AccInputIgnoreFramesGear1
		self.AccInputIgnoreFramesGear2 = AccInputIgnoreFramesGear2
		self.AccInputIgnoreFramesGear3 = AccInputIgnoreFramesGear3
		self.AccInputIgnoreFramesGearTop = AccInputIgnoreFramesGearTop
		self.ConstraintBreakThreshold = ConstraintBreakThreshold


class PlayerRideJump:

	def __init__(self, Name, RideOffsetPosY, RideOffsetPosXZ, RideJumpTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RideOffsetPosY = RideOffsetPosY
		self.RideOffsetPosXZ = RideOffsetPosXZ
		self.RideJumpTime = RideJumpTime


class PlayerSelfCamera:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSetVisibleWeapon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSetWakeUpMtx:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerShieldRideMove:

	def __init__(self, Name, EnergyMove, MaxSpeed, JumpSpeedF, ContJumpSpeedF, JumpHeight, ContJumpInterval, ShieldBreakHeight, FinishSpeed, MaxJumpSpeed, LandSEOnInAirFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyMove = EnergyMove
		self.MaxSpeed = MaxSpeed
		self.JumpSpeedF = JumpSpeedF
		self.ContJumpSpeedF = ContJumpSpeedF
		self.JumpHeight = JumpHeight
		self.ContJumpInterval = ContJumpInterval
		self.ShieldBreakHeight = ShieldBreakHeight
		self.FinishSpeed = FinishSpeed
		self.MaxJumpSpeed = MaxJumpSpeed
		self.LandSEOnInAirFrame = LandSEOnInAirFrame


class PlayerShock:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSideStep:

	def __init__(self, Name, SpeedF, FSpeedF, NoDamageTime, MySlowStartFrame, ForceSlowTime, JustAvoidTime, Height, FHeight, UHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedF = SpeedF
		self.FSpeedF = FSpeedF
		self.NoDamageTime = NoDamageTime
		self.MySlowStartFrame = MySlowStartFrame
		self.ForceSlowTime = ForceSlowTime
		self.JustAvoidTime = JustAvoidTime
		self.Height = Height
		self.FHeight = FHeight
		self.UHeight = UHeight


class PlayerSideStepLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSitEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSitStart:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSitWait:

	def __init__(self, Name, AutoRecoverRate, EnergyAutoRecover, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AutoRecoverRate = AutoRecoverRate
		self.EnergyAutoRecover = EnergyAutoRecover


class PlayerSkin:

	def __init__(self, Name, WaitTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime


class PlayerSleep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSlide:

	def __init__(self, Name, UpKeyInvalidTime, FrontSlideMaxSpeedF, BackSlideMaxSpeedF, SlipDownTime, LimitAngleDegStart, MaxSlipSpeed, SlipSpeedAdd, SlipSpeedDec, EffectContTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.UpKeyInvalidTime = UpKeyInvalidTime
		self.FrontSlideMaxSpeedF = FrontSlideMaxSpeedF
		self.BackSlideMaxSpeedF = BackSlideMaxSpeedF
		self.SlipDownTime = SlipDownTime
		self.LimitAngleDegStart = LimitAngleDegStart
		self.MaxSlipSpeed = MaxSlipSpeed
		self.SlipSpeedAdd = SlipSpeedAdd
		self.SlipSpeedDec = SlipSpeedDec
		self.EffectContTime = EffectContTime


class PlayerSlideLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSlippingDown:

	def __init__(self, Name, DamageInterval, DamageVal, ChangeableInterval, ChangeableIntervalInAir, EnableSpeedDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DamageInterval = DamageInterval
		self.DamageVal = DamageVal
		self.ChangeableInterval = ChangeableInterval
		self.ChangeableIntervalInAir = ChangeableIntervalInAir
		self.EnableSpeedDamage = EnableSpeedDamage


class PlayerSpAttack:

	def __init__(self, Name, SwordSearchFrame, SwordSearchAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SwordSearchFrame = SwordSearchFrame
		self.SwordSearchAngle = SwordSearchAngle


class PlayerSquatDamage:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSquatMove:

	def __init__(self, Name, WalkSpeed, DashSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WalkSpeed = WalkSpeed
		self.DashSpeed = DashSpeed


class PlayerSquatWait:

	def __init__(self, Name, WaitTime, AtnTurnDiffAng, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitTime = WaitTime
		self.AtnTurnDiffAng = AtnTurnDiffAng


class PlayerStainCarryWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerStainWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerStepAttack:

	def __init__(self, Name, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight


class PlayerStepGuardJust:

	def __init__(self, Name, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight


class PlayerStepMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerStoleOpen:

	def __init__(self, Name, EnlargeSpd, BoneName, PosOffset, RotOffsetXyz, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnlargeSpd = EnlargeSpd
		self.BoneName = BoneName
		self.PosOffset = PosOffset
		self.RotOffsetXyz = RotOffsetXyz


class PlayerStopInAir:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSubjectWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSuperBlow:

	def __init__(self, Name, InitSpeed, JumpHeight, DecSpeed, NoRagdollTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitSpeed = InitSpeed
		self.JumpHeight = JumpHeight
		self.DecSpeed = DecSpeed
		self.NoRagdollTime = NoRagdollTime


class PlayerSuperJump:

	def __init__(self, Name, JumpHeight, WindScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.WindScale = WindScale


class PlayerSuperJumpCharge:

	def __init__(self, Name, ChargeTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChargeTime = ChargeTime


class PlayerSwimDamage:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSwimDash:

	def __init__(self, Name, EnergyDash, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyDash = EnergyDash


class PlayerSwimJump:

	def __init__(self, Name, JumpHeight, JumpSpeedF, EnergyJump, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.JumpSpeedF = JumpSpeedF
		self.EnergyJump = EnergyJump


class PlayerSwimLand:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerSwimMove:

	def __init__(self, Name, MaxSpeedF, MaxSpeedS, MaxSpeedB, MaxSpeedDash, EnergyMove, EnergyDash, DecSpeedRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeedF = MaxSpeedF
		self.MaxSpeedS = MaxSpeedS
		self.MaxSpeedB = MaxSpeedB
		self.MaxSpeedDash = MaxSpeedDash
		self.EnergyMove = EnergyMove
		self.EnergyDash = EnergyDash
		self.DecSpeedRate = DecSpeedRate


class PlayerSwimSpinAttack:

	def __init__(self, Name, EnergyDash, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyDash = EnergyDash


class PlayerSwimWait:

	def __init__(self, Name, EnergyWait, DecSpeedRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EnergyWait = EnergyWait
		self.DecSpeedRate = DecSpeedRate


class PlayerSwitchHang:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTalk:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTreeClimb:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTurnAndLookToObject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTurnAndLookToObjectNow:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTurnInner:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerTwiceJump:

	def __init__(self, Name, JumpHeight, NoClimbTime, NoClimbTimeTired, NoDispDisableAppTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.NoClimbTime = NoClimbTime
		self.NoClimbTimeTired = NoClimbTimeTired
		self.NoDispDisableAppTime = NoDispDisableAppTime


class PlayerUnbindSheikPad:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerUnequip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerUpdateEquip:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWakeBoard:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWakeBoardEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWakeBoardGoal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWakeBoardReady:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWallDashUp:

	def __init__(self, Name, JumpHeight, MinSpeedF, MaxSpeedF, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.MinSpeedF = MinSpeedF
		self.MaxSpeedF = MaxSpeedF


class PlayerWallJump:

	def __init__(self, Name, JumpHeight, JumpSpeedF, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight
		self.JumpSpeedF = JumpSpeedF


class PlayerWallSlip:

	def __init__(self, Name, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeight = JumpHeight


class PlayerWarp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWarpEffectValueSetter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PlayerWaterDivingJump:

	def __init__(self, Name, DiveSpeedF, DiveHeight, DiveSpeedDec, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DiveSpeedF = DiveSpeedF
		self.DiveHeight = DiveHeight
		self.DiveSpeedDec = DiveSpeedDec


class PlayerWaterFall:

	def __init__(self, Name, SpeedClimb, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpeedClimb = SpeedClimb


class PlayerWaterFallJump:

	def __init__(self, Name, JumpSpeedF, JumpHeight, JumpHeightWaterRemain, JumpHeightWithZora, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpSpeedF = JumpSpeedF
		self.JumpHeight = JumpHeight
		self.JumpHeightWaterRemain = JumpHeightWaterRemain
		self.JumpHeightWithZora = JumpHeightWithZora


class PlayerWeaponThrow:

	def __init__(self, Name, ThrowSpeedY, ThrowSpeedF, SquatThrowSpeedF, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowSpeedY = ThrowSpeedY
		self.ThrowSpeedF = ThrowSpeedF
		self.SquatThrowSpeedF = SquatThrowSpeedF


class PlayerZoraJump:

	def __init__(self, Name, JumpSpeedF, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpSpeedF = JumpSpeedF
		self.JumpHeight = JumpHeight


class PlayerZoraRide:

	def __init__(self, Name, LowerAngleWaitTime, AimAngleAddApplyAngle, AimAngleAdd, AimAngleAddApplySpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LowerAngleWaitTime = LowerAngleWaitTime
		self.AimAngleAddApplyAngle = AimAngleAddApplyAngle
		self.AimAngleAdd = AimAngleAdd
		self.AimAngleAddApplySpeed = AimAngleAddApplySpeed


class PowerupRune:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PreAttack:

	def __init__(self, Name, TurnSpd, ASName, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnSpd = TurnSpd
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio


class PreJumpAttack:

	def __init__(self, Name, TurnSpd, ASName, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnSpd = TurnSpd
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio


class PredictVacuumShoot:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, PartsKey, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, RotSpd, IsReuseBullet, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.PartsKey = PartsKey
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.RotSpd = RotSpd
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class PreductVacuumBurstShoot:

	def __init__(self, Name, PartsKey2, PartsKey3, BulletOffset, ASName, PosReduceRatio, AngReduceRatio, PartsKey, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, RotSpd, IsReuseBullet, SeqBank, TargetBone, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartsKey2 = PartsKey2
		self.PartsKey3 = PartsKey3
		self.BulletOffset = BulletOffset
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.PartsKey = PartsKey
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.RotSpd = RotSpd
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone


class PriestBossAimBeam:

	def __init__(self, Name, TargetOffset, TargetOffsetY, FluctuationRange, FluctuationTime, FluctuationSpan, NodeName, NodeOffset, AimMaxLength, AimLockFrame, AimOffToTarget, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetOffset = TargetOffset
		self.TargetOffsetY = TargetOffsetY
		self.FluctuationRange = FluctuationRange
		self.FluctuationTime = FluctuationTime
		self.FluctuationSpan = FluctuationSpan
		self.NodeName = NodeName
		self.NodeOffset = NodeOffset
		self.AimMaxLength = AimMaxLength
		self.AimLockFrame = AimLockFrame
		self.AimOffToTarget = AimOffToTarget


class PriestBossAimBeamWithAS:

	def __init__(self, Name, ASName, TargetOffset, TargetOffsetY, FluctuationRange, FluctuationTime, FluctuationSpan, NodeName, NodeOffset, AimMaxLength, AimLockFrame, AimOffToTarget, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TargetOffset = TargetOffset
		self.TargetOffsetY = TargetOffsetY
		self.FluctuationRange = FluctuationRange
		self.FluctuationTime = FluctuationTime
		self.FluctuationSpan = FluctuationSpan
		self.NodeName = NodeName
		self.NodeOffset = NodeOffset
		self.AimMaxLength = AimMaxLength
		self.AimLockFrame = AimLockFrame
		self.AimOffToTarget = AimOffToTarget


class PriestBossBeamMove:

	def __init__(self, Name, AtMinDamage, ShieldDamage, ReflectDeccel, ContactWaitFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtMinDamage = AtMinDamage
		self.ShieldDamage = ShieldDamage
		self.ReflectDeccel = ReflectDeccel
		self.ContactWaitFrame = ContactWaitFrame


class PriestBossBlownOff:

	def __init__(self, Name, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class PriestBossClonesSpawn:

	def __init__(self, Name, ASNameForAITree, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASNameForAITree = ASNameForAITree


class PriestBossClonesSpawnForDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PriestBossFastWarpMove:

	def __init__(self, Name, AfterImage0AppearFrame, AfterImage1AppearFrame, AppearFrame, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AfterImage0AppearFrame = AfterImage0AppearFrame
		self.AfterImage1AppearFrame = AfterImage1AppearFrame
		self.AppearFrame = AppearFrame
		self.ASName = ASName


class PriestBossMove:

	def __init__(self, Name, ASName, Speed, AccRatio, InitRotSpd, AccRotSpd, MaxRotSpd, FinRadius, FinRotate, WeaponIdx, FollowGround, WallHitLimitTime, FrontCliffDistance, FrontCliffAngle, MoveAngCliffLimitTime, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, NotMoveLimitTime, NotMoveDistanceThreshold, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.AccRatio = AccRatio
		self.InitRotSpd = InitRotSpd
		self.AccRotSpd = AccRotSpd
		self.MaxRotSpd = MaxRotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.FrontCliffDistance = FrontCliffDistance
		self.FrontCliffAngle = FrontCliffAngle
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio
		self.NotMoveLimitTime = NotMoveLimitTime
		self.NotMoveDistanceThreshold = NotMoveDistanceThreshold


class PriestBossShadowCloneVanish:

	def __init__(self, Name, DelayFrames, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DelayFrames = DelayFrames


class PriestBossSideMove:

	def __init__(self, Name, ASName, IsIgnoreSame, RotDir, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.RotDir = RotDir
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class PriestBossSlowWarpMove:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class Puddle:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class PullOut:

	def __init__(self, Name, AnimGrabPos, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AnimGrabPos = AnimGrabPos
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class PulleyChainASControl:

	def __init__(self, Name, ASName, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class PunchAttack:

	def __init__(self, Name, ASName, AtkBodyName1, AtkBodyName2, AtkBodyName3, AttackIntensity, IsGuardPierce, IsForceGuardBreak, IsIniviciblePierce, IsImpulseLarge, IsHeavy, IsHammer, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AtkBodyName1 = AtkBodyName1
		self.AtkBodyName2 = AtkBodyName2
		self.AtkBodyName3 = AtkBodyName3
		self.AttackIntensity = AttackIntensity
		self.IsGuardPierce = IsGuardPierce
		self.IsForceGuardBreak = IsForceGuardBreak
		self.IsIniviciblePierce = IsIniviciblePierce
		self.IsImpulseLarge = IsImpulseLarge
		self.IsHeavy = IsHeavy
		self.IsHammer = IsHammer
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class PutFromParent:

	def __init__(self, Name, Timer, HoldOffXLinkKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Timer = Timer
		self.HoldOffXLinkKey = HoldOffXLinkKey


class RagdollFreeze:

	def __init__(self, Name, DownFrontCtrlOffset, DownBackCtrlOffset, IsChangeInAir, TransBoneKey, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.IsChangeInAir = IsChangeInAir
		self.TransBoneKey = TransBoneKey
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class RailMove:

	def __init__(self, Name, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed


class RandomJump:

	def __init__(self, Name, AngleLimit, HeightMin, HeightMaxOffset, DistanceMin, DistanceMaxOffset, IsReturnByHitWall, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngleLimit = AngleLimit
		self.HeightMin = HeightMin
		self.HeightMaxOffset = HeightMaxOffset
		self.DistanceMin = DistanceMin
		self.DistanceMaxOffset = DistanceMaxOffset
		self.IsReturnByHitWall = IsReturnByHitWall
		self.ASName = ASName


class Rebound:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ReboundHit:

	def __init__(self, Name, Speed, GravityRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.GravityRate = GravityRate


class ReceiveTerror:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RecoverMasterSword:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ReflectThrown:

	def __init__(self, Name, ReactionLevel, FinishWaterDepth, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactionLevel = ReactionLevel
		self.FinishWaterDepth = FinishWaterDepth


class RegistedActorBroadCastMessage:

	def __init__(self, Name, TeachSelfRegistedActor, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TeachSelfRegistedActor = TeachSelfRegistedActor


class RegistedActorDeadCheck:

	def __init__(self, Name, TeachSelfRegistedActor, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TeachSelfRegistedActor = TeachSelfRegistedActor


class ReloadArrow:

	def __init__(self, Name, RotSpeed, StopSpeedRatio, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.WeaponIdx = WeaponIdx


class RemainElectricCannonBeamFire:

	def __init__(self, Name, AtkDamage, MinDamage, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkDamage = AtkDamage
		self.MinDamage = MinDamage


class RemainElectricCannonBeamHerald:

	def __init__(self, Name, HeraldTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HeraldTime = HeraldTime


class RemainElectricCannonCharge:

	def __init__(self, Name, ChargeTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChargeTime = ChargeTime


class RemainsElectricWeakPointWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RemainsFireDroneRailMove:

	def __init__(self, Name, NearDistance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NearDistance = NearDistance


class RemainsFireDroneRailStop:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RemainsFireTailAttack:

	def __init__(self, Name, ASKeyName, IsIgnoreSame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.IsIgnoreSame = IsIgnoreSame


class RemainsFireYunBoFlagControl:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RemainsWaterBulletExplode:

	def __init__(self, Name, MaxDamage, MinDamage, SizeUpTime, ExplodeTime, UseDefaultEffect, IsDelete, IsDamageGuarantee, AttackIntensity, IsVanish, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxDamage = MaxDamage
		self.MinDamage = MinDamage
		self.SizeUpTime = SizeUpTime
		self.ExplodeTime = ExplodeTime
		self.UseDefaultEffect = UseDefaultEffect
		self.IsDelete = IsDelete
		self.IsDamageGuarantee = IsDamageGuarantee
		self.AttackIntensity = AttackIntensity
		self.IsVanish = IsVanish


class RemainsWaterBulletRevive:

	def __init__(self, Name, XLinkKey, MaxChaseAngle, MaxSpeed, ChaseRate, MaxRotSpd, MinRotSpd, SignASName, SignASFrame, EndTimer, IgnroeWater, IgnoreGravity, UseParentRevDirRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.XLinkKey = XLinkKey
		self.MaxChaseAngle = MaxChaseAngle
		self.MaxSpeed = MaxSpeed
		self.ChaseRate = ChaseRate
		self.MaxRotSpd = MaxRotSpd
		self.MinRotSpd = MinRotSpd
		self.SignASName = SignASName
		self.SignASFrame = SignASFrame
		self.EndTimer = EndTimer
		self.IgnroeWater = IgnroeWater
		self.IgnoreGravity = IgnoreGravity
		self.UseParentRevDirRot = UseParentRevDirRot


class RemainsWaterBulletShooter:

	def __init__(self, Name, IgniteRotate, UseRandRot, BulletType, ReloadCounter, BaseShootParam, OffsetYParam, OffsetAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteRotate = IgniteRotate
		self.UseRandRot = UseRandRot
		self.BulletType = BulletType
		self.ReloadCounter = ReloadCounter
		self.BaseShootParam = BaseShootParam
		self.OffsetYParam = OffsetYParam
		self.OffsetAngle = OffsetAngle


class RemainsWaterBulletWait:

	def __init__(self, Name, MaxChaseAngle, MaxSpeed, ChaseRate, MaxRotSpd, MinRotSpd, SignASName, SignASFrame, EndTimer, IgnroeWater, IgnoreGravity, UseParentRevDirRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxChaseAngle = MaxChaseAngle
		self.MaxSpeed = MaxSpeed
		self.ChaseRate = ChaseRate
		self.MaxRotSpd = MaxRotSpd
		self.MinRotSpd = MinRotSpd
		self.SignASName = SignASName
		self.SignASFrame = SignASFrame
		self.EndTimer = EndTimer
		self.IgnroeWater = IgnroeWater
		self.IgnoreGravity = IgnoreGravity
		self.UseParentRevDirRot = UseParentRevDirRot


class RemainsWaterChaseBulletFall:

	def __init__(self, Name, EndTimer, InWaterDepth, SetVelocity, SetVelocityFromWeapon, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndTimer = EndTimer
		self.InWaterDepth = InWaterDepth
		self.SetVelocity = SetVelocity
		self.SetVelocityFromWeapon = SetVelocityFromWeapon


class RemainsWaterChaseBulletMove:

	def __init__(self, Name, BaseTargetOffset, BaseTargetRandOffset, BaseChaseSpd, MaxChaseSpd, ChaseSpdRate, ChaseAngleRate, DepthOffset, MaxPredictFrame, MinPredictFrame, StartPredictDist, EndPredictDist, WeakChaseTimer, MaxRotSpd, MinRotSpd, SignASName, SignASFrame, EndTimer, IgnroeWater, IgnoreGravity, UseParentRevDirRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.BaseTargetOffset = BaseTargetOffset
		self.BaseTargetRandOffset = BaseTargetRandOffset
		self.BaseChaseSpd = BaseChaseSpd
		self.MaxChaseSpd = MaxChaseSpd
		self.ChaseSpdRate = ChaseSpdRate
		self.ChaseAngleRate = ChaseAngleRate
		self.DepthOffset = DepthOffset
		self.MaxPredictFrame = MaxPredictFrame
		self.MinPredictFrame = MinPredictFrame
		self.StartPredictDist = StartPredictDist
		self.EndPredictDist = EndPredictDist
		self.WeakChaseTimer = WeakChaseTimer
		self.MaxRotSpd = MaxRotSpd
		self.MinRotSpd = MinRotSpd
		self.SignASName = SignASName
		self.SignASFrame = SignASFrame
		self.EndTimer = EndTimer
		self.IgnroeWater = IgnroeWater
		self.IgnoreGravity = IgnoreGravity
		self.UseParentRevDirRot = UseParentRevDirRot


class RemainsWaterExplodeBulletMove:

	def __init__(self, Name, MaxSpeed, CloseRadius, ChaseAngleMulRate, FarRadius, ChaseRotSpdRate, ChaseSpdRate, MaxRotSpd, MinRotSpd, SignASName, SignASFrame, EndTimer, IgnroeWater, IgnoreGravity, UseParentRevDirRot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.CloseRadius = CloseRadius
		self.ChaseAngleMulRate = ChaseAngleMulRate
		self.FarRadius = FarRadius
		self.ChaseRotSpdRate = ChaseRotSpdRate
		self.ChaseSpdRate = ChaseSpdRate
		self.MaxRotSpd = MaxRotSpd
		self.MinRotSpd = MinRotSpd
		self.SignASName = SignASName
		self.SignASFrame = SignASFrame
		self.EndTimer = EndTimer
		self.IgnroeWater = IgnroeWater
		self.IgnoreGravity = IgnoreGravity
		self.UseParentRevDirRot = UseParentRevDirRot


class RemainsWindBarrier:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RemoveRigidBody:

	def __init__(self, Name, ChangeLayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChangeLayer = ChangeLayer


class RemoveSensor:

	def __init__(self, Name, AddSensorOnLeave, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AddSensorOnLeave = AddSensorOnLeave


class ReqCreateManufactedEquipItem:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RequestCreateHCIModel:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RequestEvent:

	def __init__(self, Name, EventName, EntryPointName, IsSelfEvent, IsAddEntrySelfName, IsLoadEvent, IsPauseOtherActors, IsWaitRun, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EventName = EventName
		self.EntryPointName = EntryPointName
		self.IsSelfEvent = IsSelfEvent
		self.IsAddEntrySelfName = IsAddEntrySelfName
		self.IsLoadEvent = IsLoadEvent
		self.IsPauseOtherActors = IsPauseOtherActors
		self.IsWaitRun = IsWaitRun


class RequestEventFromMapUnit:

	def __init__(self, Name, ASKey, IsWaitStartEvent, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKey = ASKey
		self.IsWaitStartEvent = IsWaitStartEvent


class RequestOpenPopUpHelp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ReserveParashawlStart:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ResetChemicalStateNeutral:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ResetGimmick:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ResetMasterSwordForceState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ResetPlayerPullSwordStartLife:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ResetRemainsMapState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RestartStageFromGameOver:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RestorePlayerPosAndRotate:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RestorePouchForQuest:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ReuseActorDelete:

	def __init__(self, Name, IsCheckCreateParent, IsCheckBulletAttacker, IsCheckBulletHolder, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckCreateParent = IsCheckCreateParent
		self.IsCheckBulletAttacker = IsCheckBulletAttacker
		self.IsCheckBulletHolder = IsCheckBulletHolder


class ReviveEnemies:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RideHorse:

	def __init__(self, Name, JumpHeightOffset, MaxSpeed, FarRotSpeed, NearRotSpeed, RideRotSpeed, LoopASInterpolateTime, PredictedRidePosOffset, PreRideSklRootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpHeightOffset = JumpHeightOffset
		self.MaxSpeed = MaxSpeed
		self.FarRotSpeed = FarRotSpeed
		self.NearRotSpeed = NearRotSpeed
		self.RideRotSpeed = RideRotSpeed
		self.LoopASInterpolateTime = LoopASInterpolateTime
		self.PredictedRidePosOffset = PredictedRidePosOffset
		self.PreRideSklRootOffset = PreRideSklRootOffset


class RideHorseAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RideHorseForEventAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class RisingAirOneTime:

	def __init__(self, Name, LostCounter, WindSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LostCounter = LostCounter
		self.WindSpeed = WindSpeed


class RodMagicPhysBall:

	def __init__(self, Name, CreateActorName, ChemicalType, BgCheckHeight, DeleteTime, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CreateActorName = CreateActorName
		self.ChemicalType = ChemicalType
		self.BgCheckHeight = BgCheckHeight
		self.DeleteTime = DeleteTime
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class RodMagicPhysBallDivision:

	def __init__(self, Name, DivNum, DivDist, DivAngle, ChildName, CreateActorName, ChemicalType, BgCheckHeight, DeleteTime, IsUseMyRange, AttackType, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DivNum = DivNum
		self.DivDist = DivDist
		self.DivAngle = DivAngle
		self.ChildName = ChildName
		self.CreateActorName = CreateActorName
		self.ChemicalType = ChemicalType
		self.BgCheckHeight = BgCheckHeight
		self.DeleteTime = DeleteTime
		self.IsUseMyRange = IsUseMyRange
		self.AttackType = AttackType
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class RopeNormal:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Rotate:

	def __init__(self, Name, IsReturn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsReturn = IsReturn


class RotatedWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Run:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class SSMagneStickAcceptorAccept:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SSMagneStickAcceptorReject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SandwichDetectionAreaTag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SandwichDetectionAreaTagSimple:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SandwormASPlay:

	def __init__(self, Name, ASName, TargetSandOffset, SandOffsetSpeed, WaitASFinish, WaitSandOffset, IsChangeable, IsUseAtEvent, ChangeOffsetDelay, TransBoneName, IsUseTossAt, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TargetSandOffset = TargetSandOffset
		self.SandOffsetSpeed = SandOffsetSpeed
		self.WaitASFinish = WaitASFinish
		self.WaitSandOffset = WaitSandOffset
		self.IsChangeable = IsChangeable
		self.IsUseAtEvent = IsUseAtEvent
		self.ChangeOffsetDelay = ChangeOffsetDelay
		self.TransBoneName = TransBoneName
		self.IsUseTossAt = IsUseTossAt
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SandwormBlownOff:

	def __init__(self, Name, SandOffsetSpeed, TargetSandOffset, Timer, ASName, LimitDamage, DamageASName, SmallDamageASName, DamageRigidName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SandOffsetSpeed = SandOffsetSpeed
		self.TargetSandOffset = TargetSandOffset
		self.Timer = Timer
		self.ASName = ASName
		self.LimitDamage = LimitDamage
		self.DamageASName = DamageASName
		self.SmallDamageASName = SmallDamageASName
		self.DamageRigidName = DamageRigidName


class SandwormDamageJumpReaction:

	def __init__(self, Name, ASName, TargetSandOffset, SandOffsetSpeed, JumpHeight, WaitASFinish, WaitSandOffset, ReduceGravityRate, ReduceRotRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.TargetSandOffset = TargetSandOffset
		self.SandOffsetSpeed = SandOffsetSpeed
		self.JumpHeight = JumpHeight
		self.WaitASFinish = WaitASFinish
		self.WaitSandOffset = WaitSandOffset
		self.ReduceGravityRate = ReduceGravityRate
		self.ReduceRotRate = ReduceRotRate


class SandwormJumpTackle:

	def __init__(self, Name, AtkColName, PosReduceRate, GravityScale, MaxSpeed, MinSpeed, JumpHeight, JumpHeightMaxOffset, IsFinishedAtPreLandFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtkColName = AtkColName
		self.PosReduceRate = PosReduceRate
		self.GravityScale = GravityScale
		self.MaxSpeed = MaxSpeed
		self.MinSpeed = MinSpeed
		self.JumpHeight = JumpHeight
		self.JumpHeightMaxOffset = JumpHeightMaxOffset
		self.IsFinishedAtPreLandFrame = IsFinishedAtPreLandFrame


class SandwormMove:

	def __init__(self, Name, TargetSandOffset, SandOffsetSpeed, IsCheckAnmSeqCancel, VibrateStopCheck, VibrateCheckFrame, VibrateMemoryStep, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetSandOffset = TargetSandOffset
		self.SandOffsetSpeed = SandOffsetSpeed
		self.IsCheckAnmSeqCancel = IsCheckAnmSeqCancel
		self.VibrateStopCheck = VibrateStopCheck
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateMemoryStep = VibrateMemoryStep
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class SandwormNavMove:

	def __init__(self, Name, TargetSandOffset, SandOffsetSpeed, VibrateStopCheck, VibrateCheckFrame, VibrateMemoryStep, ASName, IsIgnoreSameAS, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, AccRatio, IsCheckCliff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetSandOffset = TargetSandOffset
		self.SandOffsetSpeed = SandOffsetSpeed
		self.VibrateStopCheck = VibrateStopCheck
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateMemoryStep = VibrateMemoryStep
		self.ASName = ASName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.AccRatio = AccRatio
		self.IsCheckCliff = IsCheckCliff


class SandwormTackleMove:

	def __init__(self, Name, TargetSandOffset, SandOffsetSpeed, EatNode, EatRadius, EatOffset, AtkSensorName, Speed, RotSpd, FailAngle, BaseRotRatio, FinRadius, WeaponIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetSandOffset = TargetSandOffset
		self.SandOffsetSpeed = SandOffsetSpeed
		self.EatNode = EatNode
		self.EatRadius = EatRadius
		self.EatOffset = EatOffset
		self.AtkSensorName = AtkSensorName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FailAngle = FailAngle
		self.BaseRotRatio = BaseRotRatio
		self.FinRadius = FinRadius
		self.WeaponIdx = WeaponIdx


class SceneBgmCtrlAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundCtrlAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundKillDuckingAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundNotifyTalkAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundSetEndProcAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundSetStartProcAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundStartDuckingAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SceneSoundStopDuckingAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ScrapEquip:

	def __init__(self, Name, WeaponIdx, DropSpd, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.DropSpd = DropSpd
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class Search:

	def __init__(self, Name, NoChangeTime, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NoChangeTime = NoChangeTime
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SellPictureBookUIDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SendMessage4YunBoCannon:

	def __init__(self, Name, MsgType, SendTiming, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MsgType = MsgType
		self.SendTiming = SendTiming


class SendMessageBroadCast:

	def __init__(self, Name, MsgType, SendTiming, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MsgType = MsgType
		self.SendTiming = SendTiming


class SendPlayerNoticeMessage:

	def __init__(self, Name, TargetActorName, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TargetActorName = TargetActorName
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SendSignalAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SendSignalForSignalFlowAct:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SendTargetActorRequestShareAwn:

	def __init__(self, Name, SendTiming, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SendTiming = SendTiming


class SeqPunchByASEvent:

	def __init__(self, Name, ASName, AttackIntensity, IsHammer, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AttackIntensity = AttackIntensity
		self.IsHammer = IsHammer
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SetActorNameToGameDataString:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetBloodyMoonEnv:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetChallengeIcon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetChemicalWeaponPower:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetComebackPosition:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetCookItemInDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetCurrentDungeonClearFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetDispHeartGauge:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetDispStaminaGauge:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetEnableRayHit:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetEnableWaterHit:

	def __init__(self, Name, WaterHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaterHit = WaterHit


class SetEnterDungeonFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetExtraEnergyOfPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetExtraLifeOfPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetFrameASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class SetGetFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetGetFlagByActorName:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetGravityFactor:

	def __init__(self, Name, Value, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Value = Value


class SetHorseFamiliarityPassedFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetImpulseDamageMin:

	def __init__(self, Name, ReactionLevel, IsGuardable, IsGuarantee, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactionLevel = ReactionLevel
		self.IsGuardable = IsGuardable
		self.IsGuarantee = IsGuarantee


class SetInstEventFlag:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetInstantTemperture:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetLinkTagBasic:

	def __init__(self, Name, IsOn, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOn = IsOn


class SetMaterialVisible:

	def __init__(self, Name, IsVisible, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsVisible = IsVisible


class SetOpenState:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetOwnedHorseAS:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetPlayerDrawingSword:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetPlayerStateToUnequipAndWait:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetQuestStepAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetRequestAttention:

	def __init__(self, Name, IsOn, IsAll, AttName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOn = IsOn
		self.IsAll = IsAll
		self.AttName = AttName


class SetResetPos:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetRetryDataAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetTargetFrameMtx:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetFrame, ResetTransBoneOnLeave, IsHomeMtx, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetFrame = TargetFrame
		self.ResetTransBoneOnLeave = ResetTransBoneOnLeave
		self.IsHomeMtx = IsHomeMtx
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class SetTgIgnoreObstacle:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetTraverseDist:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetTreasure:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetTreasureBoxOpenAndClose:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetWanderPathIndex:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetWorldRotOffsetFromTransBone:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SetupGetDemoModeNumUi:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShelterFromRain:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShiekSensorPlusDownloadDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Shock:

	def __init__(self, Name, HitImpactForce, VelReduce, KnockBackTime, WeaponIdx, WeaponDropSpeedXZ, WeaponDropSpeedY, ASName, ASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HitImpactForce = HitImpactForce
		self.VelReduce = VelReduce
		self.KnockBackTime = KnockBackTime
		self.WeaponIdx = WeaponIdx
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.ASName = ASName
		self.ASSlot = ASSlot


class ShockDynamicWeapon:

	def __init__(self, Name, HitImpactForce, VelReduce, KnockBackTime, WeaponIdx, WeaponDropSpeedXZ, WeaponDropSpeedY, ASName, ASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HitImpactForce = HitImpactForce
		self.VelReduce = VelReduce
		self.KnockBackTime = KnockBackTime
		self.WeaponIdx = WeaponIdx
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.ASName = ASName
		self.ASSlot = ASSlot


class ShockWave:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShootArrow:

	def __init__(self, Name, StopSpeedRatio, StopRotSpeedRatio, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.ASName = ASName


class ShootingStarBrightTower:

	def __init__(self, Name, DisappearDistance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DisappearDistance = DisappearDistance


class ShootingStartFlying:

	def __init__(self, Name, InitialVelocityMax, InitialVelocityMin, InitialAngleRange, LookSuccessRate, MaxWaterDepth, Gravity, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitialVelocityMax = InitialVelocityMax
		self.InitialVelocityMin = InitialVelocityMin
		self.InitialAngleRange = InitialAngleRange
		self.LookSuccessRate = LookSuccessRate
		self.MaxWaterDepth = MaxWaterDepth
		self.Gravity = Gravity


class ShopFixedItemNum:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShowMemoryPhoto:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShowPhoto:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ShutterClose:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class ShutterCloseWait:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class ShutterOpen:

	def __init__(self, Name, ASName, OnLink, IsPreOpen, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.OnLink = OnLink
		self.IsPreOpen = IsPreOpen


class ShutterOpenWait:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class SideStep:

	def __init__(self, Name, RotSpeedRatio, StopSpeedRatio, StopRotSpeedRatio, Gravity, JumpHeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeedRatio = RotSpeedRatio
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.Gravity = Gravity
		self.JumpHeight = JumpHeight


class SideStepWait:

	def __init__(self, Name, FirstStepDist, SecondStepDist, ThirdStepDist, FourthStepDist, Gravity, FirstStepHeight, SecondStepHeight, ThirdStepHeight, FourthStepHeight, StopSpeedRatio, StopRotSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FirstStepDist = FirstStepDist
		self.SecondStepDist = SecondStepDist
		self.ThirdStepDist = ThirdStepDist
		self.FourthStepDist = FourthStepDist
		self.Gravity = Gravity
		self.FirstStepHeight = FirstStepHeight
		self.SecondStepHeight = SecondStepHeight
		self.ThirdStepHeight = ThirdStepHeight
		self.FourthStepHeight = FourthStepHeight
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio


class SideWalk:

	def __init__(self, Name, ASKeyName, IsIgnoreSameAS, LeftMove, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASKeyName = ASKeyName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.LeftMove = LeftMove
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class SilentKilled:

	def __init__(self, Name, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class SimpleGrabWithAS:

	def __init__(self, Name, ASName, AttOffset, CheckRadius, GrabIdx, CheckSpeed, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AttOffset = AttOffset
		self.CheckRadius = CheckRadius
		self.GrabIdx = GrabIdx
		self.CheckSpeed = CheckSpeed
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SimpleLineBeam:

	def __init__(self, Name, IsGuarantee, Type, IsGuardPierces, IsSetAtIgnoreObstacle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsGuarantee = IsGuarantee
		self.Type = Type
		self.IsGuardPierces = IsGuardPierces
		self.IsSetAtIgnoreObstacle = IsSetAtIgnoreObstacle


class SimpleOpenMessageDialogAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SimpleUniqueTalk:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SiteBossAvoid:

	def __init__(self, Name, AvoidEndTime, AvoidMoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AvoidEndTime = AvoidEndTime
		self.AvoidMoveSpeed = AvoidMoveSpeed


class SiteBossBowBlowOff:

	def __init__(self, Name, ForceRecoverDist, ForceRecoverOffset, AddForceRecoverTime, IsRemoveCharacterController, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceRecoverDist = ForceRecoverDist
		self.ForceRecoverOffset = ForceRecoverOffset
		self.AddForceRecoverTime = AddForceRecoverTime
		self.IsRemoveCharacterController = IsRemoveCharacterController
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class SiteBossBowChildDeviceBreak:

	def __init__(self, Name, ReactionTime, IsDelete, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactionTime = ReactionTime
		self.IsDelete = IsDelete


class SiteBossBowHoldTurn:

	def __init__(self, Name, ASName, SpineControlOffsetAngleLR, SpineControlOffsetAngleUD, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.SpineControlOffsetAngleLR = SpineControlOffsetAngleLR
		self.SpineControlOffsetAngleUD = SpineControlOffsetAngleUD
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class SiteBossBowMoveForArrowRain:

	def __init__(self, Name, ASName, MoveTarget, FirstMoveSpeed, FirstAccelFrame, SecondMoveSpeed, SecondAccelFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.MoveTarget = MoveTarget
		self.FirstMoveSpeed = FirstMoveSpeed
		self.FirstAccelFrame = FirstAccelFrame
		self.SecondMoveSpeed = SecondMoveSpeed
		self.SecondAccelFrame = SecondAccelFrame


class SiteBossChemicalPlus:

	def __init__(self, Name, IsDeleteAllChildDevice, ChemicalLoopASName, IsSetCanGuardArrowFlag, ChmicalPlusASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsDeleteAllChildDevice = IsDeleteAllChildDevice
		self.ChemicalLoopASName = ChemicalLoopASName
		self.IsSetCanGuardArrowFlag = IsSetCanGuardArrowFlag
		self.ChmicalPlusASName = ChmicalPlusASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SiteBossCreateChildDevice:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SiteBossCreateIceSplinter:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class SiteBossDie:

	def __init__(self, Name, WarpWaitTime, IsUseYAxisSignal, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WarpWaitTime = WarpWaitTime
		self.IsUseYAxisSignal = IsUseYAxisSignal


class SiteBossFlyWaitTurnToTarget:

	def __init__(self, Name, TurnStartDiffAng, TurnASName, TurnRate, Amplitude, Time, MoveRate, EndTime, EndTimeRandRange, BaseYOffset, DamageCounter, WaitAS, IsChemicalOff, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnStartDiffAng = TurnStartDiffAng
		self.TurnASName = TurnASName
		self.TurnRate = TurnRate
		self.Amplitude = Amplitude
		self.Time = Time
		self.MoveRate = MoveRate
		self.EndTime = EndTime
		self.EndTimeRandRange = EndTimeRandRange
		self.BaseYOffset = BaseYOffset
		self.DamageCounter = DamageCounter
		self.WaitAS = WaitAS
		self.IsChemicalOff = IsChemicalOff


class SiteBossGetUpLinear:

	def __init__(self, Name, ForceRecoverOffset, ForceRecoverDist, IsRestoreRigidBody, RotCenterPos, ASName, RootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceRecoverOffset = ForceRecoverOffset
		self.ForceRecoverDist = ForceRecoverDist
		self.IsRestoreRigidBody = IsRestoreRigidBody
		self.RotCenterPos = RotCenterPos
		self.ASName = ASName
		self.RootOffset = RootOffset


class SiteBossLswordAtkWithChemical:

	def __init__(self, Name, EmitActorName, EmitNum, EmitOffsetFromParent, EmitIntervalDist, EmitIntervalRotate, EmitScale, EmitMaxScale, ScaleTime, EmitInterval, EmitStartFrame, EmitAngleFromParent, EmitActorSpeed, EmitActorSpeedRotate, EmitAttackDamage, EmitActorMinDamage, EmitPartsName, CallSEKeyAtAtOn, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, NearDist, NearMoveSpeed, FarDist, FarMoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EmitActorName = EmitActorName
		self.EmitNum = EmitNum
		self.EmitOffsetFromParent = EmitOffsetFromParent
		self.EmitIntervalDist = EmitIntervalDist
		self.EmitIntervalRotate = EmitIntervalRotate
		self.EmitScale = EmitScale
		self.EmitMaxScale = EmitMaxScale
		self.ScaleTime = ScaleTime
		self.EmitInterval = EmitInterval
		self.EmitStartFrame = EmitStartFrame
		self.EmitAngleFromParent = EmitAngleFromParent
		self.EmitActorSpeed = EmitActorSpeed
		self.EmitActorSpeedRotate = EmitActorSpeedRotate
		self.EmitAttackDamage = EmitAttackDamage
		self.EmitActorMinDamage = EmitActorMinDamage
		self.EmitPartsName = EmitPartsName
		self.CallSEKeyAtAtOn = CallSEKeyAtAtOn
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.NearDist = NearDist
		self.NearMoveSpeed = NearMoveSpeed
		self.FarDist = FarDist
		self.FarMoveSpeed = FarMoveSpeed


class SiteBossLswordFireBall:

	def __init__(self, Name, AppearInterval, BallAppearOffset, WaitASName, FireBallScale, IsShowChildDevice, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AppearInterval = AppearInterval
		self.BallAppearOffset = BallAppearOffset
		self.WaitASName = WaitASName
		self.FireBallScale = FireBallScale
		self.IsShowChildDevice = IsShowChildDevice


class SiteBossLswordFirstCreateFBall:

	def __init__(self, Name, ThrowActorName, AtMinDamage, AttackPower, FireBallScale, BindPosOffset, ASName, CreateNum, AddAttackPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowActorName = ThrowActorName
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.FireBallScale = FireBallScale
		self.BindPosOffset = BindPosOffset
		self.ASName = ASName
		self.CreateNum = CreateNum
		self.AddAttackPower = AddAttackPower


class SiteBossLswordPostWarp:

	def __init__(self, Name, CancelSleepPartsName, WaitTime, NoCryAnime, IsTurnToTarget, ASName, IsCheckDistFromTarget, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CancelSleepPartsName = CancelSleepPartsName
		self.WaitTime = WaitTime
		self.NoCryAnime = NoCryAnime
		self.IsTurnToTarget = IsTurnToTarget
		self.ASName = ASName
		self.IsCheckDistFromTarget = IsCheckDistFromTarget


class SiteBossLswordPreWarp:

	def __init__(self, Name, SleepPartsName, PreWarpWaitTime, IsDeleteEffect, ASName, PosReduce, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SleepPartsName = SleepPartsName
		self.PreWarpWaitTime = PreWarpWaitTime
		self.IsDeleteEffect = IsDeleteEffect
		self.ASName = ASName
		self.PosReduce = PosReduce


class SiteBossLswordThrowFireBall:

	def __init__(self, Name, ThrowASName, InitVelocity, FireBallAng, BindNodeName, IsThrowAll, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowASName = ThrowASName
		self.InitVelocity = InitVelocity
		self.FireBallAng = FireBallAng
		self.BindNodeName = BindNodeName
		self.IsThrowAll = IsThrowAll


class SiteBossLswordTornadoAttack:

	def __init__(self, Name, EndTime, VacuumAcc, VacuumMaxSpeed, VacuumAngle, VacuumBaseWeight, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EndTime = EndTime
		self.VacuumAcc = VacuumAcc
		self.VacuumMaxSpeed = VacuumMaxSpeed
		self.VacuumAngle = VacuumAngle
		self.VacuumBaseWeight = VacuumBaseWeight


class SiteBossLswordTornadoEnd:

	def __init__(self, Name, IsUseTornadoAttack, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsUseTornadoAttack = IsUseTornadoAttack


class SiteBossLswordWhirlSlash:

	def __init__(self, Name, EmitChangeDist, CircleEmitOffset, EmitActorName, EmitNum, EmitOffsetFromParent, EmitIntervalDist, EmitIntervalRotate, EmitScale, EmitMaxScale, ScaleTime, EmitInterval, EmitStartFrame, EmitAngleFromParent, EmitActorSpeed, EmitActorSpeedRotate, EmitAttackDamage, EmitActorMinDamage, EmitPartsName, CallSEKeyAtAtOn, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, NearDist, NearMoveSpeed, FarDist, FarMoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.EmitChangeDist = EmitChangeDist
		self.CircleEmitOffset = CircleEmitOffset
		self.EmitActorName = EmitActorName
		self.EmitNum = EmitNum
		self.EmitOffsetFromParent = EmitOffsetFromParent
		self.EmitIntervalDist = EmitIntervalDist
		self.EmitIntervalRotate = EmitIntervalRotate
		self.EmitScale = EmitScale
		self.EmitMaxScale = EmitMaxScale
		self.ScaleTime = ScaleTime
		self.EmitInterval = EmitInterval
		self.EmitStartFrame = EmitStartFrame
		self.EmitAngleFromParent = EmitAngleFromParent
		self.EmitActorSpeed = EmitActorSpeed
		self.EmitActorSpeedRotate = EmitActorSpeedRotate
		self.EmitAttackDamage = EmitAttackDamage
		self.EmitActorMinDamage = EmitActorMinDamage
		self.EmitPartsName = EmitPartsName
		self.CallSEKeyAtAtOn = CallSEKeyAtAtOn
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.NearDist = NearDist
		self.NearMoveSpeed = NearMoveSpeed
		self.FarDist = FarDist
		self.FarMoveSpeed = FarMoveSpeed


class SiteBossMove:

	def __init__(self, Name, Speed, AccRatio, UpdownSpeed, Amplitude, ASName, RotateRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.AccRatio = AccRatio
		self.UpdownSpeed = UpdownSpeed
		self.Amplitude = Amplitude
		self.ASName = ASName
		self.RotateRate = RotateRate


class SiteBossMoveAndAttack:

	def __init__(self, Name, Speed, AccRatio, UpdownSpeed, Amplitude, ASName, RotateRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.AccRatio = AccRatio
		self.UpdownSpeed = UpdownSpeed
		self.Amplitude = Amplitude
		self.ASName = ASName
		self.RotateRate = RotateRate


class SiteBossShieldBashAttack:

	def __init__(self, Name, AtMinDamage, InitSpeed, KeepDist, MoveSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AtMinDamage = AtMinDamage
		self.InitSpeed = InitSpeed
		self.KeepDist = KeepDist
		self.MoveSpeed = MoveSpeed


class SiteBossShootArrowRain:

	def __init__(self, Name, ArrowType, InitSpeed, BaseNode, IgniteOffset, IgniteRotate, TargetOffsetY, ASName, IsConnectChild, IsCheckASEvent, IsTurnToTarget, DirMinAngle, DirMaxAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ArrowType = ArrowType
		self.InitSpeed = InitSpeed
		self.BaseNode = BaseNode
		self.IgniteOffset = IgniteOffset
		self.IgniteRotate = IgniteRotate
		self.TargetOffsetY = TargetOffsetY
		self.ASName = ASName
		self.IsConnectChild = IsConnectChild
		self.IsCheckASEvent = IsCheckASEvent
		self.IsTurnToTarget = IsTurnToTarget
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle


class SiteBossShootIceSplinter:

	def __init__(self, Name, ThrowASName, InitVelocity, BindNodeName, ThrowIdxOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ThrowASName = ThrowASName
		self.InitVelocity = InitVelocity
		self.BindNodeName = BindNodeName
		self.ThrowIdxOffset = ThrowIdxOffset


class SiteBossShootNormalArrow:

	def __init__(self, Name, InitSpeed, BaseNode, IgniteOffset, IgniteRotate, TargetOffsetY, ASName, IsConnectChild, IsCheckASEvent, IsTurnToTarget, DirMinAngle, DirMaxAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InitSpeed = InitSpeed
		self.BaseNode = BaseNode
		self.IgniteOffset = IgniteOffset
		self.IgniteRotate = IgniteRotate
		self.TargetOffsetY = TargetOffsetY
		self.ASName = ASName
		self.IsConnectChild = IsConnectChild
		self.IsCheckASEvent = IsCheckASEvent
		self.IsTurnToTarget = IsTurnToTarget
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle


class SiteBossSpearAttackBase:

	def __init__(self, Name, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, CanBreakIceBlock, IsOnSpine1Rotate, IsOnSpine2Rotate, IsOnSpine3Rotate, TargetOffsetLowAtRotate, TargetOffsetHighAtRotate, CanJustAvoid, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.CanBreakIceBlock = CanBreakIceBlock
		self.IsOnSpine1Rotate = IsOnSpine1Rotate
		self.IsOnSpine2Rotate = IsOnSpine2Rotate
		self.IsOnSpine3Rotate = IsOnSpine3Rotate
		self.TargetOffsetLowAtRotate = TargetOffsetLowAtRotate
		self.TargetOffsetHighAtRotate = TargetOffsetHighAtRotate
		self.CanJustAvoid = CanJustAvoid


class SiteBossSpearAttackVertical:

	def __init__(self, Name, ShockWaveAttackPower, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, CanBreakIceBlock, IsOnSpine1Rotate, IsOnSpine2Rotate, IsOnSpine3Rotate, TargetOffsetLowAtRotate, TargetOffsetHighAtRotate, CanJustAvoid, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShockWaveAttackPower = ShockWaveAttackPower
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.CanBreakIceBlock = CanBreakIceBlock
		self.IsOnSpine1Rotate = IsOnSpine1Rotate
		self.IsOnSpine2Rotate = IsOnSpine2Rotate
		self.IsOnSpine3Rotate = IsOnSpine3Rotate
		self.TargetOffsetLowAtRotate = TargetOffsetLowAtRotate
		self.TargetOffsetHighAtRotate = TargetOffsetHighAtRotate
		self.CanJustAvoid = CanJustAvoid


class SiteBossSpearBlownOff:

	def __init__(self, Name, DownTimeAtLater, ForceRecoverDist, ForceRecoverOffset, AddForceRecoverTime, IsRemoveCharacterController, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DownTimeAtLater = DownTimeAtLater
		self.ForceRecoverDist = ForceRecoverDist
		self.ForceRecoverOffset = ForceRecoverOffset
		self.AddForceRecoverTime = AddForceRecoverTime
		self.IsRemoveCharacterController = IsRemoveCharacterController
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class SiteBossSpearChangeWaterLevel:

	def __init__(self, Name, IsSignalOn, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsSignalOn = IsSignalOn
		self.ASName = ASName


class SiteBossSwordAfterImageAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SiteBossSwordAfterImageMove:

	def __init__(self, Name, MoveFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveFrame = MoveFrame


class SiteBossSwordAttackBase:

	def __init__(self, Name, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, MoveSpeed, KeepDistance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.MoveSpeed = MoveSpeed
		self.KeepDistance = KeepDistance


class SiteBossSwordBlowOff:

	def __init__(self, Name, ForceRecoverDist, ForceRecoverOffset, AddForceRecoverTime, IsRemoveCharacterController, AddTime, LifeReflexRatio, ImpulseRatio, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ForceRecoverDist = ForceRecoverDist
		self.ForceRecoverOffset = ForceRecoverOffset
		self.AddForceRecoverTime = AddForceRecoverTime
		self.IsRemoveCharacterController = IsRemoveCharacterController
		self.AddTime = AddTime
		self.LifeReflexRatio = LifeReflexRatio
		self.ImpulseRatio = ImpulseRatio
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class SiteBossSwordChemicalPlus:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SiteBossSwordCreateIronPile:

	def __init__(self, Name, AppearPosDist, AppearPosHeight, CreateWaitTime, IgnitionInterval, PileScale, IsRotate, IsGuard, WaitAS, CreatePileAS, IsChasePlayer, CreateNum, AttackPower, AtMinDamage, AttackPowerForPlayer, AddAttackPower, NotCreatePosBase, NotCreateRange, ThunderActorName, IsRemainBoss, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AppearPosDist = AppearPosDist
		self.AppearPosHeight = AppearPosHeight
		self.CreateWaitTime = CreateWaitTime
		self.IgnitionInterval = IgnitionInterval
		self.PileScale = PileScale
		self.IsRotate = IsRotate
		self.IsGuard = IsGuard
		self.WaitAS = WaitAS
		self.CreatePileAS = CreatePileAS
		self.IsChasePlayer = IsChasePlayer
		self.CreateNum = CreateNum
		self.AttackPower = AttackPower
		self.AtMinDamage = AtMinDamage
		self.AttackPowerForPlayer = AttackPowerForPlayer
		self.AddAttackPower = AddAttackPower
		self.NotCreatePosBase = NotCreatePosBase
		self.NotCreateRange = NotCreateRange
		self.ThunderActorName = ThunderActorName
		self.IsRemainBoss = IsRemainBoss


class SiteBossSwordGuard:

	def __init__(self, Name, RotSubsAngRate, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSubsAngRate = RotSubsAngRate
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SiteBossSwordGuardBreak:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SiteBossSwordMove:

	def __init__(self, Name, AfterImage0AppearFrame, AfterImage1AppearFrame, AppearFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AfterImage0AppearFrame = AfterImage0AppearFrame
		self.AfterImage1AppearFrame = AfterImage1AppearFrame
		self.AppearFrame = AppearFrame


class SiteBossSwordShieldRepair:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SiteBossSwordSlowMove:

	def __init__(self, Name, AfterImage0AppearFrame, AfterImage1AppearFrame, AppearFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AfterImage0AppearFrame = AfterImage0AppearFrame
		self.AfterImage1AppearFrame = AfterImage1AppearFrame
		self.AppearFrame = AppearFrame


class SiteBossSwordThrowElectricBall:

	def __init__(self, Name, MoveOffset, MoveSpeed, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, PartsName, ASName, IsCalcNextPos, IsCheckPlayerAround, PredictionFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MoveOffset = MoveOffset
		self.MoveSpeed = MoveSpeed
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsName = PartsName
		self.ASName = ASName
		self.IsCalcNextPos = IsCalcNextPos
		self.IsCheckPlayerAround = IsCheckPlayerAround
		self.PredictionFrame = PredictionFrame


class SiteBossSwordWhirlSlash:

	def __init__(self, Name, RotSpd, FinRotate, PosReduceRatio, BaseRotRatio, IsIgnoreCancelAttack, AtMinDamage, AttackPower, AddAttackPower, JustAvoidAngle, JustAvoidSideDist, JustAvoidBackDist, ASName, MoveSpeed, KeepDistance, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsIgnoreCancelAttack = IsIgnoreCancelAttack
		self.AtMinDamage = AtMinDamage
		self.AttackPower = AttackPower
		self.AddAttackPower = AddAttackPower
		self.JustAvoidAngle = JustAvoidAngle
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.ASName = ASName
		self.MoveSpeed = MoveSpeed
		self.KeepDistance = KeepDistance


class SiteBossSwordWhirlSlashCharge:

	def __init__(self, Name, ChargeTime, InitSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ChargeTime = ChargeTime
		self.InitSpeed = InitSpeed


class SiteBossThrowParts:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, PartsName, ASName, IsCalcNextPos, IsCheckPlayerAround, PredictionFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsName = PartsName
		self.ASName = ASName
		self.IsCalcNextPos = IsCalcNextPos
		self.IsCheckPlayerAround = IsCheckPlayerAround
		self.PredictionFrame = PredictionFrame


class Sleep:

	def __init__(self, Name, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class SlideMoveViewTarget:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class SlippedBackWalk:

	def __init__(self, Name, ASName, AccRatio, Speed, RotSpd, RotAddRatio, Time, FinishDist, WeaponIdx, DecelRatio, IsCliffCheck, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AccRatio = AccRatio
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotAddRatio = RotAddRatio
		self.Time = Time
		self.FinishDist = FinishDist
		self.WeaponIdx = WeaponIdx
		self.DecelRatio = DecelRatio
		self.IsCliffCheck = IsCliffCheck


class SlippedCircleWalk:

	def __init__(self, Name, ASName, Speed, RotSpd, RotDist, AccRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist
		self.AccRatio = AccRatio


class SlippedWalk:

	def __init__(self, Name, ASName, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, AccRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.AccRatio = AccRatio


class SmallDamage:

	def __init__(self, Name, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SmallDamageBackward:

	def __init__(self, Name, ASName, IsReStartASByDamage, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsReStartASByDamage = IsReStartASByDamage
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SmallDamageDirectPreTargetBack:

	def __init__(self, Name, PreTargetBone, ASName, IsSetHitPosSelecter, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreTargetBone = PreTargetBone
		self.ASName = ASName
		self.IsSetHitPosSelecter = IsSetHitPosSelecter
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SmallDamageDirectPreTargetBone:

	def __init__(self, Name, PreTargetBone, ASName, IsSetHitPosSelecter, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreTargetBone = PreTargetBone
		self.ASName = ASName
		self.IsSetHitPosSelecter = IsSetHitPosSelecter
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SoundOcclusionTagAction:

	def __init__(self, Name, OcclusionLevel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.OcclusionLevel = OcclusionLevel


class SoundOcclusionTagRemainsWater:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SoundProxyRootAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SoundReverbAreaTagAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SoundShieldingAreaTagAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SoundTrigger:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SoundTriggerFadeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SpinFlyAttack:

	def __init__(self, Name, RotSpeed, AttackSpeed, AttackSlowDownRatio, Time, TargetHeightOffset, ThroughDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.AttackSpeed = AttackSpeed
		self.AttackSlowDownRatio = AttackSlowDownRatio
		self.Time = Time
		self.TargetHeightOffset = TargetHeightOffset
		self.ThroughDist = ThroughDist


class SpotBgmTriggerAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SpreadToEnemy:

	def __init__(self, Name, SpreadDist, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SpreadDist = SpreadDist
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StalEnemyBlownOff:

	def __init__(self, Name, DownTimeBase, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, RecoverTimer, DisableBoneName, DownTimeRand, EnableConstraintName, HeadShotAddVec, HeadShotSpeed, HeadShotUseAddVec, UseRagConName, WeaponDropSpeedY, WeaponDropSpeedXZ, BlownOffASName, PreUniteASName, UniteASName, DieASName, HeadRagdollRigidNames, ArmRagdollRigidNames, HeadSpeedRate, MinHeadSpeedY, MinHeadSpeedXZ, HeadRotateOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DownTimeBase = DownTimeBase
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.RecoverTimer = RecoverTimer
		self.DisableBoneName = DisableBoneName
		self.DownTimeRand = DownTimeRand
		self.EnableConstraintName = EnableConstraintName
		self.HeadShotAddVec = HeadShotAddVec
		self.HeadShotSpeed = HeadShotSpeed
		self.HeadShotUseAddVec = HeadShotUseAddVec
		self.UseRagConName = UseRagConName
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.BlownOffASName = BlownOffASName
		self.PreUniteASName = PreUniteASName
		self.UniteASName = UniteASName
		self.DieASName = DieASName
		self.HeadRagdollRigidNames = HeadRagdollRigidNames
		self.ArmRagdollRigidNames = ArmRagdollRigidNames
		self.HeadSpeedRate = HeadSpeedRate
		self.MinHeadSpeedY = MinHeadSpeedY
		self.MinHeadSpeedXZ = MinHeadSpeedXZ
		self.HeadRotateOffset = HeadRotateOffset


class StalEnemyDie:

	def __init__(self, Name, PreDieASName, ASName, Time, PosBaseRagdollName, EnableConstraintName, AngReduceRatio, PosReduceRatio, ForceDropWeapon, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PreDieASName = PreDieASName
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollName = PosBaseRagdollName
		self.EnableConstraintName = EnableConstraintName
		self.AngReduceRatio = AngReduceRatio
		self.PosReduceRatio = PosReduceRatio
		self.ForceDropWeapon = ForceDropWeapon


class StalEnemyHeadShotReaction:

	def __init__(self, Name, ASName, AddVec, Speed, UseAddVec, RotVec, RotSpd, HeadBoneKey, IsTgOff, IsDropWeapon, IsChangeable, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AddVec = AddVec
		self.Speed = Speed
		self.UseAddVec = UseAddVec
		self.RotVec = RotVec
		self.RotSpd = RotSpd
		self.HeadBoneKey = HeadBoneKey
		self.IsTgOff = IsTgOff
		self.IsDropWeapon = IsDropWeapon
		self.IsChangeable = IsChangeable
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StalEnemyHideWait:

	def __init__(self, Name, ASName, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StalPartCatch:

	def __init__(self, Name, PartIndex, BaseRagdollRigidBodyName, SecondRagdollRigidBodyName, ThirdRagdollRigidBodyName, ConstraintNames, FreeMoveRagdollRigidBodyNames, ASName, InputWeightTimer, BlendWeightTimer, UnitePosOffset, UniteRotOffset, SecondUnitePosOffset, SecondUniteRotOffset, ThirdUnitePosOffset, ThirdUniteRotOffset, UseRagConName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PartIndex = PartIndex
		self.BaseRagdollRigidBodyName = BaseRagdollRigidBodyName
		self.SecondRagdollRigidBodyName = SecondRagdollRigidBodyName
		self.ThirdRagdollRigidBodyName = ThirdRagdollRigidBodyName
		self.ConstraintNames = ConstraintNames
		self.FreeMoveRagdollRigidBodyNames = FreeMoveRagdollRigidBodyNames
		self.ASName = ASName
		self.InputWeightTimer = InputWeightTimer
		self.BlendWeightTimer = BlendWeightTimer
		self.UnitePosOffset = UnitePosOffset
		self.UniteRotOffset = UniteRotOffset
		self.SecondUnitePosOffset = SecondUnitePosOffset
		self.SecondUniteRotOffset = SecondUniteRotOffset
		self.ThirdUnitePosOffset = ThirdUnitePosOffset
		self.ThirdUniteRotOffset = ThirdUniteRotOffset
		self.UseRagConName = UseRagConName


class StartHeartDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StartLifeUpDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StartMapOpenDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StartShiekSensorGaugeDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StartStaminaUpDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StartupTelescope:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StepDoubleAttack:

	def __init__(self, Name, CloseDist, WeaponIdx, Speed, RotSpd, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.WeaponIdx = WeaponIdx
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle


class StepDoubleLargeAttack:

	def __init__(self, Name, CloseDist, WeaponIdx, Speed, RotSpd, JustAvoidSideDist, JustAvoidBackDist, JustAvoidAngle, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CloseDist = CloseDist
		self.WeaponIdx = WeaponIdx
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.JustAvoidSideDist = JustAvoidSideDist
		self.JustAvoidBackDist = JustAvoidBackDist
		self.JustAvoidAngle = JustAvoidAngle


class Stick:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StopASIgnite:

	def __init__(self, Name, IgniteOffset, IgniteVelocityDir, IgniteSpeed, IgniteRotate, IgniteRotSpeed, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteVelocityDir = IgniteVelocityDir
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StopASPlay:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StopAllDemoSoundAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StopChargeChemicalWeaponPower:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StopCliffTongueAttack:

	def __init__(self, Name, RigidName, PosReduceRatio, AngReduceRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RigidName = RigidName
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio
		self.ASName = ASName


class StopEventMiniGameTime:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StopForLimitedTime:

	def __init__(self, Name, KeepActRotation, EnableStaticCompoundRotate, ASKeyName, IsSetEndByTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.KeepActRotation = KeepActRotation
		self.EnableStaticCompoundRotate = EnableStaticCompoundRotate
		self.ASKeyName = ASKeyName
		self.IsSetEndByTime = IsSetEndByTime


class StopJump:

	def __init__(self, Name, JumpLoopAS, LandingAS, JumpHeight, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.JumpLoopAS = JumpLoopAS
		self.LandingAS = LandingAS
		self.JumpHeight = JumpHeight
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class StorePlayerPosAndRotate:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class StrangeBeacon:

	def __init__(self, Name, SaveFlag, CalcStartFlag, KeyName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SaveFlag = SaveFlag
		self.CalcStartFlag = CalcStartFlag
		self.KeyName = KeyName


class Stun:

	def __init__(self, Name, Time, HitImpactForceSmallSwordS, HitImpactForceLargeSwordS, HitImpactForceDaggerS, HitImpactForceSpearS, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceDaggerS = HitImpactForceDaggerS
		self.HitImpactForceSpearS = HitImpactForceSpearS


class SubAnmBlownOff:

	def __init__(self, Name, SubAS, SubASSlot, LeaveSubAS, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, OnGroundTime, AS, IsFinishByAnm, IsWaitForAnmEnd, WeaponDropSpeedXZ, WeaponDropSpeedY, IsItemDrop, IsFinishByWater, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.LeaveSubAS = LeaveSubAS
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.OnGroundTime = OnGroundTime
		self.AS = AS
		self.IsFinishByAnm = IsFinishByAnm
		self.IsWaitForAnmEnd = IsWaitForAnmEnd
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.IsItemDrop = IsItemDrop
		self.IsFinishByWater = IsFinishByWater
		self.UseKnockbackDir = UseKnockbackDir


class SubAnmKnockBackShock:

	def __init__(self, Name, SubAS, SubASSlot, LeaveSubAS, ASName, HitImpactForce, VelReduce, VelReduceOnGround, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.LeaveSubAS = LeaveSubAS
		self.ASName = ASName
		self.HitImpactForce = HitImpactForce
		self.VelReduce = VelReduce
		self.VelReduceOnGround = VelReduceOnGround


class SubAnmSmallDamage:

	def __init__(self, Name, SubAS, SubASSlot, LeaveSubAS, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAS = SubAS
		self.SubASSlot = SubASSlot
		self.LeaveSubAS = LeaveSubAS
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SunMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SwarmAreaDamaged:

	def __init__(self, Name, DeadSubActorMax, RiseSpeedMin, IgnoreHitGroundTime, Time, SubAccRateMin, SubAccRateMax, Speed, IsCreateDeadActor, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeadSubActorMax = DeadSubActorMax
		self.RiseSpeedMin = RiseSpeedMin
		self.IgnoreHitGroundTime = IgnoreHitGroundTime
		self.Time = Time
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.Speed = Speed
		self.IsCreateDeadActor = IsCreateDeadActor


class SwarmChemicalDamaged:

	def __init__(self, Name, ResetChemicalTimer, IsResetAllObject, DeadSubActorMax, RiseSpeedMin, IgnoreHitGroundTime, Time, SubAccRateMin, SubAccRateMax, Speed, IsCreateDeadActor, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ResetChemicalTimer = ResetChemicalTimer
		self.IsResetAllObject = IsResetAllObject
		self.DeadSubActorMax = DeadSubActorMax
		self.RiseSpeedMin = RiseSpeedMin
		self.IgnoreHitGroundTime = IgnoreHitGroundTime
		self.Time = Time
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.Speed = Speed
		self.IsCreateDeadActor = IsCreateDeadActor


class SwarmDamaged:

	def __init__(self, Name, DeadSubActorMax, RiseSpeedMin, IgnoreHitGroundTime, Time, SubAccRateMin, SubAccRateMax, Speed, IsCreateDeadActor, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DeadSubActorMax = DeadSubActorMax
		self.RiseSpeedMin = RiseSpeedMin
		self.IgnoreHitGroundTime = IgnoreHitGroundTime
		self.Time = Time
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.Speed = Speed
		self.IsCreateDeadActor = IsCreateDeadActor


class SwarmFlyAttack:

	def __init__(self, Name, FailTimeInClosePos, ApplyMaterialAnimDist, ApplyMaterialAnimNumPerFrame, SubAccRateMin, SubAccRateMax, IgnoreSensorTime, MaterialAnimName, MaterialAnimFrame, Speed, RotSpd, FinRotate, HorizontalFinRadius, TargetHeightOffset, RotRatio, VerticalFinLength, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FailTimeInClosePos = FailTimeInClosePos
		self.ApplyMaterialAnimDist = ApplyMaterialAnimDist
		self.ApplyMaterialAnimNumPerFrame = ApplyMaterialAnimNumPerFrame
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.IgnoreSensorTime = IgnoreSensorTime
		self.MaterialAnimName = MaterialAnimName
		self.MaterialAnimFrame = MaterialAnimFrame
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.VerticalFinLength = VerticalFinLength


class SwarmFlyMove:

	def __init__(self, Name, SubAccRateMin, SubAccRateMax, IgnoreSensorTime, MaterialAnimName, MaterialAnimFrame, Speed, RotSpd, FinRotate, HorizontalFinRadius, TargetHeightOffset, RotRatio, VerticalFinLength, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.IgnoreSensorTime = IgnoreSensorTime
		self.MaterialAnimName = MaterialAnimName
		self.MaterialAnimFrame = MaterialAnimFrame
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.VerticalFinLength = VerticalFinLength


class SwarmGullMove:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class SwarmLevelFlyMove:

	def __init__(self, Name, SubAccRateMin, SubAccRateMax, IgnoreSensorTime, MaterialAnimName, MaterialAnimFrame, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, IsOverRise, CheckStopSpeed, IsSlowDownNearGoal, VibrateMemoryStep, VibrateCheckFrame, VibrateStopCheck, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SubAccRateMin = SubAccRateMin
		self.SubAccRateMax = SubAccRateMax
		self.IgnoreSensorTime = IgnoreSensorTime
		self.MaterialAnimName = MaterialAnimName
		self.MaterialAnimFrame = MaterialAnimFrame
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.IsOverRise = IsOverRise
		self.CheckStopSpeed = CheckStopSpeed
		self.IsSlowDownNearGoal = IsSlowDownNearGoal
		self.VibrateMemoryStep = VibrateMemoryStep
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateStopCheck = VibrateStopCheck
		self.FlyHeightMin = FlyHeightMin


class SweepCollision:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SwimEnemyAnmBackBlownOff:

	def __init__(self, Name, RotSpeed, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, AS, InWaterDepth, FloatDepth, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.AS = AS
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.UseKnockbackDir = UseKnockbackDir


class SwimEnemyAnmBackBlownOffFromPL:

	def __init__(self, Name, RotSpeed, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, AS, InWaterDepth, FloatDepth, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.AS = AS
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.UseKnockbackDir = UseKnockbackDir


class SwimEnemyAnmBackBlownOffToPL:

	def __init__(self, Name, RotSpeed, Speed, BlownHeight, PosReduceRatio, RotReduceRatio, AS, InWaterDepth, FloatDepth, UseKnockbackDir, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.Speed = Speed
		self.BlownHeight = BlownHeight
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.AS = AS
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.UseKnockbackDir = UseKnockbackDir


class SwimGetUp:

	def __init__(self, Name, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, UnderWaterDepth, RotRatio, ASName, RootOffset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.UnderWaterDepth = UnderWaterDepth
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.RootOffset = RootOffset


class SwimMove:

	def __init__(self, Name, ASName, Speed, RotSpeed, FinRadius, FinRotate, BaseRotRatio, WeaponIdx, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.BaseRotRatio = BaseRotRatio
		self.WeaponIdx = WeaponIdx
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class SwimMoveASHoldEvent:

	def __init__(self, Name, ASName, PosReduceRatio, Speed, RotSpeed, FinRadius, FinRotate, BaseRotRatio, WeaponIdx, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.BaseRotRatio = BaseRotRatio
		self.WeaponIdx = WeaponIdx
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class SwimMoveOneTimeAS:

	def __init__(self, Name, ASName, IsIgnoreSameKey, Speed, RotSpeed, FinRadius, FinRotate, BaseRotRatio, WeaponIdx, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSameKey = IsIgnoreSameKey
		self.Speed = Speed
		self.RotSpeed = RotSpeed
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.BaseRotRatio = BaseRotRatio
		self.WeaponIdx = WeaponIdx
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class SwimNoticeTurn:

	def __init__(self, Name, AngSpd, ASName, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AngSpd = AngSpd
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class SwimSmallDamage:

	def __init__(self, Name, ASName, InWaterDepth, FloatDepth, FloatRadius, VelReduce, HitImpactForceSmallSwordS, HitImpactForceSmallSwordL, HitImpactForceLargeSwordS, HitImpactForceLargeSwordL, HitImpactForceSpearS, HitImpactForceSpearL, HighSpeedY, VelReduceY, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.VelReduce = VelReduce
		self.HitImpactForceSmallSwordS = HitImpactForceSmallSwordS
		self.HitImpactForceSmallSwordL = HitImpactForceSmallSwordL
		self.HitImpactForceLargeSwordS = HitImpactForceLargeSwordS
		self.HitImpactForceLargeSwordL = HitImpactForceLargeSwordL
		self.HitImpactForceSpearS = HitImpactForceSpearS
		self.HitImpactForceSpearL = HitImpactForceSpearL
		self.HighSpeedY = HighSpeedY
		self.VelReduceY = VelReduceY


class SwimTurn:

	def __init__(self, Name, ASName, FinRotate, PosReduceRatio, RotSpeed, RotRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.FinRotate = FinRotate
		self.PosReduceRatio = PosReduceRatio
		self.RotSpeed = RotSpeed
		self.RotRatio = RotRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class SwitchElectricOff:

	def __init__(self, Name, VolReq, TargetVol, UseSklAnm, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.VolReq = VolReq
		self.TargetVol = TargetVol
		self.UseSklAnm = UseSklAnm


class SwitchElectricOn:

	def __init__(self, Name, ElecReq, VolReq, TargetVol, MinEnergyRate, UseSklAnm, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ElecReq = ElecReq
		self.VolReq = VolReq
		self.TargetVol = TargetVol
		self.MinEnergyRate = MinEnergyRate
		self.UseSklAnm = UseSklAnm


class SwitchPlayerEquipment:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SwitchStepSliderConstraint:

	def __init__(self, Name, Impulse, MinLimit, MaxLimit, SwTh, Friction, OnASName, OffASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Impulse = Impulse
		self.MinLimit = MinLimit
		self.MaxLimit = MaxLimit
		self.SwTh = SwTh
		self.Friction = Friction
		self.OnASName = OnASName
		self.OffASName = OffASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class SwitchStepSliderConstraintOnce:

	def __init__(self, Name, Impulse, MinLimit, MaxLimit, SwTh, Friction, OnASName, OffASName, IsIgnoreSame, TargetIdx, SeqBankIdx, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Impulse = Impulse
		self.MinLimit = MinLimit
		self.MaxLimit = MaxLimit
		self.SwTh = SwTh
		self.Friction = Friction
		self.OnASName = OnASName
		self.OffASName = OffASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx


class SwitchWindmill:

	def __init__(self, Name, SwRadTh, SwRadAllowance, TargetNodeName, RotAccel, MaxRotSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SwRadTh = SwRadTh
		self.SwRadAllowance = SwRadAllowance
		self.TargetNodeName = TargetNodeName
		self.RotAccel = RotAccel
		self.MaxRotSpeed = MaxRotSpeed


class SystemApplyEnvSetAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SystemDelete:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SystemFadeOutSleep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SystemHide:

	def __init__(self, Name, IsOnAttention, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOnAttention = IsOnAttention
		self.ASName = ASName


class SystemHideChase:

	def __init__(self, Name, IsOnAttention, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsOnAttention = IsOnAttention
		self.ASName = ASName


class SystemSetWindAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SystemSleep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class SystemWarp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TakeoffFromCeilLookTarget:

	def __init__(self, Name, DescentSpeed, AccRatio, RotSpeed, RotRatio, PosReduceRatio, RotReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DescentSpeed = DescentSpeed
		self.AccRatio = AccRatio
		self.RotSpeed = RotSpeed
		self.RotRatio = RotRatio
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio


class TargetCircleGuardWalk:

	def __init__(self, Name, Speed, RotSpd, RotDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist


class TargetCircleMoveKeepDist:

	def __init__(self, Name, ASName, Speed, RotSpd, RotDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist


class TargetCircleSwim:

	def __init__(self, Name, FloatDepth, FloatRadius, FloatCycleTime, InWaterDepth, ChangeDepthSpeed, Speed, RotSpd, RotDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.InWaterDepth = InWaterDepth
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist


class TargetCircleWalk:

	def __init__(self, Name, Speed, RotSpd, RotDist, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.RotDist = RotDist


class TeachPlayerInAreaForRefActor:

	def __init__(self, Name, NextTimer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.NextTimer = NextTimer


class Teleport:

	def __init__(self, Name, DistXZ, DistY, WaitTime, TimeRand, IsUseChangePos, EffectName, IsLifeGageKeep, IsLand, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistXZ = DistXZ
		self.DistY = DistY
		self.WaitTime = WaitTime
		self.TimeRand = TimeRand
		self.IsUseChangePos = IsUseChangePos
		self.EffectName = EffectName
		self.IsLifeGageKeep = IsLifeGageKeep
		self.IsLand = IsLand


class TeleportForceApperPosition:

	def __init__(self, Name, HideEffectName, IsArriveAtTarget, ArriveAtTargetRange, ArriveAtTargetTimeOut, WaitTime, TimeRand, IsUseChangePos, EffectName, IsLifeGageKeep, IsLand, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.HideEffectName = HideEffectName
		self.IsArriveAtTarget = IsArriveAtTarget
		self.ArriveAtTargetRange = ArriveAtTargetRange
		self.ArriveAtTargetTimeOut = ArriveAtTargetTimeOut
		self.WaitTime = WaitTime
		self.TimeRand = TimeRand
		self.IsUseChangePos = IsUseChangePos
		self.EffectName = EffectName
		self.IsLifeGageKeep = IsLifeGageKeep
		self.IsLand = IsLand


class TeleportTargetFrontInAir:

	def __init__(self, Name, DistMin, DistMax, FrontAngle, HeightOffset, TerritoryArea, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DistMin = DistMin
		self.DistMax = DistMax
		self.FrontAngle = FrontAngle
		self.HeightOffset = HeightOffset
		self.TerritoryArea = TerritoryArea


class TerrainCalcCenter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TerrainHideCenter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TestAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Throw:

	def __init__(self, Name, ShootSpd, ShootAng, BlurMax, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootSpd = ShootSpd
		self.ShootAng = ShootAng
		self.BlurMax = BlurMax
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ThrowLeft:

	def __init__(self, Name, ShootSpd, ShootAng, BlurMax, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootSpd = ShootSpd
		self.ShootAng = ShootAng
		self.BlurMax = BlurMax
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ThrowRight:

	def __init__(self, Name, ShootSpd, ShootAng, BlurMax, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootSpd = ShootSpd
		self.ShootAng = ShootAng
		self.BlurMax = BlurMax
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ThrowWeaponByBodyCenter:

	def __init__(self, Name, ASName, WeaponIdx, SpeedMin, SpeedMax, ThrowAng, ThrowBoomerangAng, ThrowBoomerangSpeedMax, IsForceDead, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.WeaponIdx = WeaponIdx
		self.SpeedMin = SpeedMin
		self.SpeedMax = SpeedMax
		self.ThrowAng = ThrowAng
		self.ThrowBoomerangAng = ThrowBoomerangAng
		self.ThrowBoomerangSpeedMax = ThrowBoomerangSpeedMax
		self.IsForceDead = IsForceDead
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ThrowWeaponRight:

	def __init__(self, Name, WeaponIdx, SpeedMin, SpeedMax, ThrowAng, ThrowBoomerangAng, ThrowBoomerangSpeedMax, IsForceDead, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.SpeedMin = SpeedMin
		self.SpeedMax = SpeedMax
		self.ThrowAng = ThrowAng
		self.ThrowBoomerangAng = ThrowBoomerangAng
		self.ThrowBoomerangSpeedMax = ThrowBoomerangSpeedMax
		self.IsForceDead = IsForceDead
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class Thrown:

	def __init__(self, Name, AS, RotSpd, ReactionLevel, IsForceOnly, IsOnImpact, ThrownKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS
		self.RotSpd = RotSpd
		self.ReactionLevel = ReactionLevel
		self.IsForceOnly = IsForceOnly
		self.IsOnImpact = IsOnImpact
		self.ThrownKey = ThrownKey


class ThrownAndBreak:

	def __init__(self, Name, AS, RotSpd, ReactionLevel, IsForceOnly, IsOnImpact, ThrownKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AS = AS
		self.RotSpd = RotSpd
		self.ReactionLevel = ReactionLevel
		self.IsForceOnly = IsForceOnly
		self.IsOnImpact = IsOnImpact
		self.ThrownKey = ThrownKey


class ThrownDown:

	def __init__(self, Name, ASName, Time, PosBaseRagdollRbName, DownBackCtrlOffset, DownFrontCtrlOffset, WeaponDropSpeedXZ, WeaponDropSpeedY, InWaterDownTime, IsWaitAS, ForceFinishTime, StableASName, IsItemDrop, OnGroundDownTime, GetUpGroundAngle, ForceEndWaterDepth, IsCheckVibrate, StartUpdateFriction, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.PosBaseRagdollRbName = PosBaseRagdollRbName
		self.DownBackCtrlOffset = DownBackCtrlOffset
		self.DownFrontCtrlOffset = DownFrontCtrlOffset
		self.WeaponDropSpeedXZ = WeaponDropSpeedXZ
		self.WeaponDropSpeedY = WeaponDropSpeedY
		self.InWaterDownTime = InWaterDownTime
		self.IsWaitAS = IsWaitAS
		self.ForceFinishTime = ForceFinishTime
		self.StableASName = StableASName
		self.IsItemDrop = IsItemDrop
		self.OnGroundDownTime = OnGroundDownTime
		self.GetUpGroundAngle = GetUpGroundAngle
		self.ForceEndWaterDepth = ForceEndWaterDepth
		self.IsCheckVibrate = IsCheckVibrate
		self.StartUpdateFriction = StartUpdateFriction


class ThrownSpear:

	def __init__(self, Name, RotSpeedZ, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeedZ = RotSpeedZ


class TimeSpecControllerRumble:

	def __init__(self, Name, Pattern, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Pattern = Pattern


class TimeredASPlay:

	def __init__(self, Name, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class TimeredHorseRideViewWait:

	def __init__(self, Name, Time, TimeRand, RotRatio, ASName, UpperBodyASSlot, LowerBodyASSlot, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.RotRatio = RotRatio
		self.ASName = ASName
		self.UpperBodyASSlot = UpperBodyASSlot
		self.LowerBodyASSlot = LowerBodyASSlot


class TimeredNeckSpin:

	def __init__(self, Name, Time, SpinSpeedRatio, InitSpinSpeed, SpinSpeed, NeckUDAngle, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.SpinSpeedRatio = SpinSpeedRatio
		self.InitSpinSpeed = InitSpinSpeed
		self.SpinSpeed = SpinSpeed
		self.NeckUDAngle = NeckUDAngle
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class TimeredPreJumpAttack:

	def __init__(self, Name, Time, TimeRand, TurnSpd, ASName, PosReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.TurnSpd = TurnSpd
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio


class ToCDungeon:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TornadoMove:

	def __init__(self, Name, MaxAmplitude, MinAmplitude, MaxSpeed, AmplitudeAddRate, DeleteTimer, Frequency, IgnoreHitFrame, IsHitOnlyPlayer, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxAmplitude = MaxAmplitude
		self.MinAmplitude = MinAmplitude
		self.MaxSpeed = MaxSpeed
		self.AmplitudeAddRate = AmplitudeAddRate
		self.DeleteTimer = DeleteTimer
		self.Frequency = Frequency
		self.IgnoreHitFrame = IgnoreHitFrame
		self.IsHitOnlyPlayer = IsHitOnlyPlayer


class TowingBrake:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TreasureBoxBurnedOut:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TreasureBoxOpenWait:

	def __init__(self, Name, ASName, IsIgnoreSame, TargetIdx, SeqBankIdx, ASName_PreOpen, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.TargetIdx = TargetIdx
		self.SeqBankIdx = SeqBankIdx
		self.ASName_PreOpen = ASName_PreOpen


class TreasureLocaterRoot:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TriggerAllPartsSleep:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Tumble:

	def __init__(self, Name, TumblingTime, GetUpTime, LandCheckNode, TumbleAngle, TumbleSpeed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TumblingTime = TumblingTime
		self.GetUpTime = GetUpTime
		self.LandCheckNode = LandCheckNode
		self.TumbleAngle = TumbleAngle
		self.TumbleSpeed = TumbleSpeed


class Turn:

	def __init__(self, Name, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class TurnAndChargeAndShoot:

	def __init__(self, Name, RotSpeed, StopSpeedRatio, StopRotSpeedRatio, WeaponIdx, OffsetRangeMin, OffsetRangeMax, OffsetRateByDist, OffsetRangeMinOutOfScreen, OffsetRangeMaxOutOfScreen, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpeed = RotSpeed
		self.StopSpeedRatio = StopSpeedRatio
		self.StopRotSpeedRatio = StopRotSpeedRatio
		self.WeaponIdx = WeaponIdx
		self.OffsetRangeMin = OffsetRangeMin
		self.OffsetRangeMax = OffsetRangeMax
		self.OffsetRateByDist = OffsetRateByDist
		self.OffsetRangeMinOutOfScreen = OffsetRangeMinOutOfScreen
		self.OffsetRangeMaxOutOfScreen = OffsetRangeMaxOutOfScreen
		self.ASName = ASName


class TurnAndLookAtToObjectNow:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TurnAndLookToObjNotAnimDriven:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TurnAndLookToObject:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class TurnIgnite:

	def __init__(self, Name, RotSpd, IgniteOffset, IgniteVelocityDir, IgniteSpeed, IgniteRotate, IgniteRotSpeed, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotSpd = RotSpd
		self.IgniteOffset = IgniteOffset
		self.IgniteVelocityDir = IgniteVelocityDir
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class TurnToEmptySpace:

	def __init__(self, Name, CheckDistance, CheckAngOffset, CheckShapeRadius, CastOffset, CheckAngOffsetX, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.CheckDistance = CheckDistance
		self.CheckAngOffset = CheckAngOffset
		self.CheckShapeRadius = CheckShapeRadius
		self.CastOffset = CastOffset
		self.CheckAngOffsetX = CheckAngOffsetX


class TurnWithAS:

	def __init__(self, Name, ASName, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class UKingEmitEffectLoopAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class UnarmedAttack:

	def __init__(self, Name, ASName, AtRigidBodyName, Speed, RotAngle, SpeedStopRatio, RotSpeedStopRatio, JustAvoidCheckLength, JustAvoidCheckAngle, IsIgnoreSmallHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AtRigidBodyName = AtRigidBodyName
		self.Speed = Speed
		self.RotAngle = RotAngle
		self.SpeedStopRatio = SpeedStopRatio
		self.RotSpeedStopRatio = RotSpeedStopRatio
		self.JustAvoidCheckLength = JustAvoidCheckLength
		self.JustAvoidCheckAngle = JustAvoidCheckAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit


class UnarmedLargeAttack:

	def __init__(self, Name, ASName, AtRigidBodyName, Speed, RotAngle, SpeedStopRatio, RotSpeedStopRatio, JustAvoidCheckLength, JustAvoidCheckAngle, IsIgnoreSmallHit, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.AtRigidBodyName = AtRigidBodyName
		self.Speed = Speed
		self.RotAngle = RotAngle
		self.SpeedStopRatio = SpeedStopRatio
		self.RotSpeedStopRatio = RotSpeedStopRatio
		self.JustAvoidCheckLength = JustAvoidCheckLength
		self.JustAvoidCheckAngle = JustAvoidCheckAngle
		self.IsIgnoreSmallHit = IsIgnoreSmallHit


class UpdateDataByGetDemoAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class UseNavMeshConnectAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class VacuumedItemShootToTarget:

	def __init__(self, Name, ShootOffset, ShootSpeed, ShootRotate, ShootRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, PartsKey, IsReuseBullet, SeqBank, TargetBone, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ShootOffset = ShootOffset
		self.ShootSpeed = ShootSpeed
		self.ShootRotate = ShootRotate
		self.ShootRotSpeed = ShootRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.PartsKey = PartsKey
		self.IsReuseBullet = IsReuseBullet
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class Vanish:

	def __init__(self, Name, DieType, NoDrop, ASName, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.DieType = DieType
		self.NoDrop = NoDrop
		self.ASName = ASName
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class ViewLevelFlyMove:

	def __init__(self, Name, IsCheckAnmSeqCancel, AddTargetDist, FailMoveTimer, IsNoBrake, ASName, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, IsOverRise, CheckStopSpeed, IsSlowDownNearGoal, VibrateMemoryStep, VibrateCheckFrame, VibrateStopCheck, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckAnmSeqCancel = IsCheckAnmSeqCancel
		self.AddTargetDist = AddTargetDist
		self.FailMoveTimer = FailMoveTimer
		self.IsNoBrake = IsNoBrake
		self.ASName = ASName
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.IsOverRise = IsOverRise
		self.CheckStopSpeed = CheckStopSpeed
		self.IsSlowDownNearGoal = IsSlowDownNearGoal
		self.VibrateMemoryStep = VibrateMemoryStep
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateStopCheck = VibrateStopCheck
		self.FlyHeightMin = FlyHeightMin


class Wait:

	def __init__(self, Name, Time, TimeRand, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WaitCloseItemDownloadDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitForASTriggerEvent:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitForCloseFade:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitForFrame:

	def __init__(self, Name, ValidInput, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ValidInput = ValidInput


class WaitForKeyInput:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitForStaminaUpDemoEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitHeartDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitMagneGear:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitMessageDialogEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitOnObj:

	def __init__(self, Name, Time, TimeRand, ASName, PosReduceRatio, RotReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.ASName = ASName
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio


class WaitTimer:

	def __init__(self, Name, WaitFrame, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrame = WaitFrame


class WaitUntilLifeUpDemo:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitUntilMapOpenDemoEnd:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaitWhileCreatingOwnedHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class Walk:

	def __init__(self, Name, Speed, RotSpd, FinRadius, FinRotate, WeaponIdx, BaseRotRatio, FollowGround, WallHitLimitTime, MoveAngCliffLimitTime, AccRatio, IgnoreLastCurve, IgnoreDecelerationFrontCliff, IgnoreMoveDirCoHit, JumpUpSpeedReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Speed = Speed
		self.RotSpd = RotSpd
		self.FinRadius = FinRadius
		self.FinRotate = FinRotate
		self.WeaponIdx = WeaponIdx
		self.BaseRotRatio = BaseRotRatio
		self.FollowGround = FollowGround
		self.WallHitLimitTime = WallHitLimitTime
		self.MoveAngCliffLimitTime = MoveAngCliffLimitTime
		self.AccRatio = AccRatio
		self.IgnoreLastCurve = IgnoreLastCurve
		self.IgnoreDecelerationFrontCliff = IgnoreDecelerationFrontCliff
		self.IgnoreMoveDirCoHit = IgnoreMoveDirCoHit
		self.JumpUpSpeedReduceRatio = JumpUpSpeedReduceRatio


class Warn:

	def __init__(self, Name, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WarpEffectValueSetter:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpMyHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpOwnedHorse:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPLAndResetGimmick:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPLToPosAndResetGimmick:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPlayerToActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPlayerToAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPlayerToAnchorGimmickReset:

	def __init__(self, Name, WaitFrameAfterReset, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WaitFrameAfterReset = WaitFrameAfterReset


class WarpPlayerToDestination:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpPlayerToReferenceAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToActor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToDynamicPos:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToGameDataVec3f:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToPos:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToScheduleAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WarpToStaticAnchor:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaterEmitter:

	def __init__(self, Name, Radius, Speed, Offset, Interval, VelocityDir, BindNodeName, EffectType, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.Speed = Speed
		self.Offset = Offset
		self.Interval = Interval
		self.VelocityDir = VelocityDir
		self.BindNodeName = BindNodeName
		self.EffectType = EffectType


class WaterExplode:

	def __init__(self, Name, Radius, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.Speed = Speed


class WaterFloatBase:

	def __init__(self, Name, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterFloatElectricParalysis:

	def __init__(self, Name, ASName, IgnoreSameAS, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.IgnoreSameAS = IgnoreSameAS
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterFloatFreeze:

	def __init__(self, Name, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterFloatIgniteToTarget:

	def __init__(self, Name, IgniteOffset, IgniteSpeed, IgniteRotate, IgniteRotSpeed, DirMinAngle, DirMaxAngle, MaxNoiseDist, OffsetHeight, BaseNode, ASName, IgnoreSameAS, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IgniteOffset = IgniteOffset
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.DirMinAngle = DirMinAngle
		self.DirMaxAngle = DirMaxAngle
		self.MaxNoiseDist = MaxNoiseDist
		self.OffsetHeight = OffsetHeight
		self.BaseNode = BaseNode
		self.ASName = ASName
		self.IgnoreSameAS = IgnoreSameAS
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterFloatWait:

	def __init__(self, Name, Time, TimeRand, ASName, IsIgnoreSameAS, IsEndWhenASFinished, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Time = Time
		self.TimeRand = TimeRand
		self.ASName = ASName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.IsEndWhenASFinished = IsEndWhenASFinished
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterFloatWaitEx:

	def __init__(self, Name, AdditionalPosReduceRatio, AdditionalAngleReduceRatio, AdditionalVelocityMax, WaterEffectSpeedRate, Time, TimeRand, ASName, IsIgnoreSameAS, IsEndWhenASFinished, PosReduceRatio, AngleReduceRatio, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, IsCheckWaterFall, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.AdditionalPosReduceRatio = AdditionalPosReduceRatio
		self.AdditionalAngleReduceRatio = AdditionalAngleReduceRatio
		self.AdditionalVelocityMax = AdditionalVelocityMax
		self.WaterEffectSpeedRate = WaterEffectSpeedRate
		self.Time = Time
		self.TimeRand = TimeRand
		self.ASName = ASName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.IsEndWhenASFinished = IsEndWhenASFinished
		self.PosReduceRatio = PosReduceRatio
		self.AngleReduceRatio = AngleReduceRatio
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.IsCheckWaterFall = IsCheckWaterFall


class WaterSurfaceModelOnly:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaterSurfaceMove:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WaterUpDownAnmDrivenMove:

	def __init__(self, Name, InWaterDepth, TargetDepth, PosReduceRatio, RotReduceRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.InWaterDepth = InWaterDepth
		self.TargetDepth = TargetDepth
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.ASName = ASName


class WaterUpDownDrivenPreAttack:

	def __init__(self, Name, TurnSpeed, InWaterDepth, TargetDepth, PosReduceRatio, RotReduceRatio, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TurnSpeed = TurnSpeed
		self.InWaterDepth = InWaterDepth
		self.TargetDepth = TargetDepth
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.ASName = ASName


class WaterUpDownMove:

	def __init__(self, Name, StartDepth, TargetDepth, ASName, InWaterDepth, PosReduceRatio, RotReduceRatio, AccRatio, WaterFloatRadius, WaterFloatCycleTime, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartDepth = StartDepth
		self.TargetDepth = TargetDepth
		self.ASName = ASName
		self.InWaterDepth = InWaterDepth
		self.PosReduceRatio = PosReduceRatio
		self.RotReduceRatio = RotReduceRatio
		self.AccRatio = AccRatio
		self.WaterFloatRadius = WaterFloatRadius
		self.WaterFloatCycleTime = WaterFloatCycleTime


class WeaponDrawn:

	def __init__(self, Name, WeaponIdx, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WeaponHold:

	def __init__(self, Name, WeaponIdx, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.WeaponIdx = WeaponIdx
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WeaponTrueFormEftCtrl:

	def __init__(self, Name, TransformKey, TrueFormKey, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.TransformKey = TransformKey
		self.TrueFormKey = TrueFormKey


class WildHorseCreate:

	def __init__(self, Name, MinCreateNum, MaxCreateNum, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MinCreateNum = MinCreateNum
		self.MaxCreateNum = MaxCreateNum


class WillBallAttack:

	def __init__(self, Name, ReactionLevel, IsAbleGuard, MaxSpeed, RotSpeed, ReachRange, TiredAngle, IsIgnoreLastSpRot, IsAddAABBHeight, IsGround, RotBaseRatio, Accel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ReactionLevel = ReactionLevel
		self.IsAbleGuard = IsAbleGuard
		self.MaxSpeed = MaxSpeed
		self.RotSpeed = RotSpeed
		self.ReachRange = ReachRange
		self.TiredAngle = TiredAngle
		self.IsIgnoreLastSpRot = IsIgnoreLastSpRot
		self.IsAddAABBHeight = IsAddAABBHeight
		self.IsGround = IsGround
		self.RotBaseRatio = RotBaseRatio
		self.Accel = Accel


class WillBallAvoidCenterDist:

	def __init__(self, Name, Dist, MaxDist, MiddleDist, MaxSpeed, RotSpeed, ReachRange, TiredAngle, IsIgnoreLastSpRot, IsAddAABBHeight, IsGround, RotBaseRatio, Accel, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Dist = Dist
		self.MaxDist = MaxDist
		self.MiddleDist = MiddleDist
		self.MaxSpeed = MaxSpeed
		self.RotSpeed = RotSpeed
		self.ReachRange = ReachRange
		self.TiredAngle = TiredAngle
		self.IsIgnoreLastSpRot = IsIgnoreLastSpRot
		self.IsAddAABBHeight = IsAddAABBHeight
		self.IsGround = IsGround
		self.RotBaseRatio = RotBaseRatio
		self.Accel = Accel


class WillBallParabolaAttack:

	def __init__(self, Name, MaxSpeed, MaxHeight, MinMoveXZ, GravityScale, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.MaxSpeed = MaxSpeed
		self.MaxHeight = MaxHeight
		self.MinMoveXZ = MinMoveXZ
		self.GravityScale = GravityScale


class WindControl:

	def __init__(self, Name, Radius, MaxSpeed, TargetNodeName, MaxRadSpeed, RadAccel, UseEnvTemperature, Temperature, IsModelControlOnly, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.MaxSpeed = MaxSpeed
		self.TargetNodeName = TargetNodeName
		self.MaxRadSpeed = MaxRadSpeed
		self.RadAccel = RadAccel
		self.UseEnvTemperature = UseEnvTemperature
		self.Temperature = Temperature
		self.IsModelControlOnly = IsModelControlOnly


class WindControlLength:

	def __init__(self, Name, Radius, MaxSpeed, TargetNodeName, MaxRadSpeed, RadAccel, UseEnvTemperature, Temperature, IsModelControlOnly, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.Radius = Radius
		self.MaxSpeed = MaxSpeed
		self.TargetNodeName = TargetNodeName
		self.MaxRadSpeed = MaxRadSpeed
		self.RadAccel = RadAccel
		self.UseEnvTemperature = UseEnvTemperature
		self.Temperature = Temperature
		self.IsModelControlOnly = IsModelControlOnly


class WindCutter:

	def __init__(self, Name, LevelRangeMult, LevelAtkMult, LevelScaleMult, IsLevelOneScaleOne, LevelBaseScaleAdd, AttackIntensity, AttackMinPower, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.LevelRangeMult = LevelRangeMult
		self.LevelAtkMult = LevelAtkMult
		self.LevelScaleMult = LevelScaleMult
		self.IsLevelOneScaleOne = IsLevelOneScaleOne
		self.LevelBaseScaleAdd = LevelBaseScaleAdd
		self.AttackIntensity = AttackIntensity
		self.AttackMinPower = AttackMinPower


class Windmill_Wing:

	def __init__(self, Name, StartFrameRange, ASPlaySpeedMin, ASPlaySpeedMax, IsTurnToWindDir, ASPlaySpeedMinWindPower, ASPlaySpeedMaxWindPower, TurnRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartFrameRange = StartFrameRange
		self.ASPlaySpeedMin = ASPlaySpeedMin
		self.ASPlaySpeedMax = ASPlaySpeedMax
		self.IsTurnToWindDir = IsTurnToWindDir
		self.ASPlaySpeedMinWindPower = ASPlaySpeedMinWindPower
		self.ASPlaySpeedMaxWindPower = ASPlaySpeedMaxWindPower
		self.TurnRate = TurnRate


class Windmill_WingWithAutoAnime:

	def __init__(self, Name, StartFrameRange, ASPlaySpeedMin, ASPlaySpeedMax, IsTurnToWindDir, ASPlaySpeedMinWindPower, ASPlaySpeedMaxWindPower, TurnRate, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.StartFrameRange = StartFrameRange
		self.ASPlaySpeedMin = ASPlaySpeedMin
		self.ASPlaySpeedMax = ASPlaySpeedMax
		self.IsTurnToWindDir = IsTurnToWindDir
		self.ASPlaySpeedMinWindPower = ASPlaySpeedMinWindPower
		self.ASPlaySpeedMaxWindPower = ASPlaySpeedMaxWindPower
		self.TurnRate = TurnRate


class WizzrobeChanceTime:

	def __init__(self, Name, ASName, DefaultCounter, DamageCounter, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.DefaultCounter = DefaultCounter
		self.DamageCounter = DamageCounter
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WizzrobeSummon:

	def __init__(self, Name, SummonBufferKey, SummonBufferSize, WeaponIndex, RotSpd, IgniteOffset, IgniteVelocityDir, IgniteSpeed, IgniteRotate, IgniteRotSpeed, ASName, IsIgnoreSame, PosReduceRatio, AngReduceRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.SummonBufferKey = SummonBufferKey
		self.SummonBufferSize = SummonBufferSize
		self.WeaponIndex = WeaponIndex
		self.RotSpd = RotSpd
		self.IgniteOffset = IgniteOffset
		self.IgniteVelocityDir = IgniteVelocityDir
		self.IgniteSpeed = IgniteSpeed
		self.IgniteRotate = IgniteRotate
		self.IgniteRotSpeed = IgniteRotSpeed
		self.ASName = ASName
		self.IsIgnoreSame = IsIgnoreSame
		self.PosReduceRatio = PosReduceRatio
		self.AngReduceRatio = AngReduceRatio


class WizzrobeTurn:

	def __init__(self, Name, IsWaitASFinish, SucEndWithASFinish, ASKeyName, IsIgnoreSameAS, RotSpd, FinRotate, IsFollowGround, PosReduceRatio, BaseRotRatio, IsChangeable, RotMinSpeedRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsWaitASFinish = IsWaitASFinish
		self.SucEndWithASFinish = SucEndWithASFinish
		self.ASKeyName = ASKeyName
		self.IsIgnoreSameAS = IsIgnoreSameAS
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.IsFollowGround = IsFollowGround
		self.PosReduceRatio = PosReduceRatio
		self.BaseRotRatio = BaseRotRatio
		self.IsChangeable = IsChangeable
		self.RotMinSpeedRatio = RotMinSpeedRatio


class WizzrobeVisibleWalk:

	def __init__(self, Name, IsCheckAnmSeqCancel, AddTargetDist, FailMoveTimer, IsNoBrake, ASName, XZSpeed, RotSpd, FinRotate, HorizontalFinRadius, VerticalFinLength, TargetHeightOffset, RotRatio, RiseSpeed, DownSpeed, IsOverRise, CheckStopSpeed, IsSlowDownNearGoal, VibrateMemoryStep, VibrateCheckFrame, VibrateStopCheck, FlyHeightMin, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.IsCheckAnmSeqCancel = IsCheckAnmSeqCancel
		self.AddTargetDist = AddTargetDist
		self.FailMoveTimer = FailMoveTimer
		self.IsNoBrake = IsNoBrake
		self.ASName = ASName
		self.XZSpeed = XZSpeed
		self.RotSpd = RotSpd
		self.FinRotate = FinRotate
		self.HorizontalFinRadius = HorizontalFinRadius
		self.VerticalFinLength = VerticalFinLength
		self.TargetHeightOffset = TargetHeightOffset
		self.RotRatio = RotRatio
		self.RiseSpeed = RiseSpeed
		self.DownSpeed = DownSpeed
		self.IsOverRise = IsOverRise
		self.CheckStopSpeed = CheckStopSpeed
		self.IsSlowDownNearGoal = IsSlowDownNearGoal
		self.VibrateMemoryStep = VibrateMemoryStep
		self.VibrateCheckFrame = VibrateCheckFrame
		self.VibrateStopCheck = VibrateStopCheck
		self.FlyHeightMin = FlyHeightMin


class WolfLinkAmiiboRegister:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WolfLinkAmiiboWarp:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class WolfLinkEvent:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class XLinkEventCreateAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class XLinkEventEnable:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class XLinkEventFadeAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class XLinkEventKillAction:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ZoraHeroRescuePlayer:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class ZoraHeroWaterFallJump:

	def __init__(self, Name, ASName, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName


class ZoraSurfing:

	def __init__(self, Name, RotRadPerSec, ASName, ASNameJump, WallHitTime, FinRadius, FinHeight, FinRotate, AddCalcStickX, IsClampRotVel, InWaterDepth, FloatDepth, FloatRadius, FloatCycleTime, ChangeDepthSpeed, OnRailDistance, FarDistance, Speed, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.RotRadPerSec = RotRadPerSec
		self.ASName = ASName
		self.ASNameJump = ASNameJump
		self.WallHitTime = WallHitTime
		self.FinRadius = FinRadius
		self.FinHeight = FinHeight
		self.FinRotate = FinRotate
		self.AddCalcStickX = AddCalcStickX
		self.IsClampRotVel = IsClampRotVel
		self.InWaterDepth = InWaterDepth
		self.FloatDepth = FloatDepth
		self.FloatRadius = FloatRadius
		self.FloatCycleTime = FloatCycleTime
		self.ChangeDepthSpeed = ChangeDepthSpeed
		self.OnRailDistance = OnRailDistance
		self.FarDistance = FarDistance
		self.Speed = Speed


class forceSetCameraPos:

	def __init__(self, Name, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None


class inWaterSelForkASPlay:

	def __init__(self, Name, ASName, EndState, ChangeableTiming, IsIgnoreSame, SeqBank, TargetBone, FirstRandomRatio, Behaviors = None, DemoAIAction = False):
		self.Name = Name
		self.Behaviors = Behaviors
		self.DemoAIAction = DemoAIAction
		self.RelativeId = -1
		self.AbsoluteId = -1
		self.Parent = None
		self.ASName = ASName
		self.EndState = EndState
		self.ChangeableTiming = ChangeableTiming
		self.IsIgnoreSame = IsIgnoreSame
		self.SeqBank = SeqBank
		self.TargetBone = TargetBone
		self.FirstRandomRatio = FirstRandomRatio


