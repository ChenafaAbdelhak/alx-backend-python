#!/usr/bin/env python3
from typing import Callable
"""module for make_multiplier function"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float"""
    def mult(n: float) -> float:
        """multiplies a float"""
        return n * multiplier
    return mult