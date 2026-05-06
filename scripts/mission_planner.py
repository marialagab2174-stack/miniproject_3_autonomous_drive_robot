#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped

class MissionPlanner(Node):
    def __init__(self):
        super().__init__('mission_planner')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.waypoints = [
            (2.0, 1.0, 0.0),  # x, y, theta
            (4.0, -1.0, 1.57),
            (0.0, 0.0, 0.0)
        ]
        self.get_logger().info('Mission Planner démarré. Prêt à envoyer les waypoints.')

    def send_goal(self, x, y, theta):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.z = theta
        
        self._action_client.wait_for_server()
        self.get_logger().info(f'Navigation vers x: {x}, y: {y}')
        return self._action_client.send_goal_async(goal_msg)

def main():
    rclpy.init()
    planner = MissionPlanner()
    # Envoi du premier waypoint de test
    planner.send_goal(2.0, 1.0, 0.0)
    rclpy.spin(planner)

if __name__ == '__main__':
    main()
