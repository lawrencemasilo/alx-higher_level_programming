#!/usr/bin/python3
"""
This module contains a baseclass, and a child class
"""


class BaseGeometry():
    """
    Args:
        None
    """
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""
        if isinstance(value, int) is True:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")


class Rectangle(BaseGeometry):
    """
    Args:
        BaseGeometry: inheriting from baseclass
    """
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
