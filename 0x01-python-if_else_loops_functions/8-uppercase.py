#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            uppercase_ch = chr(ord(ch) - ord('a') + ord('A'))
            print(f"{uppercase_ch}", end='')
        else:
            print(f"{ch}", end='')
    print()
