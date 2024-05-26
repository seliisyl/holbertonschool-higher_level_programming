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
            Validator for check the value.

            Arguments:
                name (str): Name of the value.
                value (int): Value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
