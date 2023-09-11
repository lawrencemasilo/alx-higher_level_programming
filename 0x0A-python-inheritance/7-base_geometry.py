#!/usr/bin/python3
"""
This module contains a baseclass
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
        if type(value) is int:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
