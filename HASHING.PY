def hash(n,arr):
    count=0
    for i in arr:
        if i==n:
            count+=1
    return count
arr=[1,2,4,5,1,3,1,3,14,1,3,5,4,3,5,4,3,5,]
n=int(input("enter the number to search for hashing:"))
print(hash(n,arr))