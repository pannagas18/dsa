nums = [1,2,7,11,15]
target = 9

# nums = [item for item in nums if item <= target]
# x = len(nums)
# y = len(nums)

# for i in range(x*y):
#     j,k = (i//y,i%y)
#     if j<k:
#         if nums[j]+nums[k] == target:
#             print(j,k)

p1 = 0
p2 = p1+1

while p1 <= len(nums):
    if not p2 >= len(nums):
        if nums[p1]+nums[p2] == target:
            print(p1,p2)
        p2+=1
    else:
        p1+=1
        p2=p1+1