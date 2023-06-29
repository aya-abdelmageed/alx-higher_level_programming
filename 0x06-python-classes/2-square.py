#!/usr/bin/python3
"""class Square that defines a squar"""


class Square:
    """class Square that defines a squar"""
    def __init__(self, size=0):
        """initialize the data"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
