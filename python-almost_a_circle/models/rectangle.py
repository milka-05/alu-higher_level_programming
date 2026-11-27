#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


def check(name, value, strict):
    """Validate an integer attribute.

    strict is True when the value must be > 0, False when >= 0."""
    if not isinstance(value, int):
        raise TypeError(name + " must be an integer")
    if strict and value <= 0:
        raise ValueError(name + " must be > 0")
    if not strict and value < 0:
        raise ValueError(name + " must be >= 0")


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Set the width, height, x, y and id of the rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width."""
        return self.__width

    @width.setter
    def width(self, value):
        check("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get or set the height."""
        return self.__height

    @height.setter
    def height(self, value):
        check("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get or set x."""
        return self.__x

    @x.setter
    def x(self, value):
        check("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get or set y."""
        return self.__y

    @y.setter
    def y(self, value):
        check("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attributes from args, or from kwargs if no args."""
        names = ["id", "width", "height", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
