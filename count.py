def countofdigit(n):
    n=abs(n)
    if n<10:
        return 1
    return 1 +countofdigit(n//10)

print(countofdigit(7777))
print(countofdigit(88))
print(countofdigit(9))
print(countofdigit(-1))