cmake_minimum_required(VERSION 2.8.3)
project(string_to_twist)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  std_msgs
  rospy
)

catkin_python_setup()
catkin_package()
