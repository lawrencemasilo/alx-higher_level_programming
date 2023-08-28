#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except ZeroDivisionError as ze:
        sys.stderr.write("Exception: {}\n".format(ze))
        return None
