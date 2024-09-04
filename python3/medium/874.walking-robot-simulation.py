#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
from collections import defaultdict


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0
        stopX = defaultdict(set)
        for x, y in obstacles:
            stopX[x].add(y)
        x, y = 0, 0
        ans = 0
        for c in commands:
            if c < 0:
                dir += c * 2 + 3
                dir = (dir + 4) % 4
            else:
                for d in range(c):
                    nx, ny = x + dirs[dir][0], y + dirs[dir][1]
                    if nx in stopX and ny in stopX[nx]:
                        break
                    x, y = nx, ny
                dis = x * x + y * y
                ans = max(ans, dis)
        return ans

# @lc code=end

