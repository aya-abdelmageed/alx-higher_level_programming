#!/usr/bin/python3
"""Load, add, save"""
import sys
import os.path


ar = sys.argv[1:]

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

item = []
if os.path.exists("./add_item.json"):
    item = load_from_json_file("add_item.json")

save_to_json_file(item + ar, "add_item.json")
