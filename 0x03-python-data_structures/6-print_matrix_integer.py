#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for x in matrix:
        form = "{} "*len(x)
        print(form.format(*x).strip())

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]                
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
