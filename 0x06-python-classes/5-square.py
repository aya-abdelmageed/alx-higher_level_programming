#!/usr/bin/python3
"""class Square that defines a square by"""


class Square:
    """class Square that defines a square by"""
    def __init__(self, size=0):
        """init square"""
        self.size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, val):
        """Setter method"""
        if type(val) is not int:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val

    def area(self):
        """return area"""

    def my_print(self):
        """print to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
