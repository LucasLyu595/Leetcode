#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:
            return True
        s = int(math.sqrt(c // 2)) + 1
        for l in range(s + 1):
            if l * l > c:
                break
            r = int(math.sqrt(c - l * l))
            if l * l + r * r == c:
                return True
        return False
        
# @lc code=end

