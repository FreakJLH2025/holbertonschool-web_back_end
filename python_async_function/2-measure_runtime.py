#!/usr/bin/env python3
"""
Module 2-measure_runtime
Defines a function measure_time
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> Union[float, int]:
    """
    Measure total execution time for wait_n(n, max_delay)
    and return average time per coroutine.

    Args:
        n (int): number of coroutines
        max_delay (int): maximum delay

    Returns:
        float: average execution time per coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
