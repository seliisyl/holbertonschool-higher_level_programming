#!/usr/bin/python3
"""
    File function for read_file().
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
