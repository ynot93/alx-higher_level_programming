#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns tuple with string length and first character."""
    if sentence == "":
        return (0, None)

    length = len(sentence)
    first = sentence[0]

    return (length, first)
