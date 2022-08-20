def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def count(f):
    """Return a function to record the time the parameter function called"""
    def counted(n):
        counted.call_count += 1 
        return f(n)
    counted.call_count = 0 # 为函数对象添加一个属性
    return counted

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

fib = count(fib) # 名字不能改
