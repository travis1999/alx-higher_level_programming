#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for x in matrix:
        form = "{} "*len(x)
        print(form.format(*x).strip())
