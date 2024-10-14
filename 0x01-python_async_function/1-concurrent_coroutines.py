#!/usr/bin/env python3
'''Asynchronous utilities for random wait times.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronously waits for a random delay.

    Args:
        max_delay (int): The upper limit for the random wait time. Defaults to 10.

    Returns:
        float: The actual wait time in seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
