#!/usr/bin/python3
"""to py object"""

import json


def from_json_string(my_str):
    """converts json str to python object"""
    return json.loads(my_str)
