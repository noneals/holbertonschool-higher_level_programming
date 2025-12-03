#!/usr/bin/python3
"""
Defines text_indentation
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text:
        if new_line and char == " ":
            continue  # Skip leading spaces
        new_line = False

        print(char, end="")

        if char in ".?:":
            print()
            print()
            new_line = True
