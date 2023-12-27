nums = [3,2,2,3]
val = 3
k = 0
while True:
    if not val in nums:
        break
    nums.remove(val)
k = (len(nums))
print(k)

while nums.count(val) != 0:
    nums.remove(val)
print(nums)