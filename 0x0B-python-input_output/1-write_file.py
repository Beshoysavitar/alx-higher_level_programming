#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
     """write_file"""
     with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
