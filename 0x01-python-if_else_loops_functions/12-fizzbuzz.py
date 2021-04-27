#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        st = ""
        if x % 3 == 0:
            st += "fizz"
        elif x % 5 == 0:
            st += "buzz"
        print("{} ".format(st or x), end="")
