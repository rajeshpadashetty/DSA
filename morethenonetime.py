from collections import Counter
def moreone(arr):
    set1=Counter(arr)
    for key, value in set1.items():
        if value>1:
            print(key)

arr=[1,2,3,3,4,2,4,5,5]
print(moreone(arr))

