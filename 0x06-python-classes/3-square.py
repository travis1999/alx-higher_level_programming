#!/usr/bin/python3

""" Square class definition """


class Square:

    """Square class"""

    def __init__(self, size=0):
        """Square initializer

        Args:
            size (int): size of the square.

        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area

        Returns:
            int: area of a square
        """
        return self.__size * self.__size
