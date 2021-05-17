#!/usr/bin/python3


def div(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by zero")
    except TypeError:
        print("wrong type")
    return result


def list_division(my_list_1, my_list_2, list_length):
    res = []
    for x in range(list_length):
        try:
            res.append(div(my_list_1[x], my_list_2[x]))
        except IndexError:
            print("out of range")
            res.append(0)
        finally:
            pass
    return res
