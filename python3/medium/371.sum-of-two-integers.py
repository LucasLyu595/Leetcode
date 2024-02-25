#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return (a & mask) if b > 0 else a
        
# @lc code=end

