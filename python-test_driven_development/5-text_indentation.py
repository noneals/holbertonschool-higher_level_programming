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

    keep_space = False
    for char in text:
        # إذا كان الحرف السابق كان . ? : وهذا الحرف space → نخلي المسافة
        if keep_space is False or char != " ":
            print(char, end="")

        if char in ".?:":
            print()
            print()
            keep_space = True
        else:
            keep_space = False
