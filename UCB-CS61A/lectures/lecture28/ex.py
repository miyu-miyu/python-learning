from ast import expr_context
from mimetypes import init
from tkinter import Y


def invert(x):
    y = 1 / x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as z:
        print('handled', z)
        return 0
    except NameError as n:
        print('handled', n)
        return None

from operator import truediv, mul, add

def reduce(f, s, initial):
    """Combine elements of s pairwise using f starting with initial.
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for i in s:
        initial = f(initial, i)
    return initial

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')