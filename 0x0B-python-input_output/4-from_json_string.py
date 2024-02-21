#!/usr/bin/python3
"""json string module"""

from json import loads


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return loads(my_str)
