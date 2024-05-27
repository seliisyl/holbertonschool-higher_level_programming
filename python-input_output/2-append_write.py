#!/usr/bin/python3
"""
   function file for append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and
    returns the number of characters added.

    Parameters:
    filename (str): The path to the file to be written to.
    Defaults to an empty string.
    text (str): The text to append to the file.
    Defaults to an empty string.

    Returns:
    int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
