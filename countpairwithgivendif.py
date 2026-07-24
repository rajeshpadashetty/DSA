def  count_pairs_differance(array,dif):
    s=set(array)
    count=0

    for num in arr:
        if num+dif in s:
            count +=1

    return count

arr=[1,2,5,4,3,6]
print(count_pairs_differance(arr,2))