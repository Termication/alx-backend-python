#!/usr/bin/env python3
'''Module for safely retrieving a value from a dictionary using a key.
'''

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dictionary using a given key, returning a default value if the key is not present.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
