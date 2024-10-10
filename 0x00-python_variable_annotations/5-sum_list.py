#!/usr/bin/env python3
'''Module for computing the sum of a list of floating-point numbers.
'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of a list of floating-point numbers.
    
    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list as a floating-point value.
    '''
    return float(sum(input_list))
