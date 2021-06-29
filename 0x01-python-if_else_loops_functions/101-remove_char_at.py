#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0:
        stringcpy = string[:n] + string[(n + 1):]
        return stringcpy
    return string
