#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if an obj is an inherited instance of class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
        Returns:
            If obj is an inherited of a_class -True.
            Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
