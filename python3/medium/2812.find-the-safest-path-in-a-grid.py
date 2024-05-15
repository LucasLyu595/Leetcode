#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dir = [0, 1, 0, -1, 0]
        n = len(grid)
        frontier = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    frontier.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        layer = 1
        while frontier:
            next = []
            while frontier:
                i, j = frontier.pop()
                for d in range(4):
                    x, y = i + dir[d], j + dir[d+1]
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == -1:
                        grid[x][y] = layer
                        next.append((x, y))
            frontier = next
            layer += 1
        frontier = [(-grid[0][0], 0, 0)]
        ans = min(grid[0][0], grid[n-1][n-1])
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        while frontier:
            safeness, i, j = heapq.heappop(frontier)
            if -safeness < ans:
                ans = -safeness
            if n - 1 == i == j:
                return ans
            for d in range(4):
                x, y = i + dir[d], j + dir[d+1]
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = 1
                    heapq.heappush(frontier, (-grid[x][y], x, y))
        return 0

        
# @lc code=end

