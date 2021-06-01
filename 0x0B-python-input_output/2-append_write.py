#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
