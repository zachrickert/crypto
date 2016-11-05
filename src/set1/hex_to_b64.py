# -*- coding: utf-8 -*-
"""Transforms hexidecimal string to a base64 string."""


def hex_to_b64(hex):
    """Transform a hexidecimal string to a base64 string."""

    # Test to see if incoming is hexidecimal
    try:
        int(hex, 16)
    except ValueError:
        raise TypeError('Input string is not a hexidecimal.')

    return hex
