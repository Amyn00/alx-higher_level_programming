#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    Print a square with the charactere #.

    Args:
        size (int): The size len of te square.
    
    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
