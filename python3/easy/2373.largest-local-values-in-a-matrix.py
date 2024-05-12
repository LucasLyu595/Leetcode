#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = max(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3])
        return ans
        
# @lc code=end

