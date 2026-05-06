# 🤖 Mini-Projet 3 : Autonomous Drive Robot (Jazzy Edition)

Projet de robotique mobile différentielle avec navigation autonome complète.

## ⚙️ Stack Technique
- **Hardware Simulation**: URDF/Xacro, Gazebo
- **Control**: ros2_control (DiffDriveController)
- **Perception**: LiDAR 360°, Caméra RGB
- **Navigation**: Nav2 (SLAM Toolbox & BT Navigator)

## 🏗️ Structure Modulaire
- `urdf/`: Décomposition en `robot_core`, `lidar`, et `ros2_control`.
- `config/`: Paramètres YAML pour les contrôleurs et Nav2.
- `scripts/`: Planificateur de mission asynchrone pour waypoints.

## 🚀 Démarrage Rapide
```bash
colcon build --packages-select miniproject_3_autonomous_drive_robot
source install/setup.bash

# 1. Lancer le robot et Gazebo
ros2 launch miniproject_3_autonomous_drive_robot launch_sim.launch.py

# 2. Lancer le SLAM
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True

# 3. Lancer la Navigation
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
```

---
**Maria Lagab** - *Spécialité Robotique et Système Intelligent*
