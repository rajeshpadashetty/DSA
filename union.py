def union(arr1,arr2):
    unin=set(arr1)
    matrix1=[]
    for num in arr2:
       unin.add(num)
    print(unin)

ar1=[1,2,3,4,5,6,7]
ar2=[2,1,5,5,6,7,3]
union(ar1,ar2)
