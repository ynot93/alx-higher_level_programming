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

    sentences = text.split('.')
    for sentence in sentences:
        questions = sentence.split('?')
        for item in questions:
            colons = item.split(':')
            for colon in colons:
                print(colon.strip())
            print()
