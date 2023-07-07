#!/usr/bin/env python3
"""
python3 -c
'print(__import__("5-sum_list").__doc__)'
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

Author: Oluwaseun Ayela 
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Trying this docstring for this module
     python3 -c
     'print(__import__("5-sum_list").sum_mixed_list.__doc__)'

    """
    return sum(mxd_lst)
    python3 - c
    print(__import__("5-sum_list").sum_mixed_list.__doc__)
