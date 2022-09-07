#!/usr/bin/env python3
"""
Remove anchor from URL
:worth = 7 kyu
:url   = https://www.codewars.com/kata/51f2b4448cadf20ed0000386/
:tags  = Regular Expressions, Strings, Fundamentals
"""
import re


def remove_url_anchor(url):
    regex = r"\#.*"
    substr = ""
    result = re.sub(regex, substr, url, 0, re.MULTILINE)
    return result
