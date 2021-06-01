#!/usr/bin/python3
"""save obj as json"""

import json


def save_to_json_file(my_obj, filename):
    """save json to file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
