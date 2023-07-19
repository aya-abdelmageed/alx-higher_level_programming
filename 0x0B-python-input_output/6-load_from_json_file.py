#!/usr/bin/python3
"""Create object from a JSON file"""
import json as j


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”"""
    with open(filename) as f:
        return j.load(f)
