#!/bin/bash

source ~/ros_catkin_ws/install_isolated/setup.bash
source /opt/ros/foxy/setup.bash
rosparam load ~/workspace/indoor-nav-system/bridge/config.yml
ros2 run ros1_bridge parameter_bridge
