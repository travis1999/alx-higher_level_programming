#!/usr/bin/python3
"""Creating classes

class square created with private var size

"""


class Square:
    def __init__(self, size):
        """Square initializer

        Args:
            size (int): size of the square.

        Returns:
            None
    """
        self.__size = size
