#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans, mul = 0, 1
        for j in range(n-1, 0, -1):
            numSame = 0
            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    numSame += 1
            numSame = max(numSame, m - numSame)
            ans += numSame * mul
            mul <<= 1
        return ans + m * mul


        
# @lc code=end

