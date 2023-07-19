#!/usr/bin/python3
"""To JSON string"""
import json as j


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return j.dumps(my_obj)
