#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    This module deletes an element from the list
    at a specific position. Returns teh same
    list, modified.
    """
    list_len = len(my_list)

    # 1st. Safety check (negative oa out of range)
    if idx < 0 or idx >= list_len:
        return my_list

    # 2nd. Deletion (if safe)
    # 'del' keyword performs the removal directly from the list
    del my_list[idx]

    # 3rd. return the modified list
    return my_list
