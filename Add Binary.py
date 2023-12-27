a = "11"
b = "1"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, base=2) + int(b,base=2))[2:]
soln = Solution()
print(soln.addBinary(a,b))
