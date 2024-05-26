#!/usr/bin/python3
"""
    Class file for Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeomtry. """
    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne la représentat° en chaîne de caractères du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
