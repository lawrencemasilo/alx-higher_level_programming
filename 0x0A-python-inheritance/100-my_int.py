#!/usr/bin/python3
"""
This module contains a class that inherits from int class
"""


class MyInt(int):
    """
    Args:
        int: Base class
    """

    def __ne__(self, other):
        """returns oppsite of !="""
        oppsite_sign = super().__eq__(other)
        return oppsite_sign

    def __eq__(self, other):
        """"returns oppsite of =="""
        oppsite_sign = super().__ne__(other)
        return oppsite_sign
