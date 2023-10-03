#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if value != ord('q') and value != ord('e'):
        print(f"{chr(value)}", end='')
