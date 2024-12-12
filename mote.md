

ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 odom base_link

ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/apper_params_online_async.yaml

ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/apper_params_online_async.yaml use_sim_time:=false
# To generate map
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/mapper_params_online_async.yaml use_sim_time:=false

ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/online_async_local.yaml use_sim_time:=false

rosrun teleop_twist_keyboard teleop_twist_keyboard.py _speed:=0.1 _turn:=0.2


Run map server
ros2 run nav2_map_server map_server --ros-args -p yaml_file_name:=map_1016.yaml -p use_sim_time:=false
ros2 run nav2_map_server map_server --ros-args -p yaml_file_name:=smap_11011.yaml -p use_sim_time:=false


ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false


#sudo useradd -m smremote -s /bin/bash


ros2 launch nav2_bringup localization_launch.py map:=./maps/20241211/m1.yaml use_sim_time:=false
ros2 launch my_robot_description localization_launch.py map:=./maps/20241211/m1.yaml use_sim_time:=fals


ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false map_subscribe_transient_local:=true


