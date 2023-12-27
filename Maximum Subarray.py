# TLE, 200 / 210 testcases passed

nums = [-2,1,-3,4,-1,2,1,-5,4]

# nums = [1]

# nums = [5,4,-1,7,8]
# while sliding_win_len < len(nums):
#     for i in nums:
#         print(nums[:sliding_win_len])
#         res = max(res, (sum(nums[:sliding_win_len])))
#     sliding_win_len += 1

# print(res)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sliding_win_len = 1
        # res = float('-inf')
        res = 0
        def get_max_of_sliding_win(nums, sliding_win_len):
            output = 0
            for i in range(len(nums)+1-sliding_win_len):
                output = max(output, sum(nums[i:i+sliding_win_len]))
            return output

        while sliding_win_len<=len(nums):
            res = max(res, get_max_of_sliding_win(nums, sliding_win_len))
            sliding_win_len += 1
        return res
soln = Solution()
print(soln.maxSubArray(nums))