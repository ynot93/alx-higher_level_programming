#!/usr/bin/python3
""" Determines the peak in a list of numbers """


def find_peak(list_of_integers):
    """
    Uses binary search to find peak.

    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        mid_num = list_of_integers[mid]

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
