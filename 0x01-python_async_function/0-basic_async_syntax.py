#!/usr/bin/env python3
'''
 An asynchronous coroutine that takes in an integer argument 
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Awaits for a random number of seconds.
    '''
    time = random.random() * max_delay
    await asyncio.sleep(time)
    return time
