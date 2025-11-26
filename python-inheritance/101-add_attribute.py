#!/usr/bin/python3
"""
module defines a function that attempts to add a new attribute to an object.
It demonstrates checking object capabilities/mutability before assignment.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (any): The object to add the attribute to.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    # In Python, objects that allow arbitrary new attributes usually
    # have a __dict__ attribute. Built-in types (str, int) do not.
    # Slots are a special case, checking __dict__ covers the requirement here.
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    # If we passed the check, we use setattr to perform the injection
    setattr(obj, name, value)
