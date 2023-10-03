#!/usr/bin/python3

uppercase = False

for ch in range(ord('z'), ord('a') - 1, -1):
    letter = chr(ch)

    if uppercase:
        letter = letter.upper()

    print(f"{letter}", end="")
    uppercase = not uppercase
