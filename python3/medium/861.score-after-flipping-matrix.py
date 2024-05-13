#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        mul, ans = 0, 0
        for j in range(n-1, -1, -1):
            tmp = 0
            for i in range(m):
                if 1 == grid[i][j]:
                    tmp += 1
            tmp = max(tmp, m-tmp)
            ans += tmp * (1 << mul)
            mul += 1
        return ans
        
# @lc code=end

