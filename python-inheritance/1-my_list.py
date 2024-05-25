#!/usr/bin/python3
"""
    Class file for MyList.
"""


class MyList(list):
    """
        MyList class inherits from list.
    """
    def print_sorted(self):
        """
            Prints the list sorted ascending.
        """
        _copy_list = self[:]
        _copy_list.sort()
        print(str(_copy_list))
