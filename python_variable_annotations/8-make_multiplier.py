#!/usr/bin/env python3
"""
Module 8-make_multiplier
Defines a type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): the multiplier value

    Returns:
        Callable[[float], float]: function that takes a float and returns float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
