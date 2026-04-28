def fun(i,n):
 if i>n:
  return 0
 fun(i+1,n)
 print(i)

 
num=int(input("enter the number of terms:"))
print(fun(1,num))