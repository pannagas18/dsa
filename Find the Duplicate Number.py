nums = [1,3,1,1,1]

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        my_dict = {}
        for i,val in enumerate(nums):
            if val in my_dict:
                return val
            my_dict[val] = i

soln = Solution()
# print(soln.findDuplicate(nums))

# res = [nums.count(i) for i in nums]
# print(res)
# print(nums[max(enumerate(res), key=lambda x: x[1])[0]])

# res = map(lambda x: nums.count(x), nums)
# print(list(res))
i = 0
while i < len(nums):
    if nums.count(i) > 1:
        print(i)
    i += 1