# -*- coding: utf-8 -*-
"""Transforms hexidecimal string to a base64 string."""
from binascii import unhexlify, b2a_base64

HEXSTRING = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def hex_to_b64(hex_input):
    """Transform a hexidecimal string to a base64 string."""
    return b2a_base64(unhexlify(hex_input)).rstrip('\n')


if __name__ == '__main__':
    print(hex_to_b64(HEXSTRING))
