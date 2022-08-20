"""Generalization"""

from operator import mul
from math import pi, sqrt


def area(r, shape_constant):
    assert r > 0, "The length must be positive"
    return r ** 2 * shape_constant

def area_square(r):
    return area(r, 1) 

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, sqrt(3) * 3 / 2)

# Higher Order Functions

def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence
    >>> summation(5,cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total 

def sum_naturals(n):
    """Sum the first N natural numbers.
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

# Locally Defined Functions

def make_addr(n):
    """Return a function that takes one parameter K and return K + N.
    >>> add_three = make_addr(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return n + k
    return adder


# Return Statement

def search(f):
    """This is a higher order function""" 
    x = 0
    while True:
        if f(x):
            return x# return None 
        x += 1

def is_three(x):
    return x == 3

def square(x):
    return x ** 2

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x.
    就是反函数"""
    return lambda y: search(lambda x: f(x) == y) # y is a parameter, not a function intrinsic name

# Logical Operators -- short circuiting

def has_big_sqrt(x):
    return x >= 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1 / n != 0