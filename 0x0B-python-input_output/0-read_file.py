#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


def read_file(filename=""):
    """Read file and print lines
    Args:
        filename (str): string of path to file

    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    read_file("my_file_0.txt")
