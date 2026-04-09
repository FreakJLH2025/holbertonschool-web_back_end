#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
Defines an async coroutine wait_random
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    and return the delay value.

    Args:
        max_delay (int): maximum delay in seconds (default 10)

    Returns:
        float: the actual delay waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
