# TRY TO IMPROVE

nums = [1,2,3,4,5,6,7]
k = 3
# nums = [1]
# k = 0
# nums = [1,2]
# k = 3
#########################################################################
# SOLUTION 1
# while k>0:
#     temp = nums[-1]
#     nums.insert(0, temp)
#     nums.pop(-1)
#     k -= 1
# print(nums)
#########################################################################

# SOLUTION 2
if len(nums) == 1 or k == 0:
    print(nums) # return

if k>=len(nums):
    while k>0:
        temp = nums[-1]
        nums.insert(0, temp)
        nums.pop(-1)
        k -= 1
    print(nums)
else:
    nums[0:0] = nums[-k:]
    print(nums)
    for i in range(k,0,-1):
        nums.pop(-i)
    print(nums)

#########################################################################
