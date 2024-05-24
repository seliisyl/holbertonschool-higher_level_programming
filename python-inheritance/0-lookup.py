#!/usr/bin/python3
"""
    Function file for lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Arguments:
    obj (class): The object to list.
     Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
