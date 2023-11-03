#!/usr/bin/python3
"""
Print 2 new lines after these characters:'.', '?', ':'

"""


def text_indentation(text):
    """
    Prints new lines after certain conditions.

    Args:
        text(str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = text.strip()
    separators = [".", "?", ":"]
    result = []

    line = ""
    for char in sentences:
        line += char
        if char in separators:
            result.append(line.strip() + "\n\n")
            line = ""

    if line:
        result.append(line.strip())

    print("".join(result))
