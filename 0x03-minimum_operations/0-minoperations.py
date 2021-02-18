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
    char_counter = 1
    op_counter = 0
    clippboard = 0
    if n <= 1:
        return 0
    while char_counter < n:
        if char_counter == 1:  # Caracter Actual
            op_counter += 2  # Copy all and Paste Ops
            clippboard = 1  # Clippboards with 1 Char
            char_counter += clippboard  # Increment the chars
        else:
            if n % 3 == 0 and char_counter >= 3:
                op_counter += 1
                char_counter += clippboard
            if n % 3 == 0 and char_counter < 3:
                op_counter += 1
                char_counter += clippboard
                op_counter += 1
                clippboard = char_counter
            if n % 3 != 0:
                if n % 2 == 0 and char_counter > 2:
                    op_counter += 1
                    char_counter += clippboard
                if n % 2 == 0 and char_counter == 2:
                    op_counter += 1
                    clippboard = char_counter
                    op_counter += 1
                    char_counter += clippboard
    return op_counter
