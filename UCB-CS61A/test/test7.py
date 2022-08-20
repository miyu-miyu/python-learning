"""This test py file is to test the command `time` in shell

$ time python3 test7.py

"""

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

t = fib(20)
print(t)
