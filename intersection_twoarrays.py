from collections import Counter

def intersection(arr1,arr2):
   
   count=Counter(arr1)

   intersection=[]

   for num in arr2:
      
      if count[num]>0:
         
         intersection.append(num)
         count[num]-=1

   return intersection 


array1=[1,2,3,4,5,6,7,8,9,0]

array2=[2,4,3,5,6,8,7,9,0]

print(intersection(array1,array2))
    
