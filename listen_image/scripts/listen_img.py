#!/usr/bin/env python
import rospy
import sensor_msgs.msg

def processImage(msg): 
    global image_pub
    w = msg.width
    h = msg.height

    print 'width : ' + str(w) + '\theight : ' + str(h)


if __name__ == '__main__':
    global image_pub
    rospy.init_node('listen_img')
    
#    image_pub = rospy.Publisher("new_image",sensor_msgs.msg.Image)
    image_sub = rospy.Subscriber("image",sensor_msgs.msg.Image, processImage)
    rospy.loginfo('initialized')

    rospy.spin()
