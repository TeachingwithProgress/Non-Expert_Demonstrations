#!/usr/bin/env python
import rospy
import rosbag
from kortex_driver.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from kortex_driver.srv import *
import time
import numpy as np
class ArmReplayer:
    def __init__(self, folder_name = None):
        self.path = 'path_to_your_bag_files'
        if folder_name is not None:
            self.path = 'path_to_bag' + folder_name + '/'
        self.cnt = 0
        bag_name = self.path + str(self.cnt) + '.bag'
        #self.bag = rosbag.Bag(bag_name, 'r')
        
        self.joint_trajectory = ConstrainedJointAngles()
        self.arm = kortex_arm.Arm()
        self.arm.home_arm()
        self.arm.open_gripper()
        self.msg = []

    def read_bag(self, cnt=None):
        if cnt is None:
            cnt = self.cnt
        self.bag = rosbag.Bag(self.path + str(cnt) + ".bag", 'r')
        self.msg = []
        for topic, msg, t in self.bag.read_messages(topics=['/my_gen3_lite/joint_states']):
            temp = JointState()
            temp.header = msg.header
            temp.position = msg.position
            temp.velocity = msg.velocity
            temp.name = msg.name
            temp.effort = msg.effort
    
            self.msg.append(temp)

        # print((self.msg))
        return self.msg

        return poses
    def close_bag(self):
        self.bag.close()

if __name__ == '__main__':
    jar = []
    rospy.init_node('arm_replayer', anonymous=True)
    #folder = input('Please input the folder name: ')
    for i in range(0, 40):
        folder = "user_" + str(i)
        replayer = ArmReplayer(folder)

        bag = 0
        replayer.read_bag(bag)
        replayer.close_bag()

