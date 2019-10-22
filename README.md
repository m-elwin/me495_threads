# Overview
Provides some code to help explore threads in python and ROS.
You should examine the examples, run them, and right your own code to further your understand
threads in python.

# Provided code
1. `scripts/gil_two_threads.py` - Non-ROS python script that
   demonstrates the effect of the GIL on multi-threaded python code. 
3. `nodes/node_square` - Performs same computation in gil_two_threads but distributed across multiple nodes
4. `nodes/time_square` - Times the computation of node_square
5. `launch/node_two_square.launch` - launches the nodes used by the node_two_threads example
3. `nodes/sub_thread` - Subscribes to a topic and sleeps for a specified period of time.
   Also prints diagnostic information.  In conjunction with publishers that publish
   at different rates, you can begin to explore the nuances of subscriber threads.
4. `nodes/timers` - Starts two timers and prints diagnostic information

# Questions
Use the provided code, code you write, and standard ROS tools to answer the following questions.
YOu can directly edit this document and then push to your assignment. If you wrote any new code, indicate
the files that you created in your answer.  If you ran some commands, record those, being sure to backticks to format 
the commands as source code.

1. Run `scripts/gil_two_threads.py`.  Why does is the version that uses two threads not roughly twice
   as fast as the version that uses a single thread?
2. Launch `gil_free.launch`. This launches two nodes that perform the same computations as
   `scripts/gil_two_threads.py` and prints the time it took to complete. In most circumstances, the computation should
    be faster than either method in `gil_two_threads.py` (note: you will have to add the times together to get the total time).
    Why?  What circumstances could lead this method to have a similar runtime to `scripts/gil_two_threads.py`.
3. Run `scripts/race_cond.py` a few times.  Does it return consistent results?
4. Use a mutex ([[https://docs.python.org/2/library/threading.html#lock-objects][called a Lock in python]] to
   fix the race condition in scripts/race_cond.py. The variable =total= should count precisely the
   total number of iterations of the loop in both threads, every time you run the code.
   - Note, you can use `with lock:` to automatically acquire a lock at the beginning of the block
     and release it when the block ends, either normally or due to an exception being thrown.

5. Run `nodes/timers`.  After observing the behavior and seeing the output, what can you infer about
   threads and timers?
6. What does `rospy.spin` do?  You can infer a bit by commenting it out and by replacing it
   with an infinite while loop.  Also feel free to look at the source code to answer this.
7. Are `main`, `callback1` and `callback2` executed on the same thread or on different threads?
8. Run `sub_thread` and publish to the `sleep` topic.  Is the sleeper subscriber running on the same thread as the main code?
9. By manipulating the frequency at which you publish to `sleep` and the time you have the subscriber delay you can infer
   information about ROS's threading system. Write a node called `pub_thread` that uses a `rospy.Timer` to publish a message to `sub_thread` at
   a 1 Hz.  The node should count how many messages it publishes and print out an updated count after every time it publishes.
   - Describe the behavior that you see when the delay time sent by `pub_thread` is shorter than 1 second
   - What happens when you increase the delay time sent by `pub_thread` to 2 seconds?
     - Does one subscriber callback complete before the next one is started?
     - After waiting for a few seconds, kill `pub_thread` but keep `sub_thread` running.  What happens with `sub_thread`?
10. Run two instances of the `pub_thread` node.  What is the relationship between subscriber threads
   and publishers?
    
