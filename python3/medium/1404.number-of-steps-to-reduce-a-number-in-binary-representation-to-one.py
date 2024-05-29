#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        target = int(s, 2)
        while target != 1:
            if target & 1:
                target += 1
            else:
                target >>= 1
            ans += 1
        return ans


# @lc code=end

