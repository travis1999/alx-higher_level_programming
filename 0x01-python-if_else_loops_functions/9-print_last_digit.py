#!/usr/bin/python3
def print_last_digit(number):
    last = None
    if number >= 0:
        last = number % 10
    if number < 0:
        last = 10 - number % 10
    print(last, end="")
    return last
