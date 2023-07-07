#!/usr/bin/env python3
"""
python3 -c
'print(__import__("7-to_kv").__doc__)'
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

Author: Oluwaseun Ayela 
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Trying this docstring for this module
     python3 -c
     print(__import__("7-to_kv").to_kv.__doc__)

    """
    return k, float(v) ** 2
    python3 - c
    print(__import__("7-to_kv").to_kv.__doc__)
