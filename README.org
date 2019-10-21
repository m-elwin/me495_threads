#+TITLE: ROS Thread Exploration
#+AUTHOR: Matthew Elwin

* Overview
Provides some code to help explore threads in python and ROS.
You should examine the examples, run them, and right your own code to further your understand
threads in python.

* Provided code
1. =scripts/gil_two_threads.py= - Non-ROS python script that
   demonstrates the effect of the GIL on multi-threaded python code. 
2. =scripts/git_io.py= - Demonstration of multi-threaded code with input/output
3. =nodes/sub_thread= - Subscribes to a topic and sleeps for a specified period of time.
   Also prints diagnostic information.  In conjunction with publishers that publish
   at different rates, you can begin to explore the nuances of subscriber threads.
4. =nodes/timers= - Starts two timers and prints diagnostic information


* Questions
