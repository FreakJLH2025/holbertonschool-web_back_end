#!/usr/bin/env python3
"""
Module 2-measure_runtime
Provides a coroutine that measures the runtime of
executing async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel and measure runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
