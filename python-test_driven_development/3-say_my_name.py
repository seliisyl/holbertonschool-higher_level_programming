#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    '''
    Prints "My name is <first name> <last name>".

    Parameters:
    first_name (str): The first name.
    last_name (str): The last name (optional).

    Exceptions:
    TypeError: If first_name or last_name are not strings.
    '''
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print(f"My name is {first_name} {last_name}")
