#!/usr/bin/env python3
'''A coroutine that uses asynchronous comprehension to gather random numbers.'''
from typing import List
import asyncio
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using async comprehension over async_generator.'''
    return [number async for number in async_generator()]
