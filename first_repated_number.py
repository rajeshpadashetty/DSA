def first_seen_number(nums):
    first_number=set()

    for num in nums:
     if num in first_number:
          return num
    
     first_number.add(num)
    return -1


digits=[1,2,4,5,6,4,6,3,2]
nin=[]
print(first_seen_number(nin))