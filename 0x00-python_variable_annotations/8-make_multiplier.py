#!/usr/bin/env python3
'''Module for creating a multiplier function.
'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies its input by a specified multiplier.

    Args:
        multiplier (float): The number by which to multiply the input.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product of its input and the multiplier.
    '''
    return lambda x: x * multiplier
