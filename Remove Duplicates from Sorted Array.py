nums = [1,1,2]
nums = [-1,0,0,0,0,3,3]

# print(set(nums).__len__())

k = 0
k = len(set(nums))
print(list(set(nums)))
nums[:k] = sorted(list(set(nums)))
print(nums)
print(k)