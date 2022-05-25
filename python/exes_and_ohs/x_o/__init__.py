#!/usr/bin/env python3
"""
Exes and Ohs
:worth = 7 kyu
:url   = https://www.codewars.com/kata/55908aad6620c066bc00002a
:tags  = Fundamentals
"""


def xo(s: str) -> bool:
    """
    Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case-insensitive.
    The string can contain any char.
    :param s:
    :return:
    """
    return s.lower().count('x') == s.lower().count('o')
