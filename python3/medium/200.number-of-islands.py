#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution: 
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    res += 1
        return res
        
# @lc code=end

