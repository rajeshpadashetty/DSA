def subsetarray(arr1,arr2):
    num=arr1
    org=[]
    for num1 in arr2:
        if num1 in arr1:
            org.append(num1)
        else:
            return "no"
    if arr2==org:
        print("arr2 is subset or arr1")
        print(arr1,org)

    return -1


ar=[1,2,3,4,5,6,7,8,9,10]
ar=[1,2,3,4,5]
ar1=[]
ar2=[]
print(subsetarray(ar1,ar2))