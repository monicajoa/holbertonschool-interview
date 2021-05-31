#!/usr/bin/python3
""" Module containing the rain task,
    Calculate how many square units of water
    will be retained after it rains on a relief map
"""


def rain(walls):
    water_limit = 0
    distance = 0
    height = 0

    if len(walls) == 0:
        return 0
    for index in walls:
        if index == 0 and height > 0:
            distance += 1
        if index > 0:
            wall_height = min(height, index)
            water_limit += wall_height * distance
            height = index
            distance = 0

    return water_limit
