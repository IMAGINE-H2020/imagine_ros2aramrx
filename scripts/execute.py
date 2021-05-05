#!/usr/bin/env python
import yaml
import os
import rospkg
import sys

from typing import Dict

import rospy
from imagine_common.msg import Affordance, AscPair, ActionParameters
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool


class ActionSequence(object):
#    def __init__(device: str = 'hdd1'):
    def __init__(self, device):
        self.pub = rospy.Publisher('/kit_gripper/action', Affordance, queue_size=1)
        rospy.init_node('ArmarXAction', anonymous=True)
        self.rate = rospy.Rate(1)
        self.sub = rospy.Subscriber('/kit_gripper/task_status', Bool, self.action_status_update)
        self.action_completed = False

        rospack = rospkg.RosPack()
        root_path = rospack.get_path('ros2armarx')
        path = os.path.join(root_path, 'config', '{}.yaml'.format(device))
        print(path)
        self.data = yaml.load(open(path), yaml.Loader)
        print(self.data['description'])

#    def action_status_update(self, msg: Bool):
    def action_status_update(self, msg):
        self.action_completed = msg.data

#    def create_affordance(self, data: Dict) -> Affordance:
    def create_affordance(self, data):
        aff = Affordance()
        ap = ActionParameters()
        print(data)

        aff.affordance_name = data['affordance_name']
        for asc_dict in data['asc']:
            ap.parameters.append(self.create_asc(asc_dict))

        aff.action_parameters_array.append(ap)
        return aff

#    def create_asc(self, data: Dict):
    def create_asc(self, data):
        asc = AscPair()
        asc.key = data['key']
        asc.value_type = data['value_type']
        if asc.value_type == 0:
            asc.value_str = data['value_str']
        elif asc.value_type == 1:
            asc.value_double = data['value_double']
        elif asc.value_type == 2:
            asc.value_pose = self.get_pose_from_dict(data['value_pose'])
        return asc

#    def get_pose_from_dict(self, data: Dict):
    def get_pose_from_dict(self, data):
        target = Pose()
        target.position.x = data['x']
        target.position.y = data['y']
        target.position.z = data['z']
        target.orientation.w = data['qw']
        target.orientation.x = data['qx']
        target.orientation.y = data['qy']
        target.orientation.z = data['qz']
        return target

#    def send_action_to_armarx(self, aff: Affordance):
    def send_action_to_armarx(self, aff):
        for i in range(3):
            if not rospy.is_shutdown():
                test = "sending action: {}".format(aff.affordance_name)
                rospy.loginfo(test)
                self.pub.publish(aff)
                self.rate.sleep()

    def run(self):
        for action in self.data['sequence']:
            self.send_action_to_armarx(self.create_affordance(action))
            while (not rospy.is_shutdown() and not self.action_completed):
                self.rate.sleep()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("please specify the configuration file name")
    try:
        act = ActionSequence(sys.argv[1])
        act.run()
    except rospy.ROSInterruptException:
        pass


# rosrun ros2armarx execute.py



