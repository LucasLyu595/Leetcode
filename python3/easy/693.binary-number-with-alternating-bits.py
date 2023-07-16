#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return all(bits[i] != bits[i+1]
                   for i in range(len(bits) - 1))
        
# @lc code=end

