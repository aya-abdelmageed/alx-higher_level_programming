#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): the width of rectangle

        """
        return self.__width

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): the height of rectangle

        """
        return self.__height

    @width.setter
    def width(self, value):
        """Args:
            value (int): the width of rectangle

        Attributes:
            __width (int):the width of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Args:
            value (int): the height of rectangle

        Attributes:
            __height (int): the height of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
