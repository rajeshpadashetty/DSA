def find_max(arr):
    if len(arr)==1:
        return arr[0]
    
    max_of_rest=find_max(arr[1:])
    

    if arr[0]>max_of_rest:
        return arr[0]
    else:
        return max_of_rest
    
print(find_max([4,9,8]))