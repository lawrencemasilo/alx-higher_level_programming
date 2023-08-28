#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {}".format(a / b), end="\n")
        except ZeroDivisionError:
            print("Inside result: {}".format(None), end="\n")
