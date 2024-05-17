#!/usr/bin/python3
"""Defines a square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, opti): The square's position. Default is (0, 0).

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square with '#' characters."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
