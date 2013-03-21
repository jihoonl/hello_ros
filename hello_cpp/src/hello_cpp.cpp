/*
   Hello CPP
 */
#include<ros/ros.h>

int main(int argc,char** argv)
{
  ros::init(argc,argv,"hello_cpp"); // Registering a node in ros master
  ROS_INFO("Welcome to ROS!");
  return 0;
}
