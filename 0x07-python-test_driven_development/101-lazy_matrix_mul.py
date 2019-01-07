#!/usr/bin/python3
"""
lazy matrix multiplication using a module
more experience with unit testing
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    return matmul(m_a, m_b)
