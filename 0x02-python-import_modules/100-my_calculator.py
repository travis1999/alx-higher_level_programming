#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num_1, num_2 = [int(x) for x in sys.argv[1::2]]
    op = sys.argv[2]
    form = "{} {} {} = {}"
    if op == '+':
        print(form.format(num_1, op, num_2, add(num_1, num_2)))
    elif op == '-':
        print(form.format(num_1, op, num_2, sub(num_1, num_2)))
    elif op == '*':
        print(form.format(num_1, op, num_2, mul(num_1, num_2)))
    elif op == '/':
        print(form.format(num_1, op, num_2, div(num_1, num_2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
