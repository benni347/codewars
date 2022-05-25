#!/usr/bin/env python3
"""
Even or Odd
:worth = 8 kyu
:url   = https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
:tags  = algorithms, math, algorithms, fundamentals
"""
def even_or_odd(number: int) -> str:
    """
    :param number: The number to check.
    :return: "Even" if the number is even, and "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

