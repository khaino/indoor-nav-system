# build docker
docker build -t roscb .
# command to publish sample ros2 message
ros2 topic pub /bridge_msg std_msgs/String "data: 'Hello, ROS 2'"
# ros-bridge reference
https://github.com/ros2/ros1_bridge#example-4-bridge-only-selected-topics-and-services
