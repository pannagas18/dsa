# NOT WORKING

nums = [8,7,15,1,6,1,9,15]
indexDiff = 1
valueDiff = 3
# nums = [1,0,1,1]
# k = 1

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """

        _dict = dict()

        for i, val in enumerate(nums):
            # if val not in _dict:
            print(_dict)
            if val in _dict:
                print(i, val, _dict[val])
                print(i - _dict[val], abs(nums[i] - nums[_dict[val]]))
                if abs(i - _dict[val]) <= indexDiff and abs(nums[i] - nums[_dict[val]]) <= valueDiff:
                    return True
            _dict[val] = i
        return False
soln = Solution()
# print(soln.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))


my_dict = dict()

for i, val in enumerate(nums):
    my_dict[i] = val
print(nums)
print(my_dict)

for i, val in enumerate(nums):
    if val in my_dict:
        print(i, val, my_dict[i])
        print(val - my_dict[i], abs(nums[i] - nums[my_dict[i]]), abs(nums[val] - nums[my_dict[i]]))
        if abs(val - my_dict[i]) <= indexDiff and abs(nums[val] - nums[my_dict[i]]) <= valueDiff:
            print(True)