#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        for i in range(len(s)-1, 0, -1):
            num = int(s[i])
            if (num + carry) & 1 == 1:
                carry += 1
                ans += 1
            carry = (num + carry) >> 1
            ans += 1
        if carry == 1:
            ans += 1
        return ans

# @lc code=end

