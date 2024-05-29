#!/usr/bin/env python3
"""
   function file for serialization convert_csv_to_json
"""

import json
import pickle

class CustomObject:

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod

    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            instance = pickle.load(file)
        return instance
