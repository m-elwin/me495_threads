# Overview
Provides some code to help explore threads in python and ROS.
You should examine the examples, run them, and write your own code to further your understand
threads in python. At the end there are questions for you to turn in.  You can edit
this file and the code provided directly to give your answers.

# Provided code
1. `scripts/gil_two_threads.py` - Non-ROS python script that
   demonstrates the effect of the GIL on multi-threaded python code. 
2. `nodes/node_square` - Performs same computation in gil_two_threads but distributed across multiple nodes
3. `nodes/time_square` - Times the computation of node_square
4. `launch/node_two_square.launch` - launches the nodes used by the node_two_threads example
5. `nodes/sub_thread` - Subscribes to a topic and sleeps for a specified period of time.
   Also prints diagnostic information.  In conjunction with publishers that publish
   at different rates, you can begin to explore the nuances of subscriber threads.
6. `nodes/timers` - Starts two timers and prints diagnostic information

# Questions
Use the provided code, code you write, and standard ROS tools to answer the following questions.
You can directly edit this document to answer the questions and then push to your assignment.
If you wrote any new code, indicate the files that you created in your answer.
If you ran some commands, record those, being sure to backticks to format 
the commands as source code.  As usual, you should spread out your answers across multiple git commits.
You will likely need to read through the provided code and understand what it does to answer the questions.

1. Run `scripts/gil_two_threads.py` several times. How long did the single and multi-threaded computations take (use the best times among all trials)?
   Is the computation that uses two threads roughly twice as fast as the version that uses a single thread? Why or why not?
2. Launch `node_two_square.launch`. This runs two nodes to perform the same computations as `scripts/gil_two_threads.py`
   and a third node to time the computations.
   - Is this faster than `scripts/gil_two_threads.py`? Why or why not?
   - Under what circumstances would this code outperform `scripts/gil_two_threads.py` and when would it underperform?
     (Hint, think about factors such as number of CPU cores available and setup overhead).
3. Run `scripts/race_cond.py` a few times.  Notice that it does not return consistent results.
   Your task is to use a a mutex ([[https://docs.python.org/2/library/threading.html#lock-objects][(called a Lock in python)]] to
   fix the race condition in `scripts/race_cond.py`. The variable `total` should count precisely the
   total number of iterations of the loop in both threads, every time you run the code.
   - You can use `with lock:` to automatically acquire a lock at the beginning of the block
     and release it when the block ends, either normally or due to an exception being thrown.

5. Run `nodes/timers`.  After observing the behavior and seeing the output, what can you infer about
   the relationship between threads and `rospy` timers?
6. What does `rospy.spin` do?  You can infer a bit by commenting it out and by replacing it
   with an infinite while loop.  Also feel free to look at the source code to answer this.
7. Are `main`, `callback1` and `callback2` executed on the same thread or on different threads in `nodes/timers`?
8. Run `sub_thread` and use `rostopic` to publish to the `sleep` topic.
   Is the sleeper subscriber running on the same thread as the main code?
9. By manipulating the frequency at which you publish to `sleep` and the time you have the subscriber delay you can infer
   information about ROS's thread behavior. Write a node called `pub_thread` that uses a `rospy.Timer` to publish a message to `sub_thread` at
   1 Hz.  The node should count how many messages it publishes and print out an updated count after every time it publishes.
   - Describe the behavior that you see when the delay time sent by `pub_thread` is shorter than 1 second
   - What happens when you increase the delay time sent by `pub_thread` to 2 seconds?
     - Does one subscriber callback complete before the next one is started?
     - After waiting for a few seconds, kill `pub_thread` but keep `sub_thread` running.  What happens with `sub_thread`?
10. Run two instances of the `pub_thread` node.  What is the relationship between subscriber threads
    and publishers?
    
