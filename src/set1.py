# -*- coding: utf-8 -*-
"""Transforms hexidecimal string to a base64 string."""
from binascii import unhexlify, b2a_base64
from binascii import Error as BinasciiError
from string import printable, punctuation

HEX4 = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
printable_set = set(printable)
punctuation_set = set(punctuation)
freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074, ' ': 16.67, '.': 1.306, ',': 1.232, ';': 0.064,
    ':': 0.068, '!': 0.066, '?': 0.112, "'": 0.486, '"': 0.534, '-': 0.306
}


def hex_to_b64(hex_input):
    """Transform a hexidecimal string to a base64 string."""
    try:
        return_value = b2a_base64(unhexlify(hex_input)).rstrip(b'\n')
    except (TypeError, BinasciiError):
        raise TypeError
    return return_value


def fixed_xor(input1, input2):
    """Take two equal-length buffers and produces their XOR combination."""
    if len(input1) == len(input2):
        return str.encode(hex(int(input1, 16) ^ int(input2, 16)).lstrip('0x').rstrip('L'))
    else:
        raise ValueError('Buffer lengths not equal')

def decode_xor(input1):
    """Decodes a single xor cipher."""

    max_score = 0

    for i in range(255):
        result = ''
        score = 0
        for j in range(len(input1) // 2):
            temp = chr(int(input1[2 * j: 2 * (j + 1)], 16) ^ i)
            if temp in printable_set:
                result += temp
                try:
                    score += freq[temp.lower()]
                except KeyError:
                    if temp.isdigit():
                        score += 4
            else:
                score = 0
                break
        if score > max_score:
            information = result, score, chr(i)
            max_score = score

    return information

if __name__ == '__main__':
    print(decode_xor(HEX4))
