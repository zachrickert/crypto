# -*- coding: utf-8 -*-
"""Transforms hexidecimal string to a base64 string."""
from binascii import unhexlify, b2a_base64


def hex_to_b64(hex_input):
    """Transform a hexidecimal string to a base64 string."""
    return b2a_base64(unhexlify(hex_input)).rstrip('\n')


def fixed_xor(input1, input2):
    """Take two equal-length buffers and produces their XOR combination."""
    if len(input1) == len(input2):
        return hex(int(input1, 16) ^ int(input2, 16)).lstrip('0x').rstrip('L')
    else:
        raise ValueError('Buffer lengths not equal')
