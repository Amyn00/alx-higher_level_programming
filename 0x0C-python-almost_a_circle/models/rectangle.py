#!/usr/bin/python3
"""Class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation rectangle constructor

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
            x (int): x value of rectangle
            y (int): y value of rectangle
            id (int): The id Base of Rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """The Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Print in stdout the rectangle instance with the char #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("")for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle
        that assigns an argument to each attribute.

        Args:
            *args (ints): New attr value.
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attrs
        """
        if args:
            arg_name = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_name[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method
        def to_dictionary(self): that returns the dictionary representation
        of a Rectangle:"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
