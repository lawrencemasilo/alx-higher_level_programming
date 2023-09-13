#!/usr/bin/python3
"""
This module contains a function,
that converts a JSON string to an object
"""
import json


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    Args:
        my_str: the str
    """
    obj = json.loads(my_str)
    return obj
