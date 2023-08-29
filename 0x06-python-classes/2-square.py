#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square:
    def __init__(self, size=0):
        self.__size = size

        try:
            int(self.__size)
            if not self.__size >= 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
