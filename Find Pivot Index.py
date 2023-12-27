nums = [1,7,3,6,5,6]
nums = [2,1,-1]
nums = [-1,1,10]
nums = [-1,-1,0,0,-1,-1]
nums = [-1,-1,1,1,0,0]

for i in range(len(nums)):
    if sum(nums[:i]) == sum(nums[i+1:]):
        print(i)

print(-1)