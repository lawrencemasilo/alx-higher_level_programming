#!/usr/bin/python3
"""
python3 -c 'print(__import__("square").__doc__)'
This directory contains a Square class
that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    print(__import__("square").MyClass.my_function.__doc__)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        print(__import__("square").my_function.__doc__)
        Args:
            id: Must be integer type only
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (
                f"[Square] ({self.id}) {self.get_x}/"
                f"{self.get_y} - {self.get_width}"
            )
    """@property
    def get_width(self):
        return self.__width

    @get_width.setter
    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def get_height(self):
        return self.__height

    @get_height.setter
    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height == value
            raise TypeError("width must be an integer")
    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) {self.__x}/"
                f"{self.__y} - {self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        if args is not None or Kwargs is not None:
            if len(args) > 0:
                super().__init__(args[0])
            if "id" in kwargs:
                super().__init__(kwargs["id"])

            if len(args) > 1:
                if not isinstance(args[1], int):
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]

            if "width" in kwargs:
                if not isinstance(kwargs["width"], int):
                    raise TypeError("width must be an integer")
                if kwargs["width"] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = kwargs["width"]

            if len(args) > 2:
                if not isinstance(args[2], int):
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = args[2]

            if "height" in kwargs:
                if not isinstance(kwargs["height"], int):
                    raise TypeError("height must be an integer")
                if kwargs["height"] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = kwargs["height"]

            if len(args) > 3:
                if not isinstance(args[3], int):
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[3]

            if "x" in kwargs:
                if not isinstance(kwargs["x"], int):
                    raise TypeError("x must be an integer")
                if kwargs["x"] <= 0:
                    raise ValueError("x must be >= 0")
                self.__x = kwargs["x"]

            if len(args) > 4:
                if not isinstance(args[4], int):
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[4]

            if "y" in kwargs:
                if not isinstance(kwargs["y"], int):
                    raise TypeError("y must be an integer")
                if kwargs["y"] <= 0:
                    raise ValueError("y must be >= 0")
                self.__y = kwargs["y"]
    """
