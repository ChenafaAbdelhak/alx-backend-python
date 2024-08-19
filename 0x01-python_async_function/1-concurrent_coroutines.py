#!/usr/bin/env python3
import asyncio
from typing import List
"""module to run multiple coroutines at same time"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that returns a list of delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    delays = await asyncio.gather(*tasks)
    return delays
