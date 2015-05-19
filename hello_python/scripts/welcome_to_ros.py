#!/usr/bin/env python
"""
    Hello Python!
"""
import rospy

if __name__== "__main__":
    rospy.init_node('hello_python') # Resgistering node in ros master
    rospy.loginfo('Welcome to ROS')
