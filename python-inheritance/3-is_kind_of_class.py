#!/usr/bin/python3
"""
This module defines a function that checks object inheritance.
It is used to verify if an object is an instance of a class or its parent.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is an instance or inherited from a_class,
              otherwise False.
    """
    return isinstance(obj, a_class)
