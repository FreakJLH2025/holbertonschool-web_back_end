#!/usr/bin/env python3
"""
Module 7-to_kv
Defines a type-annotated function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string k
    and the second element is the square of v as a float.

    Args:
        k (str): the string key
        v (Union[int, float]): the value to square

    Returns:
        Tuple[str, float]: (k, v squared as float)
    """
    return (k, float(v ** 2))
