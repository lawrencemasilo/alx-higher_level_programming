#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square:
    """ __inti__: to initialize size
        self.__size: to make size private
        try: is to check if size is an integer
        @property: to initialize the getter function
        @size.setter: to initialize the setter function
    """
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
