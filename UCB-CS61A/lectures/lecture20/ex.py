from doctest import ELLIPSIS_MARKER


class Bear:
    """A Bear."""
    def __init__(self):
        # 下面两个是 instance functions
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this is a bear'

    # 下面两个是 class functions, 使用 str(instance) 和 repr(instance) 会调用下面两个
    def __repr__(self): # 不要写成了 __rper__
        return 'Bear()'

    def __str__(self):
        return 'A bear'
        
oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

# python 内建的 str 和 repr 的实现
def repr(x):
    # type(x) 可以提取出 x 的类
    return type(x).__repr(x)

def str(x):
    t = type(x)
    if hasattr(t,'__str__'):
        return t.__str__(x)
    else:
        return repr(x)