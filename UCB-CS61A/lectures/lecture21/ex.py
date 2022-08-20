import email
from queue import Empty
from re import S


class Link:
    empty = () # a empty tuple
    def __init__(self, first , rest = empty):
        assert rest is Link.empty or isinstance(rest, Link),"The rest should be a link"
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link('+repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def square(x):
    return x ** 2

def odd(x):
    return x % 2 == 1

def range_link(start, end):
    """Return a Link containing consecutive integers from start to the end
    >>> range_link(3,6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s
    
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x) is a true value.

    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    elif f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)

def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s.
    不是重新建链表, 而是修改已有的链表"""
    if s is Link.empty:
        return Link(v)
    if s.first > v:
        return Link(v, s)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s