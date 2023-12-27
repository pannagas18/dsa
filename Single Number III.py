nums = [1,2,1,3,2,5]
# nums = [0,1]


# print(2*sum(set(nums)) - sum(nums))

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        hash_map = {num:0 for num in nums}
        for num in nums:
            hash_map[num] += 1
        for k,v in hash_map.items():
            if v == 1:
                return [k, 2*sum(set(nums))-sum(nums)-k]
print(Solution().singleNumber(nums))
