#!/usr/bin/env python
""" Despite the GIL, one thread executes while another waits for input 
   
    A "say_hello" thread prints "Hello <count>" every 0.5 seconds.
    Meanwhile the main loop waits for user input.

    Note that hello keeps being printed in the background since the main thread
    is waiting on input.
"""
from __future__ import print_function
import threading
import time

# Signal to the say_hello thread when it should end
done = False

def say_hello():
    """ Increment a count and print it"""
    count = 0
    while not done:
        print("Hello: ", count)
        count += 1
        time.sleep(0.5)

def get_input():
    """ Get user input and print it. If user types quit, exit """
     
if __name__ == "__main__":
    thread1 = threading.Thread(target = say_hello) 
    thread1.start()
    while True:
        x = raw_input("Enter something, or quit to exit:")
        print("You Entered: ", x)
        if x == "quit":
            break;
    done = True
    thread1.join()
    print("The End")
