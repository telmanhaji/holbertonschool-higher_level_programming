#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
It overrides the string representation to properly identify as a Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle but provides specific string representation.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): The size of the square side.
        """
        # 1. Validate inputs using the inherited method
        self.integer_validator("size", size)

        # 2. Initialize the Parent
        super().__init__(size, size)

        # 3. Store size for local use in __str__ and area
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
            str: '[Square] <width>/<height>'
        """
        # We override the parent's __str__ method.
        # Instead of [Rectangle], we explicitly say [Square].
        return "[Square] {}/{}".format(self.__size, self.__size)
