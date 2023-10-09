#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns tuple with string length and first character."""
    length = len(sentence)

    if sentence == "":
        first = None

    first = sentence[0]

    return (length, first)
