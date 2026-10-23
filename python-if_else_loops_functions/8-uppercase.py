#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        code = ord(letter)
        if 97 <= code <= 122:
            code -= 32
        result += chr(code)
    print("{:s}".format(result))
