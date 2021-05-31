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

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """square initializer"""
        self.__size = self.integer_validator("size", size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """returns area of the square"""
        return self.__size * self.__size


if __name__ == "__main__":
    sq = Square(10)
