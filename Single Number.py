nums = [2,2,1]
nums = [4,1,2,1,2]
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i
soln = Solution()
# print(soln.singleNumber(nums))

########################################################
# leetcode_soln
# result = 0
# for num in nums:
#     print('result1 =', result, num)
#     result ^= num
#     print('result =', result)
# print(result)
########################################################

# res_dict = {}
# for i in nums:
#     if i in res_dict:
#         res_dict[i] += 1
#     else: 
#         res_dict[i] = 1
# print(res_dict)
# print(res_dict.get(4))

# def singleNumber1(nums):
#     dic = {}
#     for num in nums:
#         dic[num] = dic.get(num, 0)+1
#     print(dic)
#     for key, val in dic.items():
#         if val == 1:
#             return key
# singleNumber1(nums)
# def singleNumber2(self, nums):
#     res = 0
#     for num in nums:
#         res ^= num
#     return res

def singleNumber3(nums):
    return 2*sum(set(nums))-sum(nums)
# print(singleNumber3(nums))
# def singleNumber4(self, nums):
#     return reduce(lambda x, y: x ^ y, nums)
    
# def singleNumber(self, nums):
#     return reduce(operator.xor, nums)

print(2*sum(set(nums)) - sum(nums))