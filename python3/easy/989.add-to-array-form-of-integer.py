#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def toArrayForm(self, num: int) -> List[int]:
        res = []
        while num:
            res.append(num % 10)
            num = num // 10
        return res[::-1]
    
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = self.toArrayForm(k)
        if len(k) > len(num):
            k, num = num, k
        res = []
        carry = 0
        while k:
            tmp = k.pop() + num.pop() + carry
            res.append(tmp % 10)
            carry = tmp // 10
        while carry:
            tmp = (0 if not num else num.pop()) + carry
            res.append(tmp % 10)
            carry = tmp // 10
        return num + res[::-1]


        
# @lc code=end

