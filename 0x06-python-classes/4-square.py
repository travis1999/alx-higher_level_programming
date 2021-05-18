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
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

            Args:
                value (int): value of new size
            Returns:
                None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates area

        Returns:
            int: area of a square
        """
        return self.__size * self.__size


if __name__ == "__main__":
    test_sq = Square(20)
    print(test_sq.size)
