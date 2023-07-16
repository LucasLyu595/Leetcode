#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True
        
# @lc code=end

