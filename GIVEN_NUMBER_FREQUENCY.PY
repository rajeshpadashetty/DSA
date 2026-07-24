from collections import Counter
def givennumber_frequency(arr ,target):
    count =Counter(arr)
    return count[target]

num=[1,2,3,4,5,3,5,4,3,4,5,3,4,4]
print(givennumber_frequency(num,4))
