#!/usr/bin/python3
"""defines a student."""


class Student:
    """Class Student."""
    def __init__(self, first_name, last_name, age):
        """
        init student
        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets a dictionary representation of the Student.
        Args:
            attrs (list): (Optional) input
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
