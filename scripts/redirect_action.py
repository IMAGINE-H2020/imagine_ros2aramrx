#!/usr/bin/env python
# license removed for brevity
import rospy
from imagine_common.msg import Affordance, AscPair, ActionParameters
from geometry_msgs.msg import Pose

class RedirectAction:
    def __init__():
        self.sub = rospy.Subscriber('/kit_gripper/action')
        self.pub = rospy.Publisher('/kit_gripper/redirected_action', Affordance, queue_size=1)
        self.clock_sub = rospy.Subscriber('clock', Clock, self.clock_callback)
        toolIndex
        aff = Affordance()
        target = Pose()
        target.position.x = 0.2
        target.position.y = 0.3
        target.position.z = 0.4
        target.orientation.w = 0.7070
        target.orientation.x = 0.7070
        target.orientation.y = 0.0
        target.orientation.z = 0.0

        asc = AscPair()
        asc.value_pose = target
        asc.value_double = 125.0
        ap = ActionParameters()
        ap.parameters.append(asc)
        aff.affordance_name = "SuckingAction"
        aff.action_parameters_array.append(ap)

    def action_callback(self, clock):
            print clock

        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
            test = "test ros2armarx action %s" % rospy.get_time()
            rospy.loginfo(test)
            pub.publish(aff)
            rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('redirect_action', anonymous=False)
        redirect_action = RedirectAction()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
