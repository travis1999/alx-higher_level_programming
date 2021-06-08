#!/usr/bin/python3
"""base class for all shapes"""

import json
import os


class Base:
    """project base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base initializer
            Args:
                id(int): id of the object created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Creates objects from the dictionary
        kwargs:
            contains a dictionary containing the keys
            id, x, y, width, height for rectangle
            size, id, x, y for square
        """

        try:
            ins = cls(1)
        except TypeError:
            ins = cls(2, 2)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """loads from file"""
        c_name = cls.__name__
        file_name = c_name+".json"

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                s_data = cls.from_json_string(file.read())
                return [cls.create(**dta) for dta in s_data]
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Converts then saves a list of abjects to
        a json file
            Args:
                list_objs(List[Base]): list of objects to save
        """
        c_name = cls.__name__
        with open("{}.json".format(c_name), "w") as file:
            if not list_objs:
                json.dump([], file)
            else:
                file.write(cls.to_json_string(
                    [x.to_dictionary() for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries containing Base
        serialized data
            Args:
                json_string(str): json repr string
            Returns: list
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Takes a list of dictionaties and returns a json
        string
            Args:
                list_dictionaries(dict): a list of 'serialized'
                Base objects
            Returns: str
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
