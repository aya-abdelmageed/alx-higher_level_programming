#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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

    def area(self):
        """for area
        Args:
            __width (int): the width of th rectangle
            __height (int): the height of the rectangle
        Return:
            the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle
        Args:
            __height (int): of the rect
            __width (int): of the rect
        Return:
            the ans or 0
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and i != self.__height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """return a string of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(self):
        """prints message of deletion of instance.
        """
        self.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and
        returns the larger of the two"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
