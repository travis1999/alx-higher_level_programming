#!/bin/python3
"""to json module"""

import json


def to_json_string(my_obj):
    """returns json repr of a python obj"""
    return json.dumps(my_obj)


if __name__ == "__main__":
    print(to_json_string([1, 2, 3, 4]))
