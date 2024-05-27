#!/usr/bin/python3
"""
   function for file load_from_json_file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    filename (str): The path to the JSON file from which
    the object should be loaded.

    Returns:
    any: The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
