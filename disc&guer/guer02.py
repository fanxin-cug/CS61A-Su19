def map_mut(f, L):
    """
    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    for i in range(len(L)):
        L[i]=f(L[i])

#t1=tree(1,[tree(5,[tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)])
#t2=tree(1,[tree(5,[tree(7)]),tree(3,[tree(9),tree(2)]),tree(6)])
def is_min_heap(t):
    """
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True
    """
    if is_leaf(t):
        return True
    else:
        lst=[]
        bl=[]
        for b in branches(t):
            lst+=[is_min_heap(b)]
            bl+=[label(b)]
        if all(lst) and label(t)<=min(bl):
            return True
        return False

def largest_product_path(tree):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    if not tree:
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        """
        lst=[]
        for b in branches(tree):
            lst+=[largest_product_path(b)]
        return label(tree)*max(lst)
        """
        return label(tree)*max([largest_product_path(b) for b in branches(tree)])

def contains(t, e):
    if is_leaf(t):
        if e == label(t):
            return True
        return False     
    else:
        lst=[]
        for b in branches(t):
            lst+=[contains(b, e)]
        if any(lst):
            return True
        else:
            if label(t)==e:
                return True
            else:
                return False

def max_tree(t):
    """
    >>> max_tree(tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))
    tree(9, [tree(7, [tree(7)]),tree(9,[tree(9),tree(4)]),tree(6)])
    """
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches= [max_tree(b) for b in branches(t)]
        new_label = max([label(b) for b in new_branches])
        return tree(new_label,new_branches)

#iterative
def level_order(tree):
    if not tree:
        return []
    current_level, next_level = [label(tree)], [tree]
    while next_level:
        find_next= []
        for b in next_level:
            find_next.extend(branches(b))
        next_level = find_next
        current_level.extend([label(t) for t in next_level])
    return current_level

#hard
def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        lst=[]
        for b in branches(t):
            for p in all_paths(b):
                lst+=[[label(t)]+p]
        return lst

# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])