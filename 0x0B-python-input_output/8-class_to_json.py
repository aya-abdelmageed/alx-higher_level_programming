#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """ dictionary description with simple data structure (list, dict ..."""
    x = {}
    if hasattr(obj, "__dict__"):
        x = obj.__dict__.copy()
    return x
