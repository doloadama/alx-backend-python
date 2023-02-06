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
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    return await asyncio.gather(*tasks)
