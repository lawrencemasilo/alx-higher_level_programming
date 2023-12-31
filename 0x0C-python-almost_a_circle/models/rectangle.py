#!/usr/bin/python3
"""
python3 -c 'print(__import__("rectangle").__doc__)'
This directory contains a Rectangle class
that inherits from the base class
"""
from models.base import Base


class Rectangle(Base):
    """
    print(__import__("rectangle").MyClass.my_function.__doc__)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        print(__import__("rectangle").my_function.__doc__)
        assigns the public instance attribute id,
        with the argument value,
        or the private class attribute __nb_objects

        Args:
            id: Must be integer type only
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height == value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x == value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y == value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for cx in range(self.__y):
            print(end="\n")
        for i in range(self.__height):
            for cy in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print(end="\n")

    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) {self.__x}/"
                f"{self.__y} - {self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        if args is not None or Kwargs is not None:
            if len(args) > 0:
                super().__init__(args[0])
            if "id" in kwargs:
                super().__init__(kwargs["id"])

            if len(args) > 1:
                if not isinstance(args[1], int):
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]

            if "width" in kwargs:
                if not isinstance(kwargs["width"], int):
                    raise TypeError("width must be an integer")
                if kwargs["width"] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = kwargs["width"]

            if len(args) > 2:
                if not isinstance(args[2], int):
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = args[2]

            if "height" in kwargs:
                if not isinstance(kwargs["height"], int):
                    raise TypeError("height must be an integer")
                if kwargs["height"] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = kwargs["height"]

            if len(args) > 3:
                if not isinstance(args[3], int):
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[3]

            if "x" in kwargs:
                if not isinstance(kwargs["x"], int):
                    raise TypeError("x must be an integer")
                if kwargs["x"] <= 0:
                    raise ValueError("x must be >= 0")
                self.__x = kwargs["x"]

            if len(args) > 4:
                if not isinstance(args[4], int):
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[4]

            if "y" in kwargs:
                if not isinstance(kwargs["y"], int):
                    raise TypeError("y must be an integer")
                if kwargs["y"] <= 0:
                    raise ValueError("y must be >= 0")
                self.__y = kwargs["y"]

    def to_dictionary(self):
        return self.__dict__
