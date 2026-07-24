def  two_sum_hash(nums,target):
    two_sums={}

    for i,num in enumerate(nums):
        sum_number=target-num

        if sum_number in two_sums:
           return [two_sums[sum_number], i]
        
        two_sums[num]=i
        
    return []


n=[10,20,30,40,50]
target=50
print(two_sum_hash(n,int(target)))