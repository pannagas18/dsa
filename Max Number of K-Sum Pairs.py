# WRONG

# nums = [1,2,3,4,3]
nums = [3,1,3,4,3]
k = 6

p1 = 0
p2 = p1+1
count = 0
while p1 <= len(nums):
    if not p2 >= len(nums):
        if nums[p1]+nums[p2] == k:
            nums.pop(p1)
            p2-=1
            nums.pop(p2)
            p1 = 0
            p2 = 0
            count+=1
        p2+=1
    else:
        p1+=1
        p2=p1+1
print(count)
    
