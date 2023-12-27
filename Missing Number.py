nums = [3,0,1]
# nums = [9,6,4,2,3,5,7,0,1]
# nums = [0,1]


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _range = len(nums)

        for i in range(_range+1):
            if i not in nums:
                return i
soln = Solution()
# print(soln.missingNumber(nums))

# res = (lambda x: x in range(len(nums)+1))
# print(res(100))

print(sum(range(0,len(nums)+1)) - sum(nums))

n = len(nums)
print((n*(n+1))//2 - sum(nums))