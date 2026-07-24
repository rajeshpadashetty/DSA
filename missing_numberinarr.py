def missing_number_in_array(arr):
    miss=set(arr)
    for num in range(1,len(arr)+1):
        if num not in miss:
            return num
    return "there is no missing number in the array"


num=[1,2,3,4,5,6,7,8,9,10]
print(missing_number_in_array(num))