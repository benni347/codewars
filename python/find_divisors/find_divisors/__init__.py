#!/usr/bin/env python3
"""
Find the Divisors!
:worth = 7 kyu
:url   = https://www.codewars.com/kata/544aed4c4a30184e960010f4
:tags  = Algorithms, mathematics, numbers
"""


def divisors(integer):
    """
    Find the divisors of an integer and if prime return integer is prime.
    :param integer:
    :return:
    """
    divisors_list = []
    for i in range(1, integer):
        if integer % i == 0:
            divisors_list.append(i)
    if len(divisors_list) == 1:
        return f"{integer} is prime"
    # remove 1 from divisors_list
    divisors_list.remove(1)
    return divisors_list
