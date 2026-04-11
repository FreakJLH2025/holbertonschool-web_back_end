#!/usr/bin/env python3
"""
Module 1-async_comprehension
Defines an async coroutine async_comprehension
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: list of 10 random floats
    """
    return [i async for i in async_generator()]
