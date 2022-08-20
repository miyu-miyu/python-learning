def fib(n):
    if n <= 0:
        return "the parameter is a invalid value"
    elif n == 1:
        return 0
    elif n == 2:
        return 1;
    else:
        pre, cur = 0, 1
        k = 2;
        while k < n:
            pre, cur =cur, pre + cur
            k += 1
        return cur

def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
