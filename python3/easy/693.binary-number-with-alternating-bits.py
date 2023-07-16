#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mod, tmp = 1 - n % 2, n >> 1
        while tmp > 0:
            if mod != tmp % 2:
                return False
            mod = 1 - mod
            tmp >>= 1
        return True
        
# @lc code=end

