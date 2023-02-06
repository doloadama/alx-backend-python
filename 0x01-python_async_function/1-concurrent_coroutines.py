#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_
    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await t for t in asyncio.as_completed(tasks)]
    return sorted(delays)
