#1.6
"""
Consider an insect in an M by N grid. The insect starts at the bottom left corner,
(0, 0), and wants to end up at the top right corner (M-1, N-1). The insect is only
capable of moving right or up. Write a function paths that takes a grid length and
width and returns the number of different paths the insect can take from the start
to the goal. (There is a closed-form solution to this problem, but try to answer it
procedurally using recursion.)
"""
def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(117, 1)
    1
    """
    if m==1 or n==1:
        return 1
    else:
        return paths(m-1,n)+paths(m,n-1)

#1.7
"""
Write a procedure merge(s1, s2) which takes two sorted (smallest value first) lists
and returns a single list with all of the elements of the two lists, in ascending order.
Use recursion.
Hint: If you can figure out which list has the smallest element out of both, then we
know that the resulting merged list will have that smallest element, followed by the
merge of the two lists with the smallest item removed. Don’t forget to handle the
case where one list is empty!
"""
def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if len(s1)==0:
        return s2
    elif len(s2)==0:
        return s1
    else:
        if s1[0]<s2[0]:
            return [s1[0]]+merge(s1[1:],s2)
        else:
            return [s2[0]]+merge(s1,s2[1:])

#1.8
#hard
def mario_number(level):
    """
    Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.
    >>> mario_number(' P P ') # jump, jump
    1
    >>> mario_number(' P P  ') # jump, jump, step
    1
    >>> mario_number('  P P ') # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    """
    """
    if 'PP' in level:
        return 0
    elif len(level)==0 or level[-1]=='P':
        return 0
    elif len(level) <= 2:
        return 1
    #elif level==' P ':
        #return 1
    #elif level=='  ':
        #return 1
    else:
        return mario_number(level[:-2])+mario_number(level[:-1])
    """
    if len(level) == 0 or level[0] == 'P':
        return 0
    elif len(level) <= 2:
        return 1
    else:
        return mario_number(level[1:]) + mario_number(level[2:])
    
#2.6
"""
Write a function that takes in a function cond and a number n and prints numbers
from 1 to n where calling cond on that number returns True.
"""
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i=1
    while i<=n:
        if cond(i):
            print(i)
        i+=1

#2.7
"""
Write a function similar to keep_ints like before, but now it takes in a number n
and returns a function that has one parameter cond. The returned function prints
out numbers from 1 to n where calling cond on that number returns True.
"""
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def f(cond):
        i=1
        while i<=n:
            if cond(i):
                print(i)
            i+=1
    return f
    