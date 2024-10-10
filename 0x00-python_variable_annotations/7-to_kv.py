#!/usr/bin/env python3
'''Module for converting a key-value pair to a tuple with the square of the value.
'''

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple consisting of a string key and the square of its associated value.

    Args:
        k (str): The key represented as a string.
        v (Union[int, float]): The value which can be either an integer or a floating-point number.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of the value as a float.
    '''
    return (k, float(v ** 2))
