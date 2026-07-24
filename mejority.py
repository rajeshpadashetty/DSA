def mejority(arr):

    subarray=set(arr)

    for element in subarray:

        if arr.count(element)>len(arr)/2:
            return element
        
    return "there is no majority element in the array"


num=[1,2,3,3,3,3,3,3,3,3,4,5,6]
print(mejority(num))