#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
  """_summary_

  Args:
      max_delay (int, optional): _description_. Defaults to 10.

  Returns:
      float: _description_
  """
  rand = await asyncio.sleep(random.uniform(0, max_delay))
  await asyncio.sleep(rand)
  return rand
