#!/usr/bin/env python
""" This code has a race condition, can you fix me?
"""
from __future__ import print_function
import threading

total = 0

def callback(niters):
    global total
    """ Loop for a specified number of iterations """
    for i in range(niters):
        total += 1

if __name__ == "__main__":
    num_iters = 1000
    t1 = threading.Thread(target = callback, args = (num_iters,))
    t2 = threading.Thread(target = callback, args = (num_iters,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Each thread did", num_iters, "iterations. Total is", total)
