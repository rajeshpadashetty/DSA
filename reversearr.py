def funrev(arr):
    if len(arr)==0:
        return []
    return [arr[-1]]+funrev(arr[:-1])
arr=[1,2,3,4,5]
print(funrev(arr))