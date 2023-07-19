#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return sel.__dict__
