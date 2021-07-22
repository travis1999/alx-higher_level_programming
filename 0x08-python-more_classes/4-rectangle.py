#!/usr/bin/python3
"""OOP TASKS"""


class Rectangle:
    """Rectangle class def"""

    def __init__(self, width=0, height=0):
        """class initializer"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (("#"*self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Get string."""
        width = self.__width
        height = self.__height
        string = "Rectangle(" + str(width) + \
            ", " + str(height) + ")"
        return string

    def check_dim(self, value, name):
        """checks if dimension is valid"""
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

    def area(self):
        """returns the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width+self.height)
