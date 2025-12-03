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

    new_line = False  # نعرف إننا في بداية سطر جديد بعد فاصل

    for char in text:

        # إذا بداية سطر جديد وهذا الحرف space → تجاهله
        if new_line and char == " ":
            continue

        print(char, end="")

        # إذا الحرف هو من الفواصل المطلوبة
        if char in ".?:":
            print()
            print()
            new_line = True  # الآن السطر الجديد يبدأ
        else:
            new_line = False
