#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    for idx in range(x):
        try:
            if int_count == x:
                break
            print("{:d}".format(my_list[x]))
            int_count += 1
        except TypeError:
            continue
    return int_count
