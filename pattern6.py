def print_pattern(n):
    for i in range(n):
        print(" "*(n-i-1), end=" ")
        print("*"*(2*i+1))
    for i in range(n):
        print(" "*i,end=" ")
        print("*"*(2*(n-i)-1))
    

n=int(input("enter the n value:"))
print_pattern(n)
        