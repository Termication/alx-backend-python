#!/usr/bin/env python3
'''Module for measuring the runtime of asynchronous comprehensions.'''

import asyncio
import time
from importlib import import_module as using

# Importing the async_comprehension function from the specified module
async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''Measures the total runtime of executing async_comprehension 4 times concurrently.'''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
