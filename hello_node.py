#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node('hello_py_node')
    rospy.loginfo("Hello, World from ROS Python!")