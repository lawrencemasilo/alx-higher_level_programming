#!/usr/bin/python3
"""This module contains a function that opens a file"""


def append_write(filename="", text=""):
    """
    appends to file
    Args:
        filename: The name of the file to open/read/write
        text: The content to be added to a file
    """
    with open(filename, mode="a", encoding="utf-8") as fo:
        fo.write(text)
        characters = len(text)
        fo.close()
        return characters
