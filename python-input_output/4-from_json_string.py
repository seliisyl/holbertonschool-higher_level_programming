#!/usr/bin/python3
"""
   function file for from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Parameters:
    my_str (str): The JSON string to be converted to a Python object.

    Returns:
    any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
