#!/usr/bin/python3
"""Rectangle class defintion"""


from . import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initializer"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height)

    @staticmethod
    def validate_int(name, value):
        """Validated whether value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def validate_value(self, name, value):
        """Validates value"""
        self.validate_int(name, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_pos(self, name, value):
        """Validates position"""
        self.validate_int(name, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_value("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_value("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_pos("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_pos("y", value)
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle with the # char"""
        print(("#"*self.width+"\n")*self.height)

    def update(self, *args, **kwargs):
        """Updates the triangle
            args: id, width, height, x, y
        """
        for idx, arg in enumerate(args):
            if idx == 0:
                self.id = arg
            elif idx == 1:
                self.width = arg
            elif idx == 2:
                self.height = arg
            elif idx == 3:
                self.x = arg
            elif idx == 4:
                self.y = arg
        if args:
            return

        for key, value in kwargs.items():
            if key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            elif key == "id":
                self.id = value
