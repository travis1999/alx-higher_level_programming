#!/usr/bin/python3
def uppercase(str):
    for x in str:
        convert = 96 < ord(x) < 173
        print(chr(ord(x) - (32)) if convert else x, end="")
    print()
