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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            return __width

        @width.setter
        def width(self, value):
            if type(value) is not [int, float]:
                raise TypeError("Enter integer or float")
            if value < 0:
                raise ValueError("Positive numbers only")
            else:
                self.__width = value

        @property
        def height(self):
            return __height

        @height.setter
        def height(self, value):
            if type(value) is not [int, float]:
                raise TypeError("Enter integer or float")
            if value < 0:
                raise ValueError("Positive numbers only")
            else:
                self.__height == value

        @property
        def x(self):
            return __x

        @x.setter
        def x(self, value):
            if type(value) is not [int, float]:
                raise TypeError("Enter integer or float")
            else:
                self.__x == value

        @property
        def y(self):
            return __y

        @y.setter
        def y(self, value):
            if type(value) is not [int, float]:
                raise TypeError("Enter integer or float")
            else:
                self.__y == value
