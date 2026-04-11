#!/usr/bin/env python3
"""
Module 0-async_generator
Defines an async coroutine async_generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop 10 times, each time wait 1 second asynchronously,
    then yield a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
