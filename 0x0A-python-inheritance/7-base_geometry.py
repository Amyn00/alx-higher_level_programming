#!/usr/bin/python3
"""Create a class based 7-base_geometry.py"""


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
