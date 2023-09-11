#!/usr/bin/python3
"""inherite Rectangle from BaseGeometry"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a param as int.
        Args:
            name (str): The name of param
            value (int): The param to validate
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
