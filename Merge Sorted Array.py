# # NOT COMPLETED

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# while n > 0:
#     print(m, n)
#     if m <= 0 or nums2[n-1] >= nums1[m-1]:  
#         nums1[m+n-1] = nums2[n-1]
#         n -= 1
#     else:
#         nums1[m+n-1] = nums1[m-1]
#         m -= 1

# print(nums1)
# # for i in range(len(nums1)):
# #     if i >= m:
# #         nums1[i] = nums2[n-1]
# #         n -= 1

# # nums1.sort()
# # print(nums1)


# ##########################################
# # nums1 = nums1[:m]
# # print(nums1)
# # nums2 = nums2[:n]
# # i = 0
# # for v in nums2:
# #     print("i = ", i)
# #     print("v = ", v, "nums1[i] = ", nums1[i])
# #     if v >= nums1[i]:
# #         nums1.insert(i+1, v)
# #         i += 2
# #         print(nums1)
# #     else: i+=1
# ##########################################



my_list = [1,2,3,4,5]

p1 = 0
p2 = len(my_list)-1

while p1 < p2:
    temp = my_list[p1] #1
    my_list[p1] = my_list[p2] #[5,2,3,4,5]
    my_list[p2] = temp
    p1+=1
    p2-=1
    print(p1,p2)

print(my_list)
