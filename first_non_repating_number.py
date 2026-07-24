from collections import Counter
def first_non_repeating_number(nums):
    count=Counter(nums)

    for num in nums:
        if count[num]==1:
            return num

    return None


my_list=[1,2,3,1,3,4,5,4,5,2,6,7,8,7,8,9,9]
print(first_non_repeating_number(my_list))

