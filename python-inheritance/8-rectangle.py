#!/usr/bin/python3
"""
   function filr for BaseGeometry
"""


class BaseGeometry:
    """
    A class named BaseGeometry with a method that raises an exception.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.

        Parameters:
        name (str): The name associated with the value
        (assumed to be a string).
        value (any): The value to be validated.

        Raises:
        TypeError: If value is not an integer with the message
        '<name> must be an integer'.
        ValueError: If value is less than or equal to 0 with the message
        '<name> must be greater than 0'.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
