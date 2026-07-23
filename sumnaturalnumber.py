def sumnatnum(n):
    if n==0:
        return 0
    return n+sumnatnum(n-1)

print(sumnatnum(6))