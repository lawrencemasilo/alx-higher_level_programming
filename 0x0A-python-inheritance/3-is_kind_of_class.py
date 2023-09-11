#!/usr/bin/python3
"""
This module contains a function that returns true,
if an object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj: the object to compare
        a_class: the class
    Return:
        True if is instance, otherwise false
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
