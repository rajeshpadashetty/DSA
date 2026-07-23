def gcd(a, b):
   
     if b==0:
         return a
     else:
        return gcd(a,a%b)    

print(gcd(10,12))