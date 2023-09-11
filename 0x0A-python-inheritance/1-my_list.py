#!/usr/bin/python3
"""
script task 1. My list.
"""


class MyList(list):
    """
    Write a class MyList that inherits from list:

    """
    def print_sorted(self):
        """
        print a sorted list ascd
        """
        print(sorted(self))
