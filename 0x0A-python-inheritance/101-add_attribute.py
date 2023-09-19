#!/usr/bin/python3
"""
This module contains a function that adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """
    Args:
        parameter A: the object
        parameter B: the name
        parameter C: the value of object
    """
    if hasattr(obj, '__dict__') is True:
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
