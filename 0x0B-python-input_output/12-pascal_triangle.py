#!/usr/bin/python3
"""pascal triangle calculation"""


def next_pascal(current):
    """finds the next seq in a pascals
    triangle
    """
    mid = []

    for idx, x in enumerate(current):
        nxt = idx + 1

        if not nxt > len(current) - 1:
            mid.append(x + current[nxt])
    return [1] + mid + [1]


def pascal_triangle(n):
    """returns a pascals triangle"""
    res = []

    if n <= 0:
        return res

    current = [1]
    for _ in range(n):
        res.append(current)
        current = next_pascal(current)

    return res
