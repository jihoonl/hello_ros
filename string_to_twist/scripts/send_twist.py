#!/usr/bin/env python
"""
  Sends twist message
"""
import rospy
import string_to_twist

if __name__ == '__main__':
    rospy.init_node('send_twist')

    command_topic = 'command'
    twist_topic = 'cmd_vel'
#    speed = 0.25
    speed = 0.4

    ts = string_to_twist.TwistSender(command_topic, twist_topic, speed)
    rospy.loginfo("Initialised")
    ts.spin()
    rospy.loginfo("Bye Bye")
