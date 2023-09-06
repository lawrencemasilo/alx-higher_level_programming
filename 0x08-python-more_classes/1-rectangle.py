#!/usr/bin/python3
"""This module contains a class that defines a Rectangle"""


class Rectangle:
    """
        __inti__: to initialize width and height
        self.__width: Private instance attribute
        self.height: Private instance attribute
        width(self): retrieves width
        @width.setter: Setter function
        height(self): retrieves height
        height.setter: Setter function
    """
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if isinstance(height, int) is not True:
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
