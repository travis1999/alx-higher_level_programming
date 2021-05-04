#!/usr/bin/python3


def padd(t):
    t = list(t)
    for x in range(len(t), 2):
        t.append(0)
    return tuple(t)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = padd(tuple_a)
    tuple_b = padd(tuple_b)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
