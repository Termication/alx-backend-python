#!/usr/bin/env python3
'''Module for performing asynchronous comprehension to gather numbers.'''
from typing import List
from importlib import import_module as using

# Importing the async_generator function from the specified module
async_generator = using('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using asynchronous comprehension over async_generator.'''
    return [num async for num in async_generator()]
