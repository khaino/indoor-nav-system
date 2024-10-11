#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class OdomToTFBroadcaster(Node):
    FRAME_ID = 'odom'
    CHILD_FRAME_ID = 'base_link'

    def __init__(self):
        super().__init__('odom_to_tf_broadcaster')
        
        self.tf_broadcaster = TransformBroadcaster(self)
        self.subscription = self.create_subscription(Odometry, '/odom', self.handle_odom_message, 10)
        self.get_logger().info("Broadcasting odom to TF tree")

    def handle_odom_message(self, msg):
        # Create a TransformStamped message
        t = TransformStamped()

        # Set header information
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.FRAME_ID  # Parent frame
        t.child_frame_id = self.CHILD_FRAME_ID  # Child frame (modify as needed)

        # Set translation from odometry position
        t.transform.translation.x = msg.pose.pose.position.x
        t.transform.translation.y = msg.pose.pose.position.y
        t.transform.translation.z = msg.pose.pose.position.z

        # Set rotation from odometry orientation
        t.transform.rotation = msg.pose.pose.orientation

        # Send the transform
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = OdomToTFBroadcaster()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__mian__":
    main()