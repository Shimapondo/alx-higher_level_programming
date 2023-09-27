#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
