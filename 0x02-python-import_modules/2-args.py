#!/usr/bin/python3
import sys

print("{} arguments:".format(len(sys.argv) - 1))
for idx, arg in enumerate(sys.argv[1:]):
    print("{}: {}".format(idx + 1, arg))
