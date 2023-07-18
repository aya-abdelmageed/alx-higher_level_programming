#!/usr/bin/python3
"""derived class"""


class MyList(list):
    """class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
