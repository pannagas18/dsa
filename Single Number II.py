nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2

        ####### EXTERNAL #######
        # hash_map = {num:0 for num in nums}
        # for num in nums:
        #     hash_map[num]+=1
        # for key, value in hash_map.items():
        #     if value==1:
        #         return key
print(Solution().singleNumber(nums))
