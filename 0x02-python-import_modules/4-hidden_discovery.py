#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    names = dir()

    f_names = [n for n in names if not n.startswith("__")]

    sorted_names = sorted(f_names)

    for name in sorted_names:
        print(name)
