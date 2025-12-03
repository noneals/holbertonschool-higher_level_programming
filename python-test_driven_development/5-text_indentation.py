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

    i = 0
    length = len(text)

    while i < length:
        ch = text[i]
        print(ch, end="")

        if ch in ".?:":
            print()
            print()


            space_count = 0
            j = i + 1
            while j < length and text[j] == " ":
                space_count += 1
                j += 1


            if space_count > 0:
                print(" ", end="")

            i = j - 1  
        i += 1
