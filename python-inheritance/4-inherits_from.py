#!/usr/bin/python3
"""
   function file for def inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Parameters:
    obj (any): The object to check.
    a_class (type): The class to match against the type of obj.

    Returns:
     bool: True if obj is an instance of a subclass of a_class,
    otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
