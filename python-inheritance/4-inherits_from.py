#!/usr/bin/python3
"""Module that defines a function inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class, else False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
