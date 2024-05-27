#!/usr/bin/python3
"""
   function file for write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and return
    s the number of characters written.

    Parameters:
    filename (str): The path to the file to be written to.
    Defaults to an empty string.
    text (str): The text to write to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
