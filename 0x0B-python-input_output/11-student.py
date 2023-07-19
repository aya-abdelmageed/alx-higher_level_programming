#!/usr/bin/python3
""" Student to disk and reload"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for i, j in json.items():
            setattr(self, i, j)
