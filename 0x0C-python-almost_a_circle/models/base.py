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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): Is list of instance who inherites of Base
        """
        filename = cls.__name__ + ".json"
        list_dicts = [o.to_dictionary() for o in list_objs]
        json_string = Base.to_json_string(list_dicts)
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """That return the list of the JSON string representation json_string

        Args:
            json_string (str): is a string representing a list of dict
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that return an instance with all attrs already set.

        Args:
            **dictionary (dict): Key/Value pairs of attrs to init
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
