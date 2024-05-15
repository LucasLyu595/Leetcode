#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
from collections import deque


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
 
        def isValidSafeness(minSafeness: int) -> bool:
            nonlocal n
            frontier = deque([(0, 0)])
            visited = [[0] * n for _ in range(n)]
            visited[0][0] = 1
            while frontier:
                i, j = frontier.popleft()
                if i == n - 1 and j == n - 1:
                    return True
                for d in range(4):
                    x, y = i + dir[d], j + dir[d+1]
                    if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                        visited[x][y] = 1
                        if grid[x][y] >= minSafeness:
                            frontier.append((x, y))
            return False
        low, high = 0, min(grid[0][0], grid[n-1][n-1])
        if isValidSafeness(high):
            return high
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if isValidSafeness(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans

        
# @lc code=end

