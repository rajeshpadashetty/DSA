def two_pair_sum(nums,target):
    two_sum=set()

    for num in nums:
        diff_num=target-num

        if diff_num in two_sum:
           print(f"pair found:{num} and {diff_num}")
           return True

        two_sum.add(num)
    return False
      