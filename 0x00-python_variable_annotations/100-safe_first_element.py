#!/usr/bin/env python3

from typing import Optional, TypeVar

T = TypeVar('T')


def safe_first_element(lst: Optional[T]) -> Optional[T]:
    if lst:
        return lst[0]
    else:
        return None
