#!/usr/bin/env python3
  """
  4. Tasks
  """


import asyncio
from 3-tasks import task_wait_random


async def task_wait_n(n, max_delay):
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
