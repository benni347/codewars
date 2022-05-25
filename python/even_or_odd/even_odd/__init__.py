#!/usr/bin/env python3
def even_or_odd(number: int) -> str:
    """
    :param number: The number to check.
    :return: "Even" if the number is even, and "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

