def f():
    def g():
        i = 0
        while True:
            yield i
    yield g()