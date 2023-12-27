nums = [3,2,3]
# nums = [2,2,1,1,1,2,2,2,1,2,2,1,2]
nums= [10,9,9,9,10]
# maj = 0
# count = 0
# for v in nums:
#     count+=1
#     maj = max(nums.count(v), maj)
#     if maj >= int(len(nums)/2):
#         break
# print(v)
# print(count, len(nums))

# res = map(nums.count, nums)
# res = list(res)
# print(res)
# print(nums[res.index(max(res))])

# _res = [nums.count(i) for i in nums]
# print(_res)
# print(nums[_res.index(max(_res))])

# p1 = 0
# p2 = len(nums)-1
# maj = 0
# while True:
#     maj_p1 = max(nums.count(nums[p1]), maj)
#     maj_p2 = max(nums.count(nums[p2]), maj)
#     maj = max(maj_p1, maj_p2)
#     if maj >= len(nums)/2:
#         break
#     p1 += 1
#     p2 -= 1
# if maj == maj_p1:
#     print(nums[p1])
# else: print(nums[p2])

# LEETCODE SOLUTION
hm={}
ans=0
for i in nums:
    print(hm.get(i,0))
    hm[i]=hm.get(i,0)+1
    print(hm)
for i,j in hm.items():
    if len(nums)//2<j:
        ans=max(ans,i)
print(ans)

nums.sort
list_size = len(nums)
print(nums[list_size//2])