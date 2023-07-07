#!/usr/bin/env python3
"""
python3 -c
'print(__import__("100-safe_first_element").__doc__)'
Augment the following code with the correct duck-typed annotations:


Author: Oluwaseun Ayela 
"""

from typing import Optional, TypeVar

T = TypeVar('T')


def safe_first_element(lst: Optional[T]) -> Optional[T]:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("100-safe_first_element").safe_first_element.__doc__)'

    """
    if lst:
        return lst[0]
    else:
        return None
    python3 - c
    print(__import__("100-safe_first_element").safe_first_element.__doc__)
