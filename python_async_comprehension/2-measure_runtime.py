#!/usr/bin/env python3
"""
Module 2-measure_runtime
Defines a coroutine measure_runtime
"""

import asyncio
import time
from typing import Union
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Union[float, int]:
    """
    Run async_comprehension four times in parallel and measure total runtime.

    Returns:
        float: total runtime in seconds
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
