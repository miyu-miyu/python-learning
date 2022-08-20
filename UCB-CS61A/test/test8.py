def mfib():
    fib_lst = [0, 1]
    def fib(n:int) -> int:
        if n < len(fib_lst):
            return fib_lst[n]
        else:
            fib_lst.append(fib(n - 1) + fib(n - 2))
            return fib_lst[n]
    return fib


if __name__ == "__main__":
    f = mfib()
    print(f)
    while True:
        n = input("input a number: ")
        if n == 'q':
            break
        n = int(n)
        print("the {0}th fib number is {1}".format(n, f(n)))

