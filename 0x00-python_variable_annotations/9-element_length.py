#!/usr/bin/env python3
"""
python3 -c
'print(__import__("9-element_length").__doc__)'
Annotate the below function’s parameters and return values with the appropriate types


Author: Oluwaseun Ayela 
"""

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("9-element_length").element_length.__doc__)'

    """
    return [(i, len(i)) for i in lst]
    python3 - c
    print(__import__("9-element_length").element_length.__doc__)'

