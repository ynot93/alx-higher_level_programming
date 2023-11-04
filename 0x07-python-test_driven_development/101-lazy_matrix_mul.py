#!/usr/bin/python3
"""
This module uses NumPy to multiply matrices.

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices using NumPy.

    Returns:
        Result of multiplication.

    """
    result = np.matmul((m_a), (m_b))
    return result
