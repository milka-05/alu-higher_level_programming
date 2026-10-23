#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)

    if count == 1:
        print("{} argument:".format(count))
    elif count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
