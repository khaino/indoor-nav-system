sudo apt install ros-foxy-navigation2
sudo apt install ros-foxy-turtlebot3*
sudo apt install ros-foxy-nav2-bringup


ros2 launch my_robot_description scout_mini_display.launch.xml


ros2 launch nav2_bringup navigation_launch.py
ros2 run slam_toolbox sync_slam_toolbox_node --ros-args --remap /scan:=/scanner/scan