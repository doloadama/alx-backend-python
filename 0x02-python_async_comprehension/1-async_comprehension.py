#!/usr/bin/env python3
"""1-Async Comprehension
"""
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    collect 10 random numbers using an async comprehension over async_generator
    then return 10 random numbers
    """

    async for i in async_generator(10):
        print(i)
