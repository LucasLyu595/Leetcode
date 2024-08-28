#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
dirs = [1, 0, -1, 0, 1]
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(x: int, y: int) -> bool:
            ans = True
            visited[x][y] = True
            for i in range(4):
                dx, dy = dirs[i], dirs[i + 1]
                tmp_x, tmp_y = x + dx, y + dy
                if 0 <= tmp_x < m and 0 <= tmp_y < n and not visited[tmp_x][tmp_y]:
                    if not grid2[tmp_x][tmp_y]:
                        visited[tmp_x][tmp_y] = True
                    else:
                        if not dfs(tmp_x, tmp_y):
                            ans = False
            return False if not grid1[x][y] else ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if not grid2[i][j]:
                        visited[i][j] = True
                    elif dfs(i, j):
                        ans += 1
        return ans

# @lc code=end

