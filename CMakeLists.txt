cmake_minimum_required(VERSION 3.8)
project(miniproject_3_autonomous_drive_robot)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch maps rviz scripts urdf worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
