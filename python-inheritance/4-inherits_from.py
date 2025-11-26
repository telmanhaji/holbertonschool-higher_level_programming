#!/usr/bin/python3
"""
This module defines a function to check strict subclass inheritance.
It is used to detect if an object is a derived instance, not the base class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is a subclass instance, False if exact class.
    """
    # 1. Check if it is 'a kind of' a_class (includes the class itself)
    # 2. AND Check if it is NOT exactly a_class
    return isinstance(obj, a_class) and type(obj) is not a_class
