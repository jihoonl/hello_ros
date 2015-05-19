#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
import sensor_msgs.msg


def process_image(msg): 
    global image_pub

    br = cv_bridge.CvBridge()
    cv_img = br.imgmsg_to_cv2(msg)
    gray_cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    gray_imgmsg = br.cv2_to_imgmsg(gray_cv_img)

    image_pub.publish(gray_imgmsg)

if __name__ == '__main__':
    global image_pub
    rospy.init_node('listen_img')
    
    image_pub = rospy.Publisher("new_image",sensor_msgs.msg.Image)
    image_sub = rospy.Subscriber("image",sensor_msgs.msg.Image, processImage)
    rospy.loginfo('initialized')

    rospy.spin()
