

ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 odom base_link

ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/apper_params_online_async.yaml

ros2 launch slam_toolbox online_async_launch.py params_file:=./src/my_robot_description/config/apper_params_online_async.yaml use_sim_time:=false