#!/usr/bin/python3
"""
   function file for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the class or its subclass;
    otherwise False.

    Parameters:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj against.

    Returns:
    bool: True if obj is an instance of or inherited from a_class,
    otherwise False.
    """
    return isinstance(obj, a_class)
