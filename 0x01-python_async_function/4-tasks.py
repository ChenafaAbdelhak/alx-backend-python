#!/usr/bin/env python3
"""module to run multiple coroutines at same time"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function that returns a list of delays"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    delays = await asyncio.gather(*tasks)
    return sorted(delays)