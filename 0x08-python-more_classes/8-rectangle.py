#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init a new Rectangle.

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new rectangle
        """
        type(self).number_of_instances += 1
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
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Print a message for every deletion of a Rect."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
