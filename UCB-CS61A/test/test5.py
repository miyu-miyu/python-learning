# consequence aggregation application 
# ex1. find perfect number less than 10000 except 1
def divisors(n):
    '''Return a list composed by the divisors of n
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    '''
    return [x for x in range(1,n) if n % x == 0]

def find_perfect(n):
    '''Return a list composed by all perfect numbers less than n except 1
    >>> find_perfect(1000)
    [6, 28, 496]
    '''
    return [x for x in range(2,n) if sum(divisors(x)) == x]

# ex2. to find the minimum perimeter of a rectangle with integer side lengths, given its area.
def rectangel_with_given_area(a):
    '''return a list composed by perimeters of rectangles with integer lenghts under the given area'''
    return [x for x in range(1, a+1) if a % x == 0] # 不是最优解

def minmum_perimeters(a):
    permiters = [2 * (a // x + x) for x in rectangel_with_given_area(a)]
    return min(permiters)