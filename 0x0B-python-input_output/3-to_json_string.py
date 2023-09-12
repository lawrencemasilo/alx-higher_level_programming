#!/usr/bin/python3
import json
"""This module contains a function converts a object to json"""


def to_json_string(my_obj):
    """
    returns JSON representation of an object
    Args:
        my_obj: the object
    """
    json_obj = json.dumps(my_obj)
    return json_obj
