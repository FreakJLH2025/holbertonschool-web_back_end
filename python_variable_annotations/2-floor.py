#!/usr/bin/env python3
"""
Module 2-floor
Defines a type-annotated function floor
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): number to floor

    Returns:
        int: floor of n
    """
    return math.floor(n)
