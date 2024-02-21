#!/usr/bin/python3
"""append text module"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
