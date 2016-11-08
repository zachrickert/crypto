#Crypto
This repository contains challenges from the the [cryptopals crypto challenges](http://cryptopals.com/).

##Set 1: Basics

### 1: Convert hex to base64
This program will convert a hexidecimal string to base64.

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

### 2: Fixed XOR
This program will take two equal-length buffers and produces their XOR combination.

The strings, after hex decoding and XOR'd:
1c0111001f010100061a024b53535009181c
686974207468652062756c6c277320657965

should produce:
746865206b696420646f6e277420706c6179
