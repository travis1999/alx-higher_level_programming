#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

form = "{} {} {} = {}"

print(form.format(a, '+', b, add(a, b)))
print(form.format(a, '-', b, sub(a, b)))
print(form.format(a, '*', b, mul(a, b)))
print(form.format(a, '/', b, div(a, b)))
