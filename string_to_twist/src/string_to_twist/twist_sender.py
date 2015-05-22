import rospy
import std_msgs.msg
import geometry_msgs.msg

class TwistSender:
    def __init__(self, command_topic, twist_topic, speed=0.1):
        self.speed = speed
        self.ang_speed = speed * 2
        self.sub_command = rospy.Subscriber(command_topic, std_msgs.msg.String, self.process_command)
        self.pub_twist = rospy.Publisher(twist_topic, geometry_msgs.msg.Twist, queue_size=1)

        self.twist_msgs = geometry_msgs.msg.Twist()
        self.twist_msgs.linear.x = 0.0
        self.twist_msgs.angular.z = 0.0

    def process_command(self, msg):
        '''
        callback for string command
        '''
        command = msg.data
        rospy.loginfo("Received : %s"%command)

        if command.find("forward") > -1:
            self.twist_msgs.linear.x = self.speed
            self.twist_msgs.angular.z = 0.0
        if command.find("backward") > -1:
            self.twist_msgs.linear.x = -self.speed
            self.twist_msgs.angular.z = 0.0
        elif command.find("left") > -1:
            self.twist_msgs.linear.x = 0.0
            self.twist_msgs.angular.z = self.ang_speed
        elif command.find("right") > -1:
            self.twist_msgs.linear.x = 0.0
            self.twist_msgs.angular.z = -self.ang_speed
        elif command.find("stop") > -1:
            self.twist_msgs.linear.x = 0.0
            self.twist_msgs.angular.z = 0.0

    def spin(self):
        '''
        Runs until it receives user interruption. 
        Sends Twist messsage with 3.0 hz 
        '''
        r = rospy.Rate(3.0)
        while not rospy.is_shutdown():
            self.pub_twist.publish(self.twist_msgs)
            r.sleep()
