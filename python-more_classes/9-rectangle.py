#!/usr/bin/python3
"""
this module defines a class Square that inherits from Rectangle.
it demonstrates the power of inheritance to reuse code.
"""
# it must import the parent class to use it
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    represents a square.
    inherits all attributes and methods (validation, area) from Rectangle.
    """

    def __init__(self, size=0):
        """
        initializes the square.

        args:
            size (int): the size of the square. defaults to 0.
        """
        # attention!
        # it calls the Parent's (super) constructor.
        # rectangle expects (width, height).
        # it passes (size, size).
        # this automatically triggers all the validation logic in Rectangle!
        super().__init__(size, size)
