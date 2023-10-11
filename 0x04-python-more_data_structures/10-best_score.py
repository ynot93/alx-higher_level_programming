#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest value"""
    if a_dictionary is None:
        return None

    max_score = 0

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_student = key
    return best_student
