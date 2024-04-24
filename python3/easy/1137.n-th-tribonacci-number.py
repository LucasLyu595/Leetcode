#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if 0 == n:
            return 0
        if 1 == n or 2 == n:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
# @lc code=end

