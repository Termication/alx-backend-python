#!/usr/bin/env python3
'''Module for Task 4, executing multiple asynchronous tasks.
'''

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes the task_wait_random function n times and returns sorted wait times.

    Args:
        n (int): The number of times to execute the task.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A sorted list of wait times for the executed tasks.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
