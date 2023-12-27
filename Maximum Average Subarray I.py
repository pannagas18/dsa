nums = [1,12,-5,-6,50,3]
# nums = [-1,-3,-4,-5,-6,-7]
k = 4
# res = (float(sum(nums[:k]))/k)
# for i in range((len(nums)-k)+1):
#     if (float(sum(nums[i:i+k]))/k)>res:
#         res = (float(sum(nums[i:i+k]))/k)
# print(res)

# res = (float('-inf'))
res = float(sum(nums[:k]))
for i in range((len(nums)-k)+1):
    output = float(sum(nums[i:i+k]))
    res = max(output, res)
print(res/k)