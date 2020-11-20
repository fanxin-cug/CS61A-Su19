""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(n, k):
        if k > n ** 1/2:
            return True
        if n % k == 0:
            return False
        return helper(n, k + 1)
    return helper(n, 2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a % b == 0:
        return b
    return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper(n, k):
        count = 0
        while n > 0:
            if n % 10 == k:
                count += 1
            n //= 10
        return count
    res = 0
    for i in range(1, 5):
        res += helper(n, i) * helper(n, 10 - i)
    res += helper(n, 5) * (helper(n, 5) - 1) // 2
    return res