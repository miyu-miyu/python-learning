def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.
    
    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [index for index in range(len(s)) if abs(s[index]) == min_abs]
    # return list(filter(lambda x: abs(s[x]) == min_abs, range(len(s))))

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.
    
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    assert len(s) >= 2
    # return max([s[i] + s[i+1] for i in range(len(s)-1)])
    # zip(s[:-1], s[1:])
    return max([a + b for a, b in zip(s[:-1], s[1:])])

def digit_dict(s):
    """Map each digit d to to the lists of elements in s that end with d.
    
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    # dict comprehensions
    #{key: value for ...}
    return {d:[x for x in s if x % 10 == d] for d in\
         range(10) if any([x % 10 == d for x in s])}

def all_have_an_equal(s):
    """Does every element equal some other element in s?
    
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    # s[i] in s[:i] + s[i+1:]
    # return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    # return 1 in [sum([1 for y in s if y == x]) for x in s]
    # s.count(element)
    return 1 in [s.count(x) for x in s]