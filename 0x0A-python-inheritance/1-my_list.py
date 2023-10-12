#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
