#!/usr/bin/python3
"""to json module"""

import json


def to_json_string(my_obj):
    """returns json repr of a python obj"""
    return json.dumps(my_obj)
