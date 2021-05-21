#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """prints indented text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        if x in ['.', '?', ':']:
            print()
        else:
            print(x, end='')
