#!/usr/bin/env python3
"""module task_wait_random"""
import asyncio
from typing import Type

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Type[asyncio.Task]:
    """Function that returns a task object"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
