# -*- coding: utf-8 -*-
"""Transforms hexidecimal string to a base64 string."""
from binascii import unhexlify, b2a_base64
from binascii import Error as BinasciiError
from string import printable, punctuation

XOR_URL = 'http://cryptopals.com/static/challenge-data/4.txt'
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
    information = ('', 0, '')
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


def search_for_xor_cipher(filname):
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen

    max_score = 0
    for line_num, line in enumerate(urlopen(filname)):
        result, score, key = decode_xor(line.rstrip(b'\n'))
        if score > max_score:
            return_text = result
            max_score = score
            line_number = line_num
    return '{}: {}'.format(line_number, return_text)


def repeating_xor(text, key):
    encoded = ''
    count = 0
    for letter in text:
        if letter == '\n':
            # encoded += '\n'
            continue
        coded_let = hex(ord(letter) ^ ord(key[count % len(key)]))
        encoded += coded_let.lstrip('0x').zfill(2)
        count += 1
    return encoded

if __name__ == '__main__':
    string = """Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal"""
    print(repeating_xor(string, "ICE"))
