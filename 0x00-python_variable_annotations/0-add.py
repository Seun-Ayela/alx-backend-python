#!/usr/bin/env python3
"""
python3 -c
'print(__import__("0-add").__doc__)'
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

Author: Oluwaseun Ayela 
"""


def add(a: float, b: float) -> float:
    return a + b
    """
    python3 -c
    'print(__import__("0-add").add.__doc__)'
    'print(__import__("0-add").MyClass.my_function.__doc__)'
    """
