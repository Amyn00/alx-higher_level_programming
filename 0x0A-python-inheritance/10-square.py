#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py)."""
    def __init__(self, size):
        """
        Init a new Square.

        Args:
            size (int): The size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
