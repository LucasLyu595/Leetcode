#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:
            return res
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    neighbors = [(x, y)]
                    while neighbors:
                        (i, j) = neighbors.pop(0)
                        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                            continue
                        grid[i][j] = "0"
                        neighbors.append((i, j-1))
                        neighbors.append((i, j+1))
                        neighbors.append((i-1, j))
                        neighbors.append((i+1, j))
        return res
        
# @lc code=end

