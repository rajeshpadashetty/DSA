def print_pattern(n):
    for i in range(n):
        print(" "*i,end=" ")
        print("*"*(2*(n-i)-1),end=" ")
        print()

n=int(input("enter the n value:"))
print_pattern(n)
        