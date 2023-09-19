#!/usr/bin/python3


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__') is True:
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
