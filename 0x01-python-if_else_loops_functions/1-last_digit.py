#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_format = "Last digit of {} is {} and is {}"
last_digit = number % 10 if number > 0 else 10 - (number % 10)
last_mess = ""
if last_digit > 5:
    last_mess = "greater than 5"
elif last_digit == 0:
    last_mess = "zero"
elif last_digit < 6 and last_digit != 0:
    last_mess = "less than 6 and not 0"
print(str_format.format(number, last_digit, last_mess))
