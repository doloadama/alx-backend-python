#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (_type_): _description_
        max_delay (_type_): _description_

    Returns:
        _type_: _description_
    """
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
