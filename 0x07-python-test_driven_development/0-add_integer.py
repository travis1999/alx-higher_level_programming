#!/usr/bin/python3
"""
function that adds two integers
"""


def check_type(var):
    """checks variable type
    returns True if int or Float
    """
    return type(var) == int or type(var) == float


def add_integer(a, b=98):
    """Returns sum of a and b"""
    if not check_type(a):
        raise TypeError("a must be an integer")
    if not check_type(b):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
