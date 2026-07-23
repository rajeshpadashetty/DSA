def funrev(i, arr, n):
    if i >= n // 2:  
        return
 
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    
    funrev(i + 1, arr, n)


arr = [1, 2, 3, 4, 5]
n = len(arr)

funrev(0, arr, n)
print(arr)