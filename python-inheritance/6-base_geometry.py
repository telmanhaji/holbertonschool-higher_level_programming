#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
It serves as a base class for other geometry classes.
"""


class BaseGeometry:
    """
    A class that defines the base geometry.
    """

    def area(self):
        """
        Raises an Exception because area() is not implemented yet.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
