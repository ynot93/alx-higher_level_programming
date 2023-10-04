#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            uppercase_ch = chr(ord(ch) - ord('a') + ord('A'))
            print("{}".format(uppercase_ch), end='')
        else:
            print("{}".format(ch), end='')
    print()
