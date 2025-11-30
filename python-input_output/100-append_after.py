#!/usr/bin/python3
"""
this module defines a function that inserts text into a file
based on a search string.
it demonstrates file parsing and modification logic.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing
    a specific string.

    args:
        filename (str): the name of the file to modify.
        search_string (str): the string to search for inside the file.
        new_string (str): the string to insert.
    """
    # read the original content
    # it uses readlines() to get a list of all lines
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    # processes the content and build the new list
    new_content = []
    for line in lines:
        new_content.append(line)
        if search_string in line:
            new_content.append(new_string)

    # writes the modified content back to the file
    # it uses "w" mode to overwrite the entire file
    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(new_content)
