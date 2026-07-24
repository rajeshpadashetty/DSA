def commonelement(arr1,arr2,arr3):
    common=set(arr1)&set(arr2)&set(arr3)
    print(list(common))

array1=[1,2,3,4,5]
array2=[1,2,5,3,8,7]
array3=[1,2,3,4,5,6,7,8]
commonelement(array1,array2,array3)



