n=24778
reverseno=0
while(n>1):
    ld=n%10
    reverseno=reverseno*10+ld
    n=n//10
   
print(reverseno)
