#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    modules = [x for x in dir(hidden_4) if not x.startswith("__")]
    for x in modules:
        print(x)
