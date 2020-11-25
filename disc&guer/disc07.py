#Linked Lists
#1.1
"""
Write a function that takes in a Python list of linked lists and multiplies them
element-wise. It should return a new linked list.
If not all of the Link objects are of equal length, return a linked list whose length is
that of the shortest linked list given. You may assume the Link objects are shallow
linked lists, and that lst of lnks contains at least one linked list.
"""
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    if Link.empty in lst_of_lnks:
        return Link.empty
    else:
        ans=1
        for i in range(len(lst_of_lnks)):
            ans*=lst_of_lnks[i].first
            lst_of_lnks[i]=lst_of_lnks[i].rest
        return Link(ans,multiply_lnks(lst_of_lnks))

#1.2
"""
Write a function that takes a sorted linked list of integers and mutates it so that
all duplicates are removed.
"""
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    #iterative
    """
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        if lnk.first==lnk.rest.first:
            lnk.rest=lnk.rest.rest
        else:
            lnk=lnk.rest
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    else:
        if lnk.first==lnk.rest.first:
            lnk.rest=lnk.rest.rest
            remove_duplicates(lnk)
        else:
            remove_duplicates(lnk.rest)

#Interfaces 2.2
"""
Write the function is palindrome such that it works for any data type that implements the sequence interface.
Assume that the Link class has implemented the __len__ method and a __getitem__ method which takes in integers.
"""
def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence
    that reads the same forwards as backwards
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    for i in range(len(seq)//2):
        if seq[i]!=seq[len(seq)-1-i]:
            return False
    return True

#Trees
#3.1
"""
Assuming that every value in t is a number, let’s define average(t), which returns
the average of all the values in t.
"""
def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    """
    #My Solution
    sumavg,cnt=0,0
    def helper(t):
        nonlocal sumavg,cnt
        for b in t.branches:
            sumavg+=b.label
            cnt+=1
            helper(b)
    helper(t)
    sumavg+=t.label
    cnt+=1
    return sumavg/cnt
    """
    def sum_helper(t):
        total,cnt=t.label,1
        for b in t.branches:
            b_total,b_cnt=sum_helper(b)
            total+=b_total
            cnt+=b_cnt
        return total,cnt
    total,cnt=sum_helper(t)
    return total/cnt

#3.2
"""
Implement long paths, which returns a list of all paths in a tree with length at least
n. A path in a tree is a linked list of node values that starts with the root and ends
at a leaf. Each subsequent element must be from a child of the previous value’s
node. The length of a path is the number of edges in the path (i.e. one less than
the number of nodes in the path). Paths are listed in order from left to right. See
the doctests for some examples.
"""
def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    lst=[]
    if n<=0 and tree.is_leaf(): #hard
        lst.append(Link(tree.label))
    for b in tree.branches:
        for e in long_paths(b,n-1):
            lst.append(Link(tree.label,e))
    return lst

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __len__(self):
        #if self is Link.empty:
            #return 0
        #else:
        return 1+len(self.rest)

    def __getitem__(self,i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]
    
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()