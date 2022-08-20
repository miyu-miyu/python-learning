def count_partitions(n, m):
    """The number of ways to partition n using integers up to m equals
        the number of ways to partition n-m using integers up to m, and # 至少有一个分成 m
        the number of ways to partition n using integers up to m-1. # 没有分成 m 的
        递归, 要全!!!
        base case 要想全
    """
    if n == 1 or n == 0 or m == 1:
        return 1
    elif n < 0 or m <= 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)

def inverse_cascade(n):
    k, num = 0, n
    while num != 0:
        k , num = k + 1, num // 10
    print_cascade(n, k-1)

def print_cascade(n, k):
    if k == 0:
        print(n // 10 ** k)
    elif k > 0:
        print(n // 10 ** k)
        print_cascade(n, k - 1)
        print(n // 10 ** k)

towers = ["A", "B", "C"]

def move(start, end):
    print(towers[start], '->', towers[end])

def solve(n, start, end):
    if n == 1:
        move(start, end)
    else: 
        spare = 3 - start - end # 怎么通过已知的两个塔算出第三个空闲的塔!!!
        solve(n - 1, start,spare)
        move(start, end)
        solve(n-1, spare, end)

def Hanoi(n):
    solve(n, 0, 2)

