cmake_minimum_required(VERSION 3.0.8)
project(me495_threads)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)


catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES me495_threads
  CATKIN_DEPENDS std_msgs
#  DEPENDS system_lib
)


catkin_install_python(PROGRAMS
  nodes/sub_thread
  nodes/node_square
  nodes/timers
  nodes/time_square
  scripts/gil_two_threads.py
  scripts/race_cond.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

