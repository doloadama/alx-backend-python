#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float] :
    
    """
    Spawn wait_random n times with a delay between  each call
    """
    delays = []
    tasks = [asyncio.ensure_future(wait_random(max_delay)) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return sorted(delays)
