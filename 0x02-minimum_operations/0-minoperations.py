#!/usr/bin/python3
"""
Module to find the minimum operations
to reach a target number of characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to reach n 'H' characters.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
