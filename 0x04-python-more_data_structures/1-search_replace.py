#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda last: replace if last == search else last, my_list))
