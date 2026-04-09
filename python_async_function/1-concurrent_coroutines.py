#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
Defines an async routine wait_n
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay and return delays in ascending order.

    Args:
        n (int): number of coroutines to spawn
        max_delay (int): maximum delay for wait_random

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
