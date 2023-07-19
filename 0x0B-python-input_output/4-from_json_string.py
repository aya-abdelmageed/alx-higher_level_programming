#!/usr/bin/python3
"""From JSON string to Object"""
import json as j


def from_json_string(my_str):
    """return an object(Python data structure)represented by a JSON string"""
    return j.loads(my_str)
