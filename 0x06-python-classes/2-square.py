#!/usr/bin/python3
"""write a class Square that defines a square by:(based on 1-square.py)"""


class Square:
    """Class - Square"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
