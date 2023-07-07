#!/usr/bin/env python3
"""
python3 -c
'print(__import__("101-safely_get_value).__doc__)'
Given the parameters and the return values, add type annotations to the function

Author: Oluwaseun Ayela 
"""

from typing import Dict, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("101-safely_get_value").safely_get_value.__doc__)'

    """
    if key in dct:
        return dct[key]
    else:
        return default
    python3 - c
    print(__import__("101-safely_get_value").safely_get_value.__doc__)
