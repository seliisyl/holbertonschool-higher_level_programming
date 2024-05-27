#!/usr/bin/python3
"""
   function file for to_json
"""


class Student:
    """
    Defines a Student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first_name,
        last_name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attribute names contained
        in this list will be retrieved.
        Otherwise, all attributes will be retrieved.

        Parameters:
        attrs (list): A list of attribute names
        to retrieve (default is None).

        Returns:
        dict: A dictionary containing the specified
        attributes of the Student.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
