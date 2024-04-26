#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if 1 == m:
            return min(grid[0])

        def backtrace(prefixSum: int, prevCol: int, row: int) -> int:
            nonlocal m, n
            if row == m:
                return prefixSum
            minSum = prefixSum + 100
            for col in range(n):
                if col == prevCol:
                    continue
                prefixSum += grid[row][col]
                ans = backtrace(prefixSum, col, row+1)
                if ans < minSum:
                    minSum = ans
                prefixSum -= grid[row][col]
            return minSum
        return min([backtrace(grid[0][i], i, 1) for i in range(n)])
        
# @lc code=end

