#!/usr/bin/python3
"""
   function file for text_indentation
"""


def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?' and ':'.
    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If the text is not a string.
    Examples:
        >>> text_indentation("Hello. How are you? Fine: thank you.")
    Hello.

    How are you?
    Fine:
    thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = {'.', '?', ':'}
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start
        while end < text_length and text[end] not in special_characters:
            end += 1
        print(text[start:end].strip(), end="")

        if end < text_length:
            print(text[end] + "\n")
            end += 1
        start = end
