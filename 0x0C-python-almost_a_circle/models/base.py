#!/usr/bin/python3
"""
python3 -c 'print(__import__("base").__doc__)'
The base class for all classes in this project
"""


class Base():
    """
    print(__import__("my_module").MyClass.my_function.__doc__)
    manages id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        print(__import__("my_module").my_function.__doc__)
        assigns the public instance attribute id,
            with the argument value,
            or the private class attribute __nb_objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
