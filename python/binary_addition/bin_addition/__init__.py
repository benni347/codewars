#!/usr/bin/env python3
"""
:worth = 7 kyu
:url   = https://www.codewars.com/kata/551f37452ff852b7bd000139/
:tags  = fundamentals, binary
"""


def add_binary(a: int, b: int) -> str:
    """
    Function that adds two binary numbers
    :param a: first number
    :param b: second number
    :return: sum of the two numbers in binary as a string
    """
    return str(bin(a + b)[2:])
