def armstrong(n):
    original=n
    digits=len(str(n))
    sum=0
    while n>0:

        digit=n%10
        sum=sum+digit**digits
        n=n//10
   
   
    return sum==original

n=int(input("enter a number"))

if armstrong(n):
    print("armstrong")

else:
    print("not armstrong")

 