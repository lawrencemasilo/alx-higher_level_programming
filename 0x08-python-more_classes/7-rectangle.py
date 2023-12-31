#!/usr/bin/python3
"""This module contains a class that defines a Rectangle"""


class Rectangle:
    """
        __inti__: to initialize width and height
        self.__width: Private instance attribute
        self.height: Private instance attribute
        width(): retrieves width
        @width.setter: Setter function
        height(): retrieves height
        height.setter: Setter function
        area(): returns the area of the rectangle
        perimeter(): returns perimeter of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec_str = ""
            for i in range(self.__height):
                rec_str = rec_str + (str(self.print_symbol) * self.__width)
                if i < self.__height - 1:
                    rec_str += "\n"
            return rec_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
