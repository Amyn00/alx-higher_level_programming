#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Write a function that prints My name is <first name> <last name>.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        None
    """

    # check if first name is string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # check is last name is string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
