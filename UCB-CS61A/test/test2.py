from math import sqrt

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def square_close_to_successor(guess):
    return aproxi_eq(guess ** 2, guess + 1)

def aproxi_eq(a, b, tolerance = 1e-3):
    return abs(a - b) < tolerance

def improve_test(i):
    phi = (1 + sqrt(5)) / 2
    assert aproxi_eq(i,phi),"phi differs from its approximation"


phi = improve(golden_update,square_close_to_successor, 0.1)


    