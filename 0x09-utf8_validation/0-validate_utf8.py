#!/usr/bin/python3
"""
 Module that holds a funtion
 that validates UTF-8 encoding
"""


def validUTF8(data):
    """Funtion that cheks if the
    data is encode in UTF-8
    Args:
        data ([list]): List of the data to validate
    Returns:
        [Bool]: True if is valid UTF-8 otherwise False
    """
    cnt = 0
    for byte in data:
        if 128 <= byte <= 191:
            if cnt == 0:
                return False
            cnt -= 1
        else:
            if cnt:
                return False
            if byte < 128:
                continue
            elif byte < 224:
                cnt = 1
            elif byte < 240:
                cnt = 2
            elif byte < 248:
                cnt = 3
            else:
                return False
    return cnt == 0
