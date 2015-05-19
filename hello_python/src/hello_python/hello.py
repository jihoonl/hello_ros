#
# Hello Python Class to show simple python class 
#
#
import rospy

class HelloPython:
    def __init__(self):
        pass

    def say(self, msg):
        rospy.loginfo(str(msg))
