def f(n):
    if n<=0:
        return n
    s1=f(n-2)
    s2=f(n-1)
    return s1+s2
print(f(10))