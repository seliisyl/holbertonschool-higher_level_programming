#!/usr/bin/env python3
"""
   function file for serialize_and_save_to_file
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
    data (dict): A Python Dictionary with data to be serialized.
    filename (str): The filename of the output JSON file.
    If the output file already exists, it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file to recreate
    the Python Dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: A Python Dictionary with the deserialized
    JSON data from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
