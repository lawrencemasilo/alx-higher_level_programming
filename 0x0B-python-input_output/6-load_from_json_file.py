#!/usr/bin/python3
"""
This module contains a function,
that converts a JSON string to an object
"""
import json


def load_from_json_file(filename):
    """
    returns a python object
    Args:
        filename: the file containing a Json string
    """
    with open(filename, "r", encoding="utf-8") as fo:
        obj = json.loads(fo.read())
    return obj
