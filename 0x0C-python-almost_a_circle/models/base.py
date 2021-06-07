#!/usr/bin/python3

import json


class Base:
    """project base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base initializer
            Args:
                id(int): id of the object created
        """
        if id != None:
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
        if len(dictionary) == 5:
            rec = Rectangle

    @classmethod
    def save_to_file(cls, list_objs):
        """Converts then saves a list of abjects to
        a json file
            Args:
                list_objs(List[Base]): list of objects to save
        """
        class_name = cls.__class__.__name__
        with open("{}.json".format(class_name), "w") as file:
            if not list_objs:
                json.dump([], file)
            else:
                file.write(self.to_json_string(list_objs))

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
