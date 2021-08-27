#!/usr/bin/python3
""" This module holds a function that
        returns the perimeter of an island
"""


def island_perimeter(grid):
    """Function that returns the perimeter of an island
    Args:
        grid (list of lists): Matrix of integers
    Returns:
        int: Perimeter of the island in grig
    """
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                if y + 1 >= len(grid[x]) or grid[x][y + 1] == 0:
                    perimeter += 1
                if y - 1 < 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                if x + 1 >= len(grid) or grid[x + 1][y] == 0:
                    perimeter += 1
                if x - 1 < 0 or grid[x - 1][y] == 0:
                    perimeter += 1
    return perimeter
