HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    return (num_eights(x // 10) if x > 10 else 0) + (1 if x % 10 == 8 else 0)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    # (-1) ** k
    def count(i,k):
        if i <= n:
            if num_eights(i) > 0 or i % 8 == 0: # 有 8
                return (-1) ** k + count(i + 1, k + 1)
            else:
                return (-1) ** k + count(i + 1, k)
        else:
            return 0
    return count(1, 0)

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n < 10:
        return 0
    else:
        all_but_last, last = n // 10, n % 10
        last_second = all_but_last % 10
        return missing_digits(all_but_last) + (last - last_second - 1 if last > last_second else 0)
    


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    def count(largest_coin, total):
        if total < 0:
            return 0
        if total == 0:
            return 1
        num = 1
        coin = next_largest_coin(1)
        if coin > largest_coin:
            return num
        num += count(coin, total - coin)# 5
        coin = next_largest_coin(coin)
        if coin > largest_coin:
            return num
        num += count(coin, total - coin)# 10
        coin = next_largest_coin(coin)
        if coin > largest_coin:
            return num
        num += count(coin, total - coin)# 25
        return num
    return count(25,total)
           
    


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # ??????
    return (lambda f: \
        (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))) \
            (lambda f: (lambda i: 1 if (i == 0) else i * f(i - 1)))

def f1(f):
    def f2(x):
        def f3(v):
            return x(x)(v)
        return f(f3)
    def f4(x):
        def f5(v):
            return x(x)(v)
        return f(f5)
    return f2(f4)
def f6(f):
    def f7(i):
        return 1 if i == 0 else i * f(i - 1)
    return f7

def func():
    return f1(f6)
        