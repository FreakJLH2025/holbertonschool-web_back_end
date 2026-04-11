#!/usr/bin/env python3
"""
Module async_generator
Defines an asynchronous generator that yields random numbers
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generate 10 random float numbers between 0 and 10.

    Each iteration waits asynchronously for 1 second
    before yielding the next number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        
