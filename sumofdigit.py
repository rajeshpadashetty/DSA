def sumofdigit(n):
    if n<=10:
     return n
    count=0
    lastdigit=n%10
    remainingdigits=n//10
    count+=count
    return lastdigit + sumofdigit(remainingdigits)
    print(count)

print(sumofdigit(7777))
print(sumofdigit(88))
print(sumofdigit(9))