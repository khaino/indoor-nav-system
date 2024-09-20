source ~/ros_catkin_ws/install_isolated/setup.bash
source ~/catkin_ws/devel/setup.bash
rosrun scout_bringup bringup_can2usb.bash
roslaunch scout_bringup scout_robot_base.launch 