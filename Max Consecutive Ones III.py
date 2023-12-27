# NOT COMPLETED

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
nums = [0,0,0,1]
k = 4

# len_zero = 0
# i = 0
# index = 0
# max_l = 0
# while i < len(nums):
#     print(index, i)
#     if nums[index:i+1][-1] == 0:
#         len_zero+=1
#         # print("increasing", len_zero)
#     if len_zero == k:
#         print("res", nums[index:i+1])
#         max_l = max(max_l, len(nums[index:i+1]))
#         print(max_l)
#         len_zero = 0
#         index += 1
#         i = index
#     else: i += 1
# print(max_l)

for i in range(len(nums)):
    if 0 < nums[:i].count(0) <= k:
        # print(nums[:i])
        sliding_win_l = len(nums[:i])
print(sliding_win_l)

# for i in range((len(nums)-sliding_win_l)+1):
#     print(nums[i:i+sliding_win_l])
#     if nums[i:i+sliding_win_l].count(0) <= k:
#         max_l = len(nums[i:i+sliding_win_l])
#     else: sliding_win_l += 1
# print(max_l)
i = 0
while i <= (len(nums)-sliding_win_l)+1:
    print(i)
    print(nums[i:i+sliding_win_l])
    if nums[i:i+sliding_win_l].count(0) <= k:
        max_l = len(nums[i:i+sliding_win_l])
    sliding_win_l += 1
    print("adsf", (len(nums)-sliding_win_l)+1)
    i += 1
    
print(max_l)