# higher_order function
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x ** 2

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# self reference
def print_sums(n):
    """
    >>> print_sums(1)(3)(5)
    1
    4
    9
    """
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

# currying

from operator import add

def curry1(f):
    def func1(a):
        def func2(b):
            return f(a, b)
        return func2
    return func1

def uncurry1(func1):
    def f(x, y):
        return func1(x)(y)
    return f
