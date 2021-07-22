#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """writes text to a file"""
    with open(filename, "w") as file:
        return file.write(text)
