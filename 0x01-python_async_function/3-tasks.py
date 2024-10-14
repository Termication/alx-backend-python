#!/usr/bin/env python3
'''Module for Task 3, creating asynchronous tasks.
'''

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asynchronous task for the wait_random function.

    Args:
        max_delay (int): The maximum delay for the wait_random task.

    Returns:
        asyncio.Task: The created asynchronous task.
    '''
    return asyncio.create_task(wait_random(max_delay))
