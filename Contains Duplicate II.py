nums = [1,2,3,1]
k = 3
# nums = [1,0,1,1]
# k = 1

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        _dict = dict()

        for i, val in enumerate(nums):
            # if val not in _dict:
            # print(_dict)
            if val in _dict:
                # print(i, val, _dict[val])
                # print(i - _dict[val])
                if abs(i - _dict[val]) <= k:
                    return True
            _dict[val] = i
        return False
soln = Solution()
print(soln.containsNearbyDuplicate(nums, k))