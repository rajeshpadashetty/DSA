def print_pattern(n):
    for i in range(0,n):
     for j in range(i):
        print(j,end="")
     print()

n=int(input("enter the n value: "))
print_pattern(n)