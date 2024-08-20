#!/usr/bin/env python3
"""module thats waits for a random delay"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """function that sleeps for random"""
    random_number = random.uniform(0.0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
