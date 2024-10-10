#!/usr/bin/env python3
'''Module for computing the sum of a list
containing both integers and floating-point numbers.
'''

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floating-point numbers.

    Returns:
        float: The sum of the numbers in the list as a floating-point value.
    '''
    return float(sum(mxd_lst))
