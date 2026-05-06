# 🚀 Autonomous Drive Robot - Master Edition (ROS 2 Jazzy)

Ce projet implante un système complet de navigation autonome pour un robot différentiel, intégrant la fusion de capteurs et une pile de navigation avancée.

## 🛠 Architecture & Stack Technique

### 1. Modélisation (URDF/Xacro)
- **Châssis** : Base rectangulaire optimisée pour la stabilité.
- **Actuateurs** : 2 roues motrices (Diff Drive) + 1 roue caster (friction réduite pour Gazebo).
- **Capteurs** : 
  - **LiDAR 360°** (RP Lidar A1 simulé) pour la cartographie.
  - **IMU 6-axes** pour la détection d'orientation et d'accélération.
  - **Caméra RGB** pour le retour visuel.

### 2. Estimation d'état (Sensor Fusion)
- **EKF (Extended Kalman Filter)** : Fusion des données `/odom` (encodeurs) et `/imu` via le package `robot_localization` pour une estimation de position ultra-précise.

### 3. Navigation & SLAM
- **SLAM** : Utilisation de `Slam Toolbox` en mode asynchrone pour la génération de carte temps réel.
- **Nav2 Stack** :
  - **Smac Planner** : Génération de trajectoires fluides et cinématiquement réalisables.
  - **Inflation Layers** : Couches de coût configurées pour maintenir une distance de sécurité de 0.55m des obstacles.
  - **Recovery Behaviors** : Protocoles de dégagement automatique en cas de blocage.

## 📂 Structure du Projet
- `urdf/` : Fichiers Xacro modulaires (core, lidar, imu, camera, ros2_control).
- `config/` : Paramètres YAML (`nav2`, `ekf`, `controllers`).
- `scripts/` : Node Python d'autonomie réactive (`autonomous_drive.py`).
- `launch/` : Scripts de lancement orchestrant la simulation et le traitement.

## 🚀 Guide d'utilisation

### Installation
```bash
cd ~/ros2_ws
colcon build --packages-select miniproject_3_autonomous_drive_robot
source install/setup.bash
```

### Lancement de la Simulation & Navigation
1. **Démarrer le robot dans Gazebo** :
   ```bash
   ros2 launch miniproject_3_autonomous_drive_robot launch_sim.launch.py
   ```
2. **Lancer la Navigation Avancée** :
   ```bash
   ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
   ```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Machine :** Dell Latitude 7400 | Ubuntu 24.04 LTS
