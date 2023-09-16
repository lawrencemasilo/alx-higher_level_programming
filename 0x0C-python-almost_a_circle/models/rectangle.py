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
    def get_width(self):
        return self.__width

    @get_width.setter
    def set_width(self, value):
        self.__width = value

    @property
    def get_height(self):
        return self.__height

    @get_height.setter
    def set_height(self, value):
        self.__height == value

    @property
    def get_x(self):
        return self.__x

    @get_x.setter
    def set_x(self, value):
        self.__x == value

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def set_y(self, value):
        self.__y == value
