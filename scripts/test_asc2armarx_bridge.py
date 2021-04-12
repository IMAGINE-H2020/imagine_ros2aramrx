#!/usr/bin/env python
import sys
# license removed for brevity
import rospy
import keyboard
from imagine_common.msg import Affordance, AscPair, ActionParameters
from geometry_msgs.msg import Pose

def talker(action):
    print("Triggering action {}".format(action))
    pub = rospy.Publisher('/kit_gripper/action', Affordance, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    aff = Affordance()
    ap = ActionParameters()
    target = Pose()


    if action == "SuckingAction":
        aff.affordance_name = "SuckingAction"

        asc = AscPair()
        asc.key = "SuckingPose"             # Param <"SuckingPose">
        asc.value_type = 2                  # Param <2>
        target.position.x = 0.260           # Param pose, translation: in meters; orientation: as quaternion
        target.position.y = 0.030
        target.position.z = 0.006
        target.orientation.w = 0.70572561025619507
        target.orientation.x = 0.70672500133514404
        target.orientation.y = 0.04416978731751442
        target.orientation.z = -0.023254597559571266
        asc.value_pose = target

        asc1 = AscPair()
        asc1.key = "SuckingPower"           # Param <"SuckingPower">
        asc1.value_type = 1                 # Param <1>
        asc1.value_double = 5.0             # Param float value > 0

        ap.parameters.append(asc)
        ap.parameters.append(asc1)


    elif action == "TeachInAction":
        aff.affordance_name = "TeachInAction"

        asc = AscPair()
        asc.key = "AdesName"                # Param <"TeachInAction">
        asc.value_type = 0                  # Param <0>
        asc.value_str = ""                  # Param defualt <"KinestheticTeaching">

        asc1 = AscPair()
        asc.key = "KinematicChainName"      # Param <"KinematicChainName">
        asc.value_type = 0                  # Param <0>
        asc.value_str = ""                  # Param default <"KIT_Gripper_Arm_With_PG">

        asc2 = AscPair()
        asc.key = "RefFrameName"            # Param <"RefFrameName">
        asc.value_type = 0                  # Param <0>
        asc.value_str = ""                  # Param <"KIT_Gripper_PG_Base">

        ap.parameters.append(asc)
        ap.parameters.append(asc1)
        ap.parameters.append(asc2)

    elif action == "UnscrewingAction":
        aff.affordance_name = "UnscrewingAction"

        asc = AscPair()
        asc.key = "ScrewPose"               # Param <"ScrewPose">
        asc.value_type = 2                  # Param <2>
        target.position.x = 0.296           # Param pose, translation: in meters; orientation (defualt): as quaternion
        target.position.y = 0.008
        target.position.z = 0.014
        target.orientation.w = 1
        target.orientation.x = 0
        target.orientation.y = 0
        target.orientation.z = 0

        asc.value_pose = target

        asc1 = AscPair()
        asc1.key = "ScrewDir"               # Param <"ScrewDir">
        asc1.value_type = 1                 # Param <1>
        asc1.value_double = 0               # Param float value <0> for unscrew, <1> for screw

        ap.parameters.append(asc)
        ap.parameters.append(asc1)

    elif action == "MoveArmToPoseAction":
        aff.affordance_name = "MoveArmToPoseAction"

        asc = AscPair()
        asc.key = "PoseName"                # Param <"PoseName">
        asc.value_type = 0                  # Param <0>
        asc.value_str = "PerceptionPose"    # Param <choose from the valid Pose name list>
                                            # ["PerceptionPose", "ReadyPose", "HomePose", "DropPose, etc."]

        asc1 = AscPair()
        asc1.key = "TimeDuration"           # Param <"TimeDuration">
        asc1.value_type = 1                 # Param <1>
        asc1.value_double = 1.0             # Param double value > 0

        ap.parameters.append(asc)
        ap.parameters.append(asc1)

    elif action == "SwitchToolAction":
        aff.affordance_name = "SwitchToolAction"

        asc = AscPair()
        asc.key = "ToolIndex"               # Param <"ToolIndex">
        asc.value_type = 0                  # Param <0>
        asc.value_str = "-1"                 # Param <choose from the valid tool list>

        ap.parameters.append(asc)

    elif action == "RotatingBaseAction":
        aff.affordance_name = "RotatingBaseAction"

        asc = AscPair()
        asc.key = "FlipAngle"               # Param <"FlipAngle">
        asc.value_type = 1                  # Param <1> for double value
        asc.value_double = -90              # Param <-90> for upside down

        ap.parameters.append(asc)

    elif action == "FlippingAction":
        aff.affordance_name = "FlippingAction"

        asc = AscPair()

        ap.parameters.append(asc)

    elif action == "ShakingAction":
        aff.affordance_name = "ShakingAction"

        asc = AscPair()
        asc.key = "FlipAngle"               # Param <"FlipAngle">
        asc.value_type = 1                  # Param <1> for double value
        asc.value_double = -90              # Param <-90> for upside down

        asc1 = AscPair()
        asc1.key = "ShakeAmplitude"         # Param <"FlipAngle">
        asc1.value_type = 1                 # Param <1> for double value
        asc1.value_double = 10              # Param <-90> for upside down

        asc2 = AscPair()
        asc2.key = "FinalTargetAngleDegrees" # Param <"FlipAngle">
        asc2.value_type = 1                  # Param <1> for double value
        asc2.value_double = 90              # Param <-90> for upside down

        ap.parameters.append(asc)
        ap.parameters.append(asc1)
        ap.parameters.append(asc2)

    elif action == "InitializeRobotAction":
        aff.affordance_name = "InitializeRobotAction"

        asc = AscPair()

        ap.parameters.append(asc)

    elif action == "PickingUpAction":
        aff.affordance_name = "PickingUpAction"

        asc = AscPair()

        ap.parameters.append(asc)

    elif action == "CloseJawAction":
        aff.affordance_name = "CloseJawAction"

        asc = AscPair()

        ap.parameters.append(asc)

    elif action == "OpenJawAction":
        aff.affordance_name = "OpenJawAction"

        asc = AscPair()

        ap.parameters.append(asc)

    elif action == "SwitchPumpAction":
        aff.affordance_name = "SwitchPumpAction"

        asc = AscPair()
        asc.key = "PumpEnableFlag"          # Param <"PumpEnableFlag">
        asc.value_type = 0                  # Param <0> for string value
        asc.value_str = "True"              # Param "True" or "False"

        asc1 = AscPair()
        asc1.key = "ValveReverseFlag"       # Param <"ValveReverseFlag">
        asc1.value_type = 0                 # Param <0> for string value
        asc1.value_str = "False"            # Param "True" or "False"

        ap.parameters.append(asc)
        ap.parameters.append(asc1)

    elif action == "ReversePumpAction":
        aff.affordance_name = "SwitchPumpAction"

        asc = AscPair()
        asc.key = "PumpEnableFlag"          # Param <"PumpEnableFlag">
        asc.value_type = 0                  # Param <0> for string value
        asc.value_str = "True"              # Param "True" or "False"

        asc1 = AscPair()
        asc1.key = "ValveReverseFlag"       # Param <"ValveReverseFlag">
        asc1.value_type = 0                 # Param <0> for string value
        asc1.value_str = "True"            # Param "True" or "False"

        ap.parameters.append(asc)
        ap.parameters.append(asc1)

    elif action == "StopPumpAction":
        aff.affordance_name = "SwitchPumpAction"

        asc = AscPair()
        asc.key = "PumpEnableFlag"          # Param <"PumpEnableFlag">
        asc.value_type = 0                  # Param <0> for string value
        asc.value_str = "False"              # Param "True" or "False"

        asc1 = AscPair()
        asc1.key = "ValveReverseFlag"       # Param <"ValveReverseFlag">
        asc1.value_type = 0                 # Param <0> for string value
        asc1.value_str = "False"            # Param "True" or "False"

        ap.parameters.append(asc)
        ap.parameters.append(asc1)

    elif action == "SwitchLightAction":
        aff.affordance_name = "SwitchLightAction"

        asc = AscPair()
        asc.key = "SwitchFlag"              # Param <"SwitchFlag">
        asc.value_type = 0                  # Param <0> for string value
        asc.value_str = "True"              # Param "True" or "False"

        ap.parameters.append(asc)

    elif action == "TurnOffLightAction":
        aff.affordance_name = "SwitchLightAction"

        asc = AscPair()
        asc.key = "SwitchFlag"              # Param <"SwitchFlag">
        asc.value_type = 0                  # Param <0> for string value
        asc.value_str = "False"              # Param "True" or "False"

        ap.parameters.append(asc)

    elif action == "PushingAction":
        aff.affordance_name = "PushingAction"

        asc = AscPair()
        asc.key = "LeverPose"               # Param <"ScrewPose">
        asc.value_type = 2                  # Param <2>
        target.position.x = 0.212           # Param pose, translation: in meters; orientation (defualt): as quaternion
        target.position.y = 0.119
        target.position.z = 0.031
        target.orientation.w = 0.70023339986801147
        target.orientation.x = 0.69271087646484375
        target.orientation.y = 0.098351821303367615
        target.orientation.z = 0.14195789396762848

        asc.value_pose = target

        ap.parameters.append(asc)

    aff.action_parameters_array.append(ap)

    counter = 0
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        test = "test ros2armarx action %s" % rospy.get_time()
        rospy.loginfo(test)
        pub.publish(aff)
        counter += 1
        if counter == 3:
            return
        rate.sleep()

if __name__ == '__main__':
    action_list = [
    'SuckingAction',
    'TeachInAction',
    'UnscrewingAction',
    'MoveArmToPoseAction',
    'SwitchToolAction',
    'RotatingBaseAction',
    'FlippingAction',
    'ShakingAction',
    'InitializeRobotAction',
    'PickingUpAction',
    'CloseJawAction',
    'OpenJawAction',
    'SwitchPumpAction',
    'ReversePumpAction',
    'StopPumpAction',
    'SwitchLightAction',
    'TurnOffLightAction',
    'PushingAction'
    ]
    instr = 'actions to choose, enter a number in the range [{} - {}]:\n'.format(0, (len(action_list)-1))
    for i, a in enumerate(action_list):
        instr += ( str(i) + '\t' + a + '\n')
    instr += 'leave it empty to exit\n'
    try:
        while True:
            index = raw_input(instr)
            if index and 0 <= int(index) <= len(action_list):
                talker(action_list[int(index)])
            else:
                sys.exit(0)
    except rospy.ROSInterruptException:
        pass
