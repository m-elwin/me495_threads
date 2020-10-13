cmake_minimum_required(VERSION 3.0.8)
project(me495_threads)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)


catkin_python_setup()

add_message_files(
  FILES
  TestIntArray.msg
)
  
generate_messages(
   DEPENDENCIES
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES me495_threads
  CATKIN_DEPENDS std_msgs message_runtime
#  DEPENDS system_lib
)


catkin_install_python(PROGRAMS
  nodes/sub_thread
  nodes/node_square
  nodes/timers
  nodes/time_square
  nodes/throughput
  scripts/gil_two_threads.py
  scripts/race_cond.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

