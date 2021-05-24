#!/usr/bin/python3
"""OOP TASKS"""


class Rectangle:
    """Rectangle class def"""

    def __init__(self, width=0, height=0):
        """class initializer"""
        self.width = width
        self.height = height

    def check_dim(self, value, name):
        """checks if dimention is valid"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.check_dim(value, "width")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""
        self.check_dim(value, "height")
        self.__height = value
