nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
out = []
# i = 1
# while i < len(nums):   
#     val = nums[0]
#     if val == nums[i-1]:
#         out.append(f"{val}")
#     i+=1
# print(out)

# a = 0
# for i in range(len(nums)-1):
#     print(nums[i]+1 == nums[i+1])
#     # print(i)
#     if not nums[i]+1 == nums[i+1]:
#         b = i
#         print(a, b)
#         if a==b:
#             out.append(f"{nums[a]}")
#         else:
#             out.append(f"{nums[a]}->{nums[b]}")
#         a = i+1
# if nums[-1] == nums[-2] + 1:
#     print(a,b, "adsf")
#     out[-1] = f"{a}->{b+1}"
# else:
#     out.append(f"{nums[-1]}")
# print(out)

window = []
out = []
for i in range(len(nums)-1):
    print(i)
    if nums[i]+1 == nums[i+1]:
        window.append(nums[i])
    else:
        print(window)
        out.append(f"{nums[i]}")

print(out)
