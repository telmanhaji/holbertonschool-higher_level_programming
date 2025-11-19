#!/usr/bin/python3
"""
Replaces an element in a list at a specific position
without modifying the original list
"""
# 1st. Creating a copy of the original list immediately.
# Using the slicing syntax [:] to clone the list
new_list = my_list [:]

# 2nd. Checking if the index is valid
if idx < 0:
    return new_list
if idx >= len (my_list):
    return new_list
# 3rd. If valid, making the change ONLY to the new_list
new_list[idx] = element

# 4th. Returning the modified copy
return new_list