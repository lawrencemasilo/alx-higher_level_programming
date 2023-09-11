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
        raise Exception("area() is not implemented")
