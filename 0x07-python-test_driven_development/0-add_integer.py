#!/usr/bin/python3
"""
    python3 -c 'print(__import__("0-add_integer").__doc__)'
    This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    Args:
        a: is type int, and greater or equals to zero
        b: is type int, if a default value of 98 if argument not passed
    Return: the addition of a and b, type int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/0-add_integer.txt")
