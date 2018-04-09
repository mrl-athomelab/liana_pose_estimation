cmake_minimum_required(VERSION 2.8.3)
project(liana_pose_estimation)

find_package(catkin REQUIRED COMPONENTS
   rospy
   std_msgs
   sensor_msgs
   message_generation
)

add_service_files(
  FILES
  PoseEstimator.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package()