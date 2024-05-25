#!/usr/bin/python3
"""
   function for file is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class,
    otherwise False.

    Parameters:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj against.

    Returns:
    bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
