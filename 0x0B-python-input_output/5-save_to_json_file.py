#!/usr/bin/python3
""" function that writes an Object to a text file,
using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: input
        filename: input
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
