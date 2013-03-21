hello_ros
=========

Hello world in ros

It is a minimum example to show how to compile in catkin. The example contains how to create

- cpp package
- python package

and how to generate

- msg
- srv
- action


## How To ##

Assumes that up-to-date ROS(>=groovy) is installed. If not please, visit installation page.(http://www.ros.org/wiki/ROS/Installation)

### Create workspace directory

<pre>
> mkdir ros
> cd ros
> mkdir src
> cd src
> catkin_init_workspace
</pre>

If catkin_init_workspace command is not available, please do

> source /opt/ros/<YOUR ROS RELEASE VERSION>/setup.bash

### Download source file

<pre>
> cd ros/src
> git clone https://github.com/jihoonl/hello_ros.git
</pre>

### Compile

<pre>
> cd ros
> catkin_make
</pre>

After catkin_make, 'build' and 'devel' directories are created.

### Execution

Assumes that roscore is already running...
 
#### Execute hello_cpp
<pre>
> cd ros/devel
> source setup.bash
> rosrun hello_cpp hello_cpp
</pre>

#### Execute hello_python
<pre>
> cd ros/devel
> source setup.bash
> rosrun hello_python hello_python.py
</pre>

