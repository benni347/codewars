"""
URL: https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/
"""

def generate_shape(n):
    solve_str = ""
    for i in range(n):
        solve_str += "+" * n + "\n"
    solve_str = solve_str[:-1]
    return solve_str
