#!/usr/bin/python3

def no_c(my_string):
    a = [i for i in my_string if i != 'c' and i != 'C']
    b = "".join(a)
    return b
