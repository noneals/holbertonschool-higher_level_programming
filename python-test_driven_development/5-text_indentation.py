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

            # إذا كان فيه مسافة واحدة بعدها—اطبعيها
            if i + 1 < length and text[i + 1] == " ":
                print(" ", end="")
                i += 1  # نتخطى هذي المسافة
        i += 1
