#!/usr/bin/python3
"""is sub"""


def inherits_from(obj, a_class):
    """is subclass"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
