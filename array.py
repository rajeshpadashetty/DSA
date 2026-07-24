from collections import Counter

def arrayequal(arr1,arr2):

    set1=Counter(arr1)
    set2=Counter(arr2)

    if set1==set2:
        return True
    
    else:
        return False

array1=[1,2,3,4,5,6,7,8,9,10]
array2=[1,2,3,4,5,6,7,8,9,10]
print(arrayequal(array1,array2))