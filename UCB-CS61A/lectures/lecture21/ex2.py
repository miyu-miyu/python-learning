class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches = []) -> None:
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    
    def __repr__(self) -> str:
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def __str__(self) -> str:
        return '\n'.join(self.indented())

    def indented(self) -> list:
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
    
    def is_leaf(self) -> bool:
        return not self.branches

def fib_tree(n:int) -> Tree:
    if n == 0 or n == 1:
        return Tree(n)
    else:
        fib_left = fib_tree(n - 2)
        fib_right = fib_tree(n - 1)
        return Tree(fib_left.label + fib_right.label, [fib_left, fib_right])

def leaves(t:Tree) -> list:
    if t.is_leaf():
        return [t.label]
    else:
        leave_list = []
        for branch in t.branches:
            # leave_list[-1:-1] = leaves(branch) 
            # 切片只能插入在前面, 比如 -1 的前面, 0 的前面, 而不能插在 -1 的后面
            '''
            >>> l = []
            >>> l[-1:-1] = [1,2]
            >>> l
            [1, 2]
            >>> l[-1:-1]=[3,4]
            >>> l
            [1, 3, 4, 2]
            >>> l[-1:] = [3,4]
            >>> l
            [1, 3, 4, 3, 4]
            >>> l[0:0]=[5,6]
            >>> l
            [5, 6, 1, 3, 4, 3, 4]
            '''
            leave_list.extend(leaves(branch))
        return leave_list

def height(t: Tree) -> int:
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 1
    else:
        return 1 + max([height(b) for b in t.branches])

