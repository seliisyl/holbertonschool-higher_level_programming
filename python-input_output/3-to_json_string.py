#!/usr/bin/python3
"""
   function file for to_json_string
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Parameters:
    my_obj (any): The object to be serialized to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
