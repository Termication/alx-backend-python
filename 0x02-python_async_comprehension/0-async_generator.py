#!/usr/bin/env python3
'''A coroutine that yields random numbers asynchronously.'''
import asyncio
import random

async def async_generator():
    '''Generates a sequence of 10 random numbers between 0 and 10 asynchronously.'''
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
