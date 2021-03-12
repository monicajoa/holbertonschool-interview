#!/usr/bin/python3
"""This module reads the stdind line by line
    and comupte metrics of the file size and status codes
"""
import sys
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for log, line in enumerate(sys.stdin, 1):
        aux_line = line.split(' ')
        st_code = aux_line[-2]
        fl_size = aux_line[-1]
        if st_code in status_codes:
            status_codes[st_code] += 1
        total_size += int(fl_size)
        if log % 10:
            print("File size: {:d}".format(total_size))
            for key, value in status_codes.items():
                if value > 0:
                    print("{}: {}".format(key, value))
finally:
    print("File size: {:d}".format(total_size))
    for key, value in status_codes.items():
        if value > 0:
            print("{}: {}".format(key, value))
