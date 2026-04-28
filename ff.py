def fun(i,n):
 if i<1:
  return 0
 print(i)
 fun(i-1,n)
 
num=int(input("enter the number of terms:"))
print(fun(num,num))