def count(s, value):
    """Count the number of times that value occurs in 
    sequence s"""
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheers():
    for _ in range(3): # _ means that we would like never use such variable
        print("Go Bears!!!")

def mySum(l):
    total = 0
    for elm in l:
        total += elm
    return total

def mysum_r(l):
    if(l == []):
        return 0
    else:
        return l[0] + mysum_r(l[1:])

def divisors(n): # 列出 n 的真因子
    return [1] + [x for x in range(2, n) if n % x ==0]

# reverse a list
def reverse(l):
    length = len(l)
    for i in range(length // 2):
        temp = l[i]
        l[i] = l[length - 1 - i]
        l[length - 1 - i] = temp
    return l