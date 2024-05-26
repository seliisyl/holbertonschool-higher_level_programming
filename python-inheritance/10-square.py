#!/usr/bin/python3
"""
    Class file for Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Initialise un nouveau Square.

        Args:
            size (int): La taille du carré (côté du carré).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size
