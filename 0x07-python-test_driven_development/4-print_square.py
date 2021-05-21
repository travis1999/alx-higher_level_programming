#!/usr/bin/python3
"""print square function"""


def print_square(size):
    """prints a square representation"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#"*(x + 1))
