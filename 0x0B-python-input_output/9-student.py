#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """ class of student"""

    def __init__(self, first_name, last_name, age):
        """method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dir description"""
        return self.__dict__
