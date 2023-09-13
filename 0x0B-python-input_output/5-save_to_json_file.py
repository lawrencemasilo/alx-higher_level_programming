#!/usr/bin/python3
"""
This module contains a function converts a object to json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    returns JSON representation of an object
    Args:
        my_obj: the object
        filename: the file to be opened/created
    """
    with open(filename, "w", encoding="utf-8") as fo:
        json_obj = json.dumps(my_obj)
        fo.write(json_obj)
