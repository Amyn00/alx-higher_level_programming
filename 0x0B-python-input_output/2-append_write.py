#!/usr/bin/python3
"""This defines a file-appending function."""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8).
    Args:
        filename (str): input
        text (str): input
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
