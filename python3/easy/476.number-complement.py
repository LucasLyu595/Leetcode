#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        sum, tmp = 1, num
        while tmp > 0:
            tmp //= 2
            sum *= 2
        return sum - 1 - num
        
        
        
# @lc code=end

