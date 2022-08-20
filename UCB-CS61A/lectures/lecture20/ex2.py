from operator import getitem


class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return "Ratio({0}, {1})".format(self.numer, self.denom)

    def __str__(self):
        return "{0}/{1}".format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int): #type(other) == int:
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + other.numer * self.denom
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)
    # 仅完成__add__, 只能实现 Ratio + int, 但是不能实现 int + Ratio, 还需要完成 __radd__
    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom
    
def gcd(a, b):
    while a % b:
        t = b
        b = a % b
        a = t
    return b

# 可以在类外为类添加方法和属性
Ratio.__bool__ = lambda self: not self.numer == 0 
Ratio.bb = True

# 也可以在定义了实例后, 为实例单独添加属性
'''
>>> r = Ratio(1,2)
>>> r.bb
True
>>> r.cc = 2
>>> r.cc
2
'''
