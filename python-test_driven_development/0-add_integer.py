#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("") 

    if not isinstance(b, (int, float)):
        raise TypeError("")

    a = int(a)
    b = int(b)
    return a + b
