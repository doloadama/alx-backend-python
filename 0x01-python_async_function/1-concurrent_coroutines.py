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
    tasks = []
    for _ in range(n):
       task = wait_random(max_delay)
       tasks.append(task)
    return await asyncio.gather(*tasks)
