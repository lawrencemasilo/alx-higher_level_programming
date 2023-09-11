#!/usr/bin/python3
"""
This module contains a subclass
"""


class MyList(list):
    """
    parameter a: inherits from list
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
