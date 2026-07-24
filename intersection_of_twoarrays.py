def intersection_array(arr1,arr2):

    set1=set(arr1)

    intersection=set()

    for num in arr2:

        if num in set1:
            intersection.add(num)
            
    return list(intersection)


array1=[1,2,3,4,5,6,7,8,9]
array2=[1,2,3,3,4,5,5.6]
print(intersection_array(array1,array2))
