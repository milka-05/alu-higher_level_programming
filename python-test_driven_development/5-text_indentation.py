#!/usr/bin/python3
"""Module that defines text_indentation.

Prints a text with 2 new lines after each of the characters . ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each . ? and : character.

    Raises a TypeError if text is not a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        line += c
        if c in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
