#!/usr/bin/python3
"""inherite Rectangle from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
    def __init__(self, width, height):
        """
        Init a new Rectangle.

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
