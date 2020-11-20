def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def count_up(n):
    if n==1:
        print(1)
    else:
        count_up(n-1)
        print(n)

def sum_digits_1(n):
    ans=0
    while n//10:
        ans+=n%10
        n//=10
    ans+=n
    return ans

def sum_digits_2(n):
    if n<10:
        return n
    else:
        return sum_digits_2(n//10)+n%10