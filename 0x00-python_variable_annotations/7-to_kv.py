#!/usr/bin/env python3
from typing import Union, Tuple
"""complex types"""


def to_kv(k:str, v: Union[int, float]) -> Tuple[str, float]:
    """cast to tuple"""
    return (k, v**2)