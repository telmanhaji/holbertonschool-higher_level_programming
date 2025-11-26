#!/usr/bin/python3
"""
This module defines a rebel integer class MyInt.
It demonstrates operator overloading to invert equality checks.
"""


class MyInt(int):
    """
    A class that inherits from int but inverts the == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.

        Args:
            other (int): The value to compare against.

        Returns:
            bool: False if values are equal, True otherwise.
        """
        # The standard behavior of == is actually the behavior of !=
        # So we return the result of the PARENT's inequality check.
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.

        Args:
            other (int): The value to compare against.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        # The standard behavior of != is actually the behavior of ==
        # So we return the result of the PARENT's equality check.
        return super().__eq__(other)
