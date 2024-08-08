#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#

# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [0, 1, 0, -1, 0]
        x, y = rStart, cStart
        ans = []
        di = 0
        total = rows * cols
        step = 1
        while len(ans) < total:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= x < rows and 0 <= y < cols:
                        ans.append([x, y])
                    x += dir[di]
                    y += dir[di + 1]
                di += 1
                di %= 4
            step += 1
        return ans

# @lc code=end

