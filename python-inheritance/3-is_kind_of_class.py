#!/usr/bin/python3
"""
This module defines a function to check object inheritance.
It demonstrates the concept of polymorphism inspection.
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
    # isinstance() checks if 'obj' is an instance of 'a_class'
    # OR any of its subclasses.
    return isinstance(obj, a_class
