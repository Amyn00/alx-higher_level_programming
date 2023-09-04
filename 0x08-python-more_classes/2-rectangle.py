#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Init a new Rectangle.

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    # Getter and Setter for width value.
    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Getter and Setter for height value.
    @property
    def height(self):
        """Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the Resctangle.
        
        Returns:
            int: The area
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Calculates the area of the Rectangle.
        
        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
