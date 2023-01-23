#!/usr/bin/python3
'''Scripts that determines if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''Number of bytes in current UTF-8 character'''
    num_bytes = 0
    # Iterate through each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        mask = 1 << 7
        byte = byte & ~mask
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # If the byte starts with 10, it's a continuation byte
            # and therefore not the start of a new character
            if (byte >> 6) == 0b10:
                return False
            # If the byte starts with 0, it's a single-byte character
            elif (byte >> 7) == 0:
                num_bytes = 1
            # If the byte starts with 110, it's the start of a 2-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 2
            # If the byte starts with 1110, it's the start of a 3-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 3
            # If the byte starts with 11110, it's the start of a 4-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 4
            # If the byte starts with any other value, it's not a valid UTF-8 character
            else:
                return False
        # If this is a continuation byte
        else:
            # If the byte does not start with 10, it's not a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    # If all bytes were continuation bytes or the data is empty, it's not a valid UTF-8 string
    return num_bytes == 0
