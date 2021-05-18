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

    def my_print(self):
        """ prints the square"""
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                print("#"*self.size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
