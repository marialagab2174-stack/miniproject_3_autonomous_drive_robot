import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    package_name = 'miniproject_3_autonomous_drive_robot'
    xacro_file = os.path.join(get_package_share_directory(package_name),'urdf','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description_config.toxml(), 'use_sim_time': True}]
        )
    ])
