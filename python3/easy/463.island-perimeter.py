#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if 0 == i:
                        ans += 2
                    elif 0 <= i - 1 and 0 == grid[i-1][j]:
                        ans += 2
                    # if m-1 == i:
                    #     ans += 1
                    # elif i + 1 <= m - 1 and 0 == grid[i+1][j]:
                    #     ans += 1
                        
                    if 0 == j:
                        ans += 2
                    elif 0 <= j - 1 and 0 == grid[i][j-1]:
                        ans += 2
                    # if n-1 == j:
                    #     ans += 1
                    # elif j + 1 <= n - 1 and 0 == grid[i][j+1]:
                    #     ans += 1
        return ans

        
# @lc code=end

