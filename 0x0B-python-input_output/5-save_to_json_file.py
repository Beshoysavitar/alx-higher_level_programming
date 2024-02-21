#!/usr/bin/python3
"""save to json file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, encoding="utf-8", mode="w") as file:
                dump(my_obj, file)
