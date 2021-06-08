#!/usr/bin/python3
"""Square class definition"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square initializer
            Args:
                size(int): size of the square
            Kwargs:
                x(int): x position
                y(int): y position
                id(int): id of the shape
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square as string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square
        key word arguments are ignored if argsis used
            args: id, size, x, y
            kwargs: id, size, x, y

            eg:
                sq.update(10, 20) #updates id and size
        """
        if args:
            i_args = ["id", "size", "x", "y"]
            kwargs = dict(zip(i_args, args))

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """returns a dictionary representation
        of the object
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
