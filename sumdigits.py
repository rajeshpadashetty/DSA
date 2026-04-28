def sumdigits(n):
    total=0
    if n<=0:
       return total
    for i in range(n,n+1):
       total+=i
    return total
print(sumdigits(5))