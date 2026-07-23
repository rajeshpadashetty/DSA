
def print_pattern(n):
    for i in range(0,n):
        for j in range(i-1):
            print("*",end="")
        print()


n=int(input("enter the n value:"))
print_pattern(n)

