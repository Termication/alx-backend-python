#!/usr/bin/env python3
'''Module for safely retrieving the first element of a sequence.
'''

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence if it exists, or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
