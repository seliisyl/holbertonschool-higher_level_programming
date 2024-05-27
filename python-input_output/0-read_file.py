#!/usr/bin/python3
"""
    File function for read_file().
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Parameters:
    filename (str): path to the file to be read. Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
