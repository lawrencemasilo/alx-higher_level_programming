#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square:
    """ __inti__: to initialize size
        self.__size: to make size private
        try: is to check if size is an integer
    """
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
