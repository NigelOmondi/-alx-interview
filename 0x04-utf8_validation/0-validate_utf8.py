#!/usr/bin/env python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers, each representing one byte of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_remaining_bytes = 0

    for byte in data:
        if num_remaining_bytes == 0:
            # Check the first byte
            if (byte >> 5) == 0b110:
                num_remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_remaining_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check the continuation bytes
            if (byte >> 6) != 0b10:
                return False
            num_remaining_bytes -= 1

    return num_remaining_bytes == 0
