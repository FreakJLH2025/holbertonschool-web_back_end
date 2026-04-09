#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Defines a type-annotated function sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): list containing integers and floats

    Returns:
        float: sum of the values in the list
    """
    return float(sum(mxd_lst))
