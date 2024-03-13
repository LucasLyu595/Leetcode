#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.floor(math.sqrt((pow(n, 2) + n )// 2))
        if 2 * pow(x, 2) == pow(n, 2) + n:
            return x
        return -1
        
# @lc code=end

