#!/usr/bin/env python3
  """
  3. Tasks
  """
import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay):
    """_summary_

    Args:
        max_delay (_type_): _description_

    Returns:
        _type_: _description_
    """
      task = asyncio.create_task(wait_random(max_delay))
      return task
