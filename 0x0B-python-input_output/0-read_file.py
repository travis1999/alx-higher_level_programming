#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """reads file to stdout"""
    with open(filename, "r") as file:
        print(file.read())
    