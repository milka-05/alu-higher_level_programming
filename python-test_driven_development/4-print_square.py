#!/usr/bin/python3
"""Module that defines print_square.

Prints a square with the character #.
"""


def print_square(size):
    """Print a square of size x size with the character #.

    Raises a TypeError if size is not an integer and a ValueError if
    size is less than 0."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
