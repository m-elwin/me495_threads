#!/usr/bin/env python
""" This module is used for squaring the integers in a range
"""

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

