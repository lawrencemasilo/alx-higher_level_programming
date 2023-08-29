#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square:
    """ __inti__: to initialize size
        self.__size: to make size private
        try: is to check if size is an integer
        @property: to initialize the getter function
        @size.setter: to initialize the setter function
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if position[0] > 0 and position[1] > 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if position[0] > 0 and position[1] > 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print(end="\n")
        else:
            x = 0
            for i in range(self.__size):
                if x < self.position[0]:
                    print("_", end="")
                for j in range(self.size):
                    print("#", end="")
                print(end="\n")
                x += 1
