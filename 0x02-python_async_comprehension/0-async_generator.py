#!/usr/bin/env python3
"""
0-Async Generator
"""
import asyncio
import random
from typing import List

async def async_generator() -> List[float]:
    """loop 10 times, each time asynchronously
    wait 1 second, then yield a random number
    between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
