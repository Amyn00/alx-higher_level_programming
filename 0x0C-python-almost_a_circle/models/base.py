#!/usr/bin/python3
"""The first Class Base"""
import json


class Base:
    """The Base model.

    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation new Base.

        Args:
            id (int): The id of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON one of the standard formats for sharing data representation.
        Static method that return the JSON string representation of list dict

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
