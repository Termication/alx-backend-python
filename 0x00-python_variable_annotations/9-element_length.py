#!/usr/bin/env python3
'''Module for computing the lengths of sequences in an iterable.
'''

from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples, where each tuple contains a sequence
    and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each consisting of
        a sequence from the input and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
