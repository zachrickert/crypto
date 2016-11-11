#Crypto
This repository contains challenges from the the [cryptopals crypto challenges](http://cryptopals.com/).

##Set 1: Basics

### 1: Convert heßx to base64
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

### 3: Decode XOR cipher
This program will dechper a single XOR cipher.

It will loop through the 255 possible combinations for the XOR key.
Each function will be scored against the frequency of different letters,
numbers and punctuation marks.  The program will return the string that
scores the highest.

The frequency scores that are used are:

    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
    'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
    's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074, ' ': 16.67, '.': 1.306, ',': 1.232, ';': 0.064,
    ':': 0.068, '!': 0.066, '?': 0.112, "'": 0.486, '"': 0.534, '-': 0.306

* Letter: Scores were taken from [letter frquency](https://en.wikipedia.org/wiki/Letter_frequency)
* Spaces: Average english word is 5 letters long, so 1 out 6 charicters should be a space or 16.67%
* Numbers: Are all given a score of 4 in the code.
* Punctionation: Scores taken from [punctuation frequency](https://en.wikipedia.org/wiki/Punctuation_of_English).
    * These were given as frequency per 1000 words.
    * Divided given number by 1000 to get punctuation freq per word.
    * Divided by 5 to get punctuation per letter (assume average of 5 letters per word)
    * Multiple by 100 to get percent.
