#!/usr/bin/python3

""" Square class definition """


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ Square initializer

            Args:
                size (int): size of square
                position (tuple): 2d position of the square
            Returns:
                None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter"""
        return self.__position

    @staticmethod
    def valid(x):
        """checks args"""
        return type(x) == int and x >= 0

    @position.setter
    def position(self, value):
        """size setter

            Args:
                value (int): value of new size
            Returns:
                None
        """
        if False in [*[self.valid(x) for x in value], len(value) == 2]:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates area

        Returns:
            int: area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
            prints a square
        """
        for x in range(self.size):
            print(" "*self.position[0]+"#"*self.size)


if __name__ == "__main__":
    test_sq = Square(10, position=(10, 15))
    print(test_sq.size)

    test_sq.my_print()
