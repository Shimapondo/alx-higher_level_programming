#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
