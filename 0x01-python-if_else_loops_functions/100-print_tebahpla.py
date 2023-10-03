#!/usr/bin/python3

uppercase = False

for ch in range(ord('z'), ord('a') - 1, -1):
    letter = chr(ch - (32 if uppercase else 0))
    print(f"{letter}", end="")
    uppercase = not uppercase
