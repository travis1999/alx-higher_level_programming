#!/usr/bin/python3
def uppercase(str):
    for x in str:
        convert = 96 < ord(x) < 173
        string = chr(ord(x) - (32)) if convert else x)
        print( "{}".formant(string), end="")
    print()
