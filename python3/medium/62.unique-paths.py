#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] + [0] * (n-1)
        
        for _ in range(m):
            for j in range (1, n):
                dp[j] += dp[j-1]
        
        return dp[-1]
        
# @lc code=end

