digits = [1,2,3]
# digits = [f'{i}' for i in digits]

# res = [i for i in str(int(''.join(digits)) + 1)]
# print(res)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]

        res = [int(i) for i in str(int(''.join(digits)) + 1)]
        return res
ans = Solution()
print(ans.plusOne(digits))