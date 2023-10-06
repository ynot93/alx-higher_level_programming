#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_sum = 0
    for arg in sys.argv[1:]:
        arg_sum += int(arg)
    print("{}".format(arg_sum))
