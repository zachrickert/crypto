# -*- coding: utf-8 -*-
"""Testing for hex_to_b64.py module."""
import pytest

from hex_to_b64 import hex_to_b64

HEXSTRING = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
NOT_HEXSTRING = b"Not a hexistring"
BASE64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
# -------------------Tests------------------------
# [x] Accepts text if incoming is hexidecimal.
# [x] Type error if incoming is not hexidecimal.
# [] Return correct value.


def test_incoming_hexidecimal():
    """Accept text if incoming is hexidecimal."""
    assert hex_to_b64(HEXSTRING)


def test_incoming_not_hexidecimal_raises_error():
    """Accept text if incoming is hexidecimal."""
    with pytest.raises(TypeError):
        hex_to_b64(NOT_HEXSTRING)


def test_outputs_correct_strip():
    """Return correct value."""
    assert hex_to_b64(HEXSTRING) == BASE64
