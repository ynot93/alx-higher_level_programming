#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num = len(sys.argv) - 1

    if num == 1:
        print("{} argument:".format(num))
    elif num == 0:
        print("{} arguments.".format(num))
    else:
        print("{} arguments:".format(num))

    if num > 0:
        for count in range(1, num + 1):
            print("{}: {}".format(count, sys.argv[count]))
