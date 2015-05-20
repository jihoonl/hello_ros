#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
import sensor_msgs.msg

def process_image(msg): 
    global image_pub
    global br

    cv_img = br.imgmsg_to_cv2(msg) # Convert to opencv format using cv_bridge
    gray_cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) # Grayscale
    gray_imgmsg = br.cv2_to_imgmsg(gray_cv_img, "mono8") # Convert back to ros image msg

    image_pub.publish(gray_imgmsg) # Publish

if __name__ == '__main__':
    global image_pub
    global br

    rospy.init_node('listen_img') # Initialise
    
    br = cv_bridge.CvBridge() # Instantiate CV Bridge
    image_pub = rospy.Publisher("new_image",sensor_msgs.msg.Image, queue_size=1) # publisher
    image_sub = rospy.Subscriber("image",sensor_msgs.msg.Image, process_image) # Subscriber 
    rospy.loginfo('initialized')

    rospy.spin() # Wait for Ctrl-C
