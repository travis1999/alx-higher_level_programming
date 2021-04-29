#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv) - 1 
    print("{} arguments{}".format(l, ':' if l else '.'))
    for idx, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(idx + 1, arg))
