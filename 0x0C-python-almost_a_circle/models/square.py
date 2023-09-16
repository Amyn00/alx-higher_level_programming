#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherite from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """This initializes a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The id of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method def update(...)
        that assigns attrs.
        Args:
            *args: is the list of arguments - no-keyworded arguments.
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs: can be thought of as a double pointer to a dictionary:
                      key/value (keyworded arguments)
        """
        if args:
            arg_name = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_name[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def to_dictionary(self):
        """Update the class Square by adding the public method
        def to_dictionary(self): that returns the dictionary representation
        of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
