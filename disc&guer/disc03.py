def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if m<n:
        m,n=n,m
    if n==1:
        return m
    else:
        return m+multiply(m,n-1)

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(index):
        if index==n:
            return True
        elif n%index==0 or n==1:
            return False
        else:
            return prime_helper(index+1)
    return prime_helper(2)

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(i):
        if i==0:
            return x
        else:
            return f(repeat(i-1))
    return repeat

def count_stair_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    #wrong answer
    '''
    if k==1:
        return 1
    elif n<0:
        return 0
    elif n==0:
        return 1
    else:
        return count_k(n-k,k)+count_k(n,k-1)
    '''
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        i,total=1,0
        while i<=k:
            total+=count_k(n-i,k)
            i+=1
        return total