#!/usr/bin/python3
"""
    File for the class Rectangle.
"""


class Rectangle:
    """
        Class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
            Initialization of the Rectangle class.
            Arguments:
                width (int, optional): Width of the rectangle.
                height (int, optional): Height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
            Get the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter of the width of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the height of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter of the height of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
