#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @staticmethod
    def valid(x):
        return type(x) == int and x >= 0

    @position.setter
    def position(self, value):
        if False in [*[self.valid(x) for x in value], len(value) == 2]:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for x in range(self.size):
            print(" "*self.position[0]+"#"*self.size)


if __name__ == "__main__":
    test_sq = Square(10, position=(10, 15))
    print(test_sq.size)

    test_sq.my_print()
