#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, att, value):
    """
    Add a new attribute to an object if possible.
    Args:
        obj (any): The obj to add
        att (str): The name of the att to add
        value (any): The value of att
    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
