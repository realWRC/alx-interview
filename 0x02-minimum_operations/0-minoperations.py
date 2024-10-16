#!/usr/bin/python3
"""
Module for a method to do an interview thing
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the
    file.
    """
    if n < 2:
        return 0
    totalOperations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            totalOperations += divisor
            n = n / divisor
        divisor += 1
    return totalOperations
