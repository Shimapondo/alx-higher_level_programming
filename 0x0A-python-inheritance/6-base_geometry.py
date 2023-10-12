#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
