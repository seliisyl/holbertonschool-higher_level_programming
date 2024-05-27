#!/usr/bin/python3
"""
   function file for save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Parameters:
    my_obj (any): The object to be serialized to JSON and saved to the file.
    filename (str): The path to the file where the object should be saved.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
