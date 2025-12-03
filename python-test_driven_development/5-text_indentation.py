#!/usr/bin/python3
"""Text indentation module.

This module defines a function `text_indentation` that prints a text
with two new lines after each occurrence of '.', '?' and ':'.
"""

def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for ch in text:
        # If we just started a new line, skip any leading spaces
        if new_line and ch == " ":
            continue

        print(ch, end="")

        if ch in ".?:":
            print()
            print()
            new_line = True
        else:
            new_line = False
