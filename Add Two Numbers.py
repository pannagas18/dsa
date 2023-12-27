# LIST NODE =>  NOT DONE (BRUH SHIT CODE)

l1 = [2,4,3]
l2 = [5,6,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        _sum = int(''.join(map(str, list(reversed(l1))))) + int(''.join(map(str, list(reversed(l2)))))
        out = []
        for i in str(_sum):
            out.insert(0, int(i))
        return out
print(Solution().addTwoNumbers(l1,l2))
        