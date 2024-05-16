#
# @lc app=leetcode id=2061 lang=python3
#
# [2061] Number of Spaces Cleaning Robot Cleaned
#

# @lc code=start
from collections import deque


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        cap = m * n - sum(sum(line) for line in room)
        x, y = 0, 0
        dirs = [0, 1, 0, -1]
        d = 0
        ans = 0
        while room[x][y] < 3:
            if 0 == room[x][y]:
                room[x][y] = 2
                ans += 1
            else:
                room[x][y] += 1
            findNext = False
            for dd in range(4):
                attempt = (d + dd) % 4
                i, j = x + dirs[attempt], y + dirs[(attempt+1) % 4]
                if 0 <= i < m and 0 <= j < n and room[i][j] != 1:
                    x, y = i, j
                    findNext = True
                    d = attempt
                    break
            if not findNext:
                break
        return ans
            





        
# @lc code=end

