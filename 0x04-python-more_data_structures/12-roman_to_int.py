#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts roman numeral to integer"""
    if not isinstance(roman_string, str):
        return 0

    if roman_string is None:
        return 0

    roman_numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 100
            }
    result = 0
    prev = 0

    for num in reversed(roman_string):
        value = roman_numbers.get(num, 0)

        if value >= prev:
            result += value
        else:
            result -= value

        prev = value

    return result
