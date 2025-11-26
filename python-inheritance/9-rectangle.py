#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
It implements the area method and custom string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    Inherits validation from BaseGeometry and implements specific area logic.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with validated private attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # 1. Validate inputs using the inherited method from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # 2. Assign to private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        # We override the parent's area() method to provide actual logic
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the standard string representation of the rectangle.

        Returns:
            str: '[Rectangle] <width>/<height>'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
