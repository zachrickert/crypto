# -*- coding: utf-8 -*-
"""Testing for hex_to_b64.py module."""
import pytest

from set1 import hex_to_b64, fixed_xor

HEX1 = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
NOT_HEXSTRING = b"Not a hexistring"
BASE64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
HEX2 = b'1c0111001f010100061a024b53535009181c'
HEX3 = b'686974207468652062756c6c277320657965'
HEX_RESULT1 = b'746865206b696420646f6e277420706c6179'

# -------------------hex_to_bin64.py Tests------------------------
# [x] Accepts text if incoming is hexidecimal.
# [x] Type error if incoming is not hexidecimal.
# [x] Return correct value.


def test_hex_to_bin64_accepts_incoming_hexidecimal():
    """Accept text if incoming is hexidecimal."""
    assert hex_to_b64(HEX1)


def test_hex_to_bin64_incoming_not_hexidecimal_raises_error():
    """Accept text if incoming is hexidecimal."""
    with pytest.raises(TypeError):
        hex_to_b64(NOT_HEXSTRING)


def test_hex_to_bin64_outputs_correct_value():
    """Return correct value."""
    assert hex_to_b64(HEX1) == BASE64


# -------------------fixed_xor.py Tests------------------------
# [x] Accepts two buffers.
# [x] Unequal buffer lengths not equal length raises error.
# [] Returns correct XOR'd value.


def test_fixed_xor_accepts_two_buffers():
    """Accept text if incoming is hexidecimal."""
    assert fixed_xor(HEX2, HEX3)


def test_fixed_xor_raises_error_if_buffer_lengths_not_equal():
    """Unequal buffer lengths not equal length raises error."""
    with pytest.raises(ValueError):
        fixed_xor(HEX1, HEX2)


def test_fixed_xor_returns_correct_amount():
    """Returns correct XOR'd value."""
    assert fixed_xor(HEX2, HEX3) == HEX_RESULT1
