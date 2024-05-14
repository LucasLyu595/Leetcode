#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if 0 == grid[i][j]:
                return 0
            ans = 0
            cur = grid[i][j]
            grid[i][j] = 0
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                tmp = dfs(i+x, j+y)
                ans = max(ans, tmp)
            grid[i][j] = cur
            return cur + ans
        ans = 0
        for i in range(m):
            for j in range(n):
                tmp = dfs(i, j)
                ans = max(ans, tmp)
        return ans
        

# @lc code=end

