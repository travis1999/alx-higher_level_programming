#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        for idx, x in enumerate(my_list[:x]):
            print("{}".format(x), end="")
    except IndexError:
        for idx, x in enumerate(my_list):
            print("{}".format(x), end="")
    finally:
        print()
        return idx + 1
