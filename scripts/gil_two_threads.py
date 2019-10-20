#!/usr/bin/env python
""" Demonstrate that python threads do not execute simultaneously

    The code computes the square of a list of numbers.

    First it does so using a single loop in a single thread.

    Next it does it using two threads, one for each list half.

    The timing results for both methods are displayed
"""
from __future__ import print_function
import threading
import timeit

def squares(a, b):
    """ Compute the square of each integer from a to b

        Args:
            a (int) - the lowest number in the range (inclusive)
            b (int) - the highest number in the range (exclusive)

            Note: a < b

       Returns:
         The squares of the integers from 0 to 1000
    """
    nums = range(a, b)
    squares = []
    for n in nums:
        squares.append(n**2)
    return squares

def one_thread_square():
    """ Computes the square of each integer from 0 to 100000
        Uses a single thread. 

        Prints the time it took to execute
    """
    start = timeit.default_timer()
    squares(0, 100001) # The max range is not inclusive
    end = timeit.default_timer()
    print("One Thread Time: ", end - start)

def two_thread_square():
    """ Computes the square of each integer from 0 to 100000, using two threads
    
        Prints the time it took to execute, excluding the time to setup the threads
    """
    # create the threads, each to handle half the lists
    thread1 = threading.Thread(target = squares, args = (0, 50000))
    thread2 = threading.Thread(target = squares, args = (50000, 100001))
    
    start = timeit.default_timer()
    # start the threads
    thread1.start()
    thread2.start()

    # wait for the threads to complete
    thread1.join()
    thread2.join()
    end = timeit.default_timer()
    print("Two Thread Time: ", end - start)


def main():
    one_thread_square()
    two_thread_square()

if __name__ == "__main__":
    main()
