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
    """Rectangle sub class"""
    def __init__(self, width, height):
        """initializer"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """Rectangle str representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """reterns area of the rectangle"""
        return self.__width * self.__height
