#!/usr/bin/python3
"""
    This module contains a function that returns
    attributes and methods of an object
"""


def lookup(obj):
    """
    parameter a: an object
    """

    return list(dir(obj))
