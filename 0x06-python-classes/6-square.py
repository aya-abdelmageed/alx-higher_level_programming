#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """init square"""
        self.size = size
        self.position = position

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
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @position.setter
    def position(self, val):
        """Setter method"""
        if type(val) != tuple or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in val) or any(j < 0 for j in val):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val
