"""
:URL: https://www.codewars.com/kata/5ace2d9f307eb29430000092/
"""


def modify_multiply(st, loc, num):
    org_str: str = st
    new_str: str = ""
    mod_str: str = st.split()

    new_str = (mod_str[loc] + "-") * num
    return new_str[:-1]
