#!/usr/bin/python3
class Square:
    """
    this module defines a square
    """
    def __init__(self, size):
        """
        it initializes the square.
        args:
            size (int): the size of the square.
        """
        # assigning the incoming 'size' to the private attribute '__size'
        # the double underscore (__) makes it private.
        self.size = size
