#!/usr/bin/python3
"""Module that defines add_integer.

Adds two integers or floats, casting floats to integers.
Raises a TypeError if an argument is not a number.
"""


def add_integer(a, b=98):
    """Add two integers.

    Returns the sum of a and b as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
