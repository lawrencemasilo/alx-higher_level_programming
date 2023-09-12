#!/usr/bin/python3
import json
"""
This module contains a function,
that converts a JSON string to an object
"""


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    Args:
        my_str: the str
    """
    obj = json.loads(my_str)
    return obj
