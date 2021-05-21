#!/usr/bin/python3
"""matrix division"""


def m_div(a, b):
    """divides a by b"""

    if not type(a) == int or not type(b) == float:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    return round(a/b, 2)


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not type(div) == int or not type(b) == float:
        raise TypeError("div must be a number")

    lens = [len(x) for x in div]
    if len(set(lens)) != 1:
        raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")

    return [[m_div(a, b) for x in y] for y in div]
