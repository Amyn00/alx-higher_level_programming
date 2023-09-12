#!/usr/bin/python3
""" function that inserts a line of text to a file,
after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text to a file, after each line
    Args:
        filename (str): The name of file
        search_string (str): The string to search
        new_string (str): The new string
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
