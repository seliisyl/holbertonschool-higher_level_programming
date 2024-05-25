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
