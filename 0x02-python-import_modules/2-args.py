#!/usr/bin/python3
import sys


if __name__ == "__main__":
    print("{} arguments:".format(len(sys.argv) - 1))
    for idx, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(idx + 1, arg))
