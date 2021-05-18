#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.size = size

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

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for x in range(self.size):
            print("#"*self.size)


if __name__ == "__main__":
    test_sq = Square(10)
    print(test_sq.size)

    test_sq.my_print()
