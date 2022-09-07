#!/usr/bin/env python3
"""
Get Planet by ID
:worth =  8   kyu
:url   =  https://www.codewars.com/kata/515e188a311df01cba000003/  
:tags  =  Debugging
"""


def get_planet_name(planet_id):
    # This doesn't work; Fix it!
    if planet_id == 1:
        return "Mercury"
    if planet_id == 2:
        return "Venus"
    if planet_id == 3:
        return "Earth"
    if planet_id == 4:
        return "Mars"
    if planet_id == 5:
        return "Jupiter"
    if planet_id == 6:
        return "Saturn"
    if planet_id == 7:
        return "Uranus"
    if planet_id == 8:
        return "Neptune"


# The code below isn't mine but it is the best practice.
# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)
