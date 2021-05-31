#!/usr/bin/python3
"""Geometry base class"""


class BaseGeometry:
    """The base geometry class"""

    def area(self):
        """area methord"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Number validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
