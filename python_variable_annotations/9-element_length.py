#!/usr/bin/env python3
"""
Module 9-element_length
Defines a type-annotated function element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence],
) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): an iterable of sequences (like strings, lists, tuples)

    Returns:
        List[Tuple[Sequence, int]]: list of tuples (element, length of element)
    """
    return [(i, len(i)) for i in lst]
