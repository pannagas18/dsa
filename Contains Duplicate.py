nums = [1,2,3,1]

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        #     return False
        # else:
        #     return True

soln = Solution()
print(soln.containsDuplicate(nums))