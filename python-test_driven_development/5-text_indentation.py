#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for ch in text:
        if new_line and ch == " ":
            continue

        print(ch, end="")

        if ch in ".?:":
            print()
            print()
            new_line = True
        else:
            new_line = False
