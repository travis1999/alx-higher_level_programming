#!/usr/bin/python3
"""modify json file"""

import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
args_list = []

if os.path.exists(file_name):
    args_list = load_from_json_file(file_name)
args_list += sys.argv[1:]
save_to_json_file(args_list, file_name)
