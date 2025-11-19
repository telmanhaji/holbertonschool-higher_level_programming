#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list.
    """
    # 1st. Creates a copy of the original list immediately.
    # Should use the slicing syntax [:] to clone the list.
    new_list = my_list[:]

    # 2nd. Checks if the index is valid
    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list

    # 3rd. If valid, makes the change ONLY to the new_list
    new_list[idx] = element

    # 4th. Return the modified copy
    return new_list
