arr=[1,2,2,1,3,4,3,2,1]
fre={}

for num in arr:
     if num in fre:
        fre[num]+=1
     else:
         fre[num]=1
    
print(fre)
