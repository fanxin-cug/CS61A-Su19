#constructor
def tree(label,branches=[]):
    """
    >>> tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    [3, [1], [2, [1], [1]]]
    """
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)

#selector
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

ex1 = tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])])

def count_nodes(t):
    """
    >>> count_nodes(ex1)
    9
    """
    if is_leaf(t):
        return 1
    else:
        total=0
        for b in branches(t):
            total+=count_nodes(b)
        return total+1

ex2 = tree('D', [tree('B', [tree('A'), tree('C')]), tree('F', [tree('E'), tree('H', [tree('G'), tree('I')])])])

def collect_leaves(t):
    """
    >>> collect_leaves(ex2)
    ['A', 'C', 'E', 'G', 'I']
    """
    if is_leaf(t):
        return [label(t)]
    else:
        lst=[]
        for b in branches(t):
            lst+=collect_leaves(b)
        return lst

def print_calls(name, f):
    def new_f(t):
        print('Name:', name)
        print('Inputted Tree:')
        print_tree(t)
        input()
        ret = f(t)
        print('Returned:', ret)
        return ret
    return new_f

def print_tree(t, indent=0):
    print(' '*indent,label(t))
    for b in branches(t):
        print_tree(b,indent+1)

def square_tree(t):
    """
    >>> square_tree(ex1)
    [64, [16, [4], [9]], [9, [1], [1, [1], [1]]]]
    """
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        lst=[]
        for b in branches(t):
            lst+=[square_tree(b)]
        return tree(label(t)**2,lst)

def fib_tree(n):
    """
    >>> print_tree(fib_tree(4))
    """
    if n<=1:
        return tree(n)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])