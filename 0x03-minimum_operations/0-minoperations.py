#!/usr/bin/python3
""" Module that holds the function minOperations(n)
"""


def minOperations(n):
    """ Method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file

    Args:
        n ([int]): [number of letters to search]

    Returns:
        [n]: [number of operations]
    """
    char_counter = 2  # Character Counter, initializes with "HH" two Characters
    op_counter = 2   # Operations Counter, Copy & paste (have 2 Chars) = 2 op
    clippboard = 1   # Clippboard, number of characters currently copied
    if n <= 1:
        return 0
    while char_counter < n:
        if n % char_counter == 0:
            clippboard = char_counter
            op_counter += 1
        char_counter += clippboard
        op_counter += 1
    return op_counter
