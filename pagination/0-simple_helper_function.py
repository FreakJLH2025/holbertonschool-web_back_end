#!/usr/bin/env python3
"""
Module 0-simple_helper_function
Defines a helper function index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: (start index, end index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
