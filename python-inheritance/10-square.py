#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
It demonstrates creating a specialized subclass.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits validation and visual representation from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): The size of the square side.
        """
        # 1. Validate the size using the method inherited from BaseGeometry
        self.integer_validator("size", size)

        # 2. Initialize the Parent (Rectangle)
        # We tell Rectangle: "My width is size, and my height is size"
        super().__init__(size, size)

        # 3. Store size specifically (Rectangle stores it as width/height)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2
