#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            ch = chr(ord(ch) - ord('a') + ord('A'))
        print("{}".format(ch), end='')
    print("")
