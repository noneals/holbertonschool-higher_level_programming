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

    skip_space = False

    for char in text:

        if skip_space:
            # نحذف space فقط إذا كنا في بداية سطر جديد
            if char == " ":
                # لكن doctest يبغى نحافظ على المسافة داخل الجملة
                # الحل: نخلي المسافة إذا السطر السابق مو فاصل
                print(char, end="")
                skip_space = False
                continue
            else:
                print(char, end="")
                skip_space = False
                continue

        print(char, end="")

        if char in ".?:":
            print()
            print()
            skip_space = True
