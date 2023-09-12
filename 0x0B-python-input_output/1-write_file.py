#!/usr/bin/python3
"""This module contains a function that opens a file"""


def write_file(filename="", text=""):
    """
    Writes to file
    Args:
        filename: The name of the file to open/read
        text: The content to be added to a file
    """
    with open(filename, mode="r+", encoding="utf-8") as fo:
        fo.write(text)
        characters = len(text)
        fo.close()
        return characters
