#!/usr/bin/python3
"""
function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    This function return the int addition of a and b

    if a or b as a non-intiger or non-float, raise TypeError
    """

    # check if a is int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # chack if b is int or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # cast a and b to int then return their sum
    return int(a) + int(b)
