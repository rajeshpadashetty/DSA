def arraynumexistornot(arr, target):

    subarray=set(arr)

    if target in subarray:
        return True
    
    else:
        return False