#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
It demonstrates how to use inherited validation logic for attributes.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using the BaseGeometry framework.
    Inherits validation logic to ensure width and height are positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with validated private attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # 1. Validate the inputs using the inherited method
        # This uses the logic defined in BaseGeometry (Task 7)
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # 2. Assign to private attributes ONLY after validation passes
        self.__width = width
        self.__height = height
