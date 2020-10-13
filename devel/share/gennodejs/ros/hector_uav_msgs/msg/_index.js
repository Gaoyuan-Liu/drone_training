
"use strict";

let AttitudeCommand = require('./AttitudeCommand.js');
let Supply = require('./Supply.js');
let ThrustCommand = require('./ThrustCommand.js');
let RuddersCommand = require('./RuddersCommand.js');
let ServoCommand = require('./ServoCommand.js');
let RawRC = require('./RawRC.js');
let Compass = require('./Compass.js');
let ControllerState = require('./ControllerState.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let MotorPWM = require('./MotorPWM.js');
let Altimeter = require('./Altimeter.js');
let MotorCommand = require('./MotorCommand.js');
let HeadingCommand = require('./HeadingCommand.js');
let MotorStatus = require('./MotorStatus.js');
let RC = require('./RC.js');
let YawrateCommand = require('./YawrateCommand.js');
let HeightCommand = require('./HeightCommand.js');
let RawImu = require('./RawImu.js');
let RawMagnetic = require('./RawMagnetic.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let LandingActionFeedback = require('./LandingActionFeedback.js');
let PoseFeedback = require('./PoseFeedback.js');
let PoseGoal = require('./PoseGoal.js');
let LandingGoal = require('./LandingGoal.js');
let LandingFeedback = require('./LandingFeedback.js');
let TakeoffAction = require('./TakeoffAction.js');
let PoseActionResult = require('./PoseActionResult.js');
let LandingAction = require('./LandingAction.js');
let TakeoffActionGoal = require('./TakeoffActionGoal.js');
let TakeoffResult = require('./TakeoffResult.js');
let PoseAction = require('./PoseAction.js');
let TakeoffGoal = require('./TakeoffGoal.js');
let TakeoffActionResult = require('./TakeoffActionResult.js');
let LandingResult = require('./LandingResult.js');
let TakeoffFeedback = require('./TakeoffFeedback.js');
let PoseActionFeedback = require('./PoseActionFeedback.js');
let PoseActionGoal = require('./PoseActionGoal.js');
let TakeoffActionFeedback = require('./TakeoffActionFeedback.js');
let PoseResult = require('./PoseResult.js');
let LandingActionResult = require('./LandingActionResult.js');
let LandingActionGoal = require('./LandingActionGoal.js');

module.exports = {
  AttitudeCommand: AttitudeCommand,
  Supply: Supply,
  ThrustCommand: ThrustCommand,
  RuddersCommand: RuddersCommand,
  ServoCommand: ServoCommand,
  RawRC: RawRC,
  Compass: Compass,
  ControllerState: ControllerState,
  VelocityZCommand: VelocityZCommand,
  VelocityXYCommand: VelocityXYCommand,
  MotorPWM: MotorPWM,
  Altimeter: Altimeter,
  MotorCommand: MotorCommand,
  HeadingCommand: HeadingCommand,
  MotorStatus: MotorStatus,
  RC: RC,
  YawrateCommand: YawrateCommand,
  HeightCommand: HeightCommand,
  RawImu: RawImu,
  RawMagnetic: RawMagnetic,
  PositionXYCommand: PositionXYCommand,
  LandingActionFeedback: LandingActionFeedback,
  PoseFeedback: PoseFeedback,
  PoseGoal: PoseGoal,
  LandingGoal: LandingGoal,
  LandingFeedback: LandingFeedback,
  TakeoffAction: TakeoffAction,
  PoseActionResult: PoseActionResult,
  LandingAction: LandingAction,
  TakeoffActionGoal: TakeoffActionGoal,
  TakeoffResult: TakeoffResult,
  PoseAction: PoseAction,
  TakeoffGoal: TakeoffGoal,
  TakeoffActionResult: TakeoffActionResult,
  LandingResult: LandingResult,
  TakeoffFeedback: TakeoffFeedback,
  PoseActionFeedback: PoseActionFeedback,
  PoseActionGoal: PoseActionGoal,
  TakeoffActionFeedback: TakeoffActionFeedback,
  PoseResult: PoseResult,
  LandingActionResult: LandingActionResult,
  LandingActionGoal: LandingActionGoal,
};
