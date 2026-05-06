#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class AdvancedAutonomous(Node):
    def __init__(self):
        super().__init__('advanced_autonomous_node')
        self.publisher_ = self.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.safe_distance = 0.8

    def scan_callback(self, msg):
        # On divise le scan en 3 zones : Gauche, Centre, Droite
        half_len = len(msg.ranges) // 2
        center_range = msg.ranges[half_len-30 : half_len+30]
        min_front = min(center_range)

        cmd = Twist()
        if min_front < self.safe_distance:
            self.get_logger().warn(f'⚠️ Obstacle détecté à {min_front:.2f}m')
            cmd.linear.x = 0.0
            cmd.angular.z = 0.6  # Rotation pour trouver un chemin
        else:
            cmd.linear.x = 0.4
            cmd.angular.z = 0.0
        
        self.publisher_.publish(cmd)

def main():
    rclpy.init()
    node = AdvancedAutonomous()
    rclpy.spin(node)
