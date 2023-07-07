#!/usr/bin/env python3
"""
python3 -c
'print(__import__("7-to_kv").__doc__)'
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

Author: Oluwaseun Ayela 
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("7-to_kv").to_kv.__doc__)'

    """
    return k, float(v) ** 2
    python3 - c
    print(__import__("7-to_kv").to_kv.__doc__)
