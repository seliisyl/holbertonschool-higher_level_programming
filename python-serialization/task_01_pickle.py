#!/usr/bin/env python3
"""
   function file for serialization convert_csv_to_json
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a new instance of CustomObject.

        :param name: Name of the object (string)
        :param age: Age of the object (integer)
        :param is_student: Whether the object represents a student (boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject to a file.

        :param filename: Name of the file where the object will be saved
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.

        :param filename: Name of the file from which the object will be loaded
        :return: An instance of CustomObject if successful, otherwise None
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            return None
