nums = [0,1,0,3,12]
nums = [0,0,1]

p1 = 0

for i, v in enumerate(nums):
    if nums[p1] == 0:
        print(p1)
        item = nums.pop(p1)
        nums.append(item)
    else:
        p1 += 1
print(nums)