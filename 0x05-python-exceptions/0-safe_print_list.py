#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    if x == 0:
        return 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
        except IndexError:
            idx -= 1
            break
    return idx + 1
