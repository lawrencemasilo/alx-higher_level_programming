#!/usr/bin/python3
"""This module contains a function that opens a file"""


def read_file(filename=""):
    """
    Reads a file
    Args:
        filename: The name of the file to open/read
    """
    with open(filename, encoding="utf-8") as fo:
        print(fo.read(), end="")
        fo.close()
