def print_pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
          print(j,end="")
        print()

n=int(input("enter the n value:"))
print_pattern(n)
        