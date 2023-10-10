#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
