#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0] = [1 for _ in range(m)]
        for j in range(n):
            dp[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n - 1][m - 1]
        
# @lc code=end

