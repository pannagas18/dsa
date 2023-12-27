nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
for v in nums:
    while nums.count(v) > 2:
        nums.remove(v)
print(len(nums))
print(nums)