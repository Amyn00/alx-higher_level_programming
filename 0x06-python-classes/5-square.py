#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    """Getter"""
    def size(self):
        return self.__size

    @size.setter
    """Setter"""
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
