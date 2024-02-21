#!/usr/bin/python3
"""load from json file"""

from json import load


def load_from_json_file(filename):
    """crate and object from a "JSON file" """
    with open(filename, encoding="utf-8", mode="r") as file:
        return load(file)
