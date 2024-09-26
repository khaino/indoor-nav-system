#!/bin/bash

source /opt/ros/foxy/setup.bash
cd ../../lidar && source install/setup.bash
ros2 launch rslidar_sdk start.py
