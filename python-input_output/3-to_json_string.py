#!/usr/bin/python3
"""Module that defines a function to_json_string."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
