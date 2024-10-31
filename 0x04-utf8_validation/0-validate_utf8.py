#!/usr/bin/python3
"""
ALX interview question solution for 0x04. UTF-8 Validation.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8
    encoding
    """
    numBytes = 0
    for byte in data:
        byte = byte & 0xFF
        if numBytes == 0:
            if (byte >> 5) == 0b110:
                numBytes = 1
            elif (byte >> 4) == 0b1110:
                numBytes = 2
            elif (byte >> 3) == 0b11110:
                numBytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            numBytes -= 1
    return numBytes == 0
