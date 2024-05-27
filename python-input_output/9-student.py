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
        Initializes the Student instance with first_name, last_name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
        dict: A dictionary containing the attributes of the Student.
        """
        return self.__dict__
