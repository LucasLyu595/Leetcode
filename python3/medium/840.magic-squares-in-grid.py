#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
TOTAL = 15
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0
        def isValid(x: int, y: int) -> bool:
            nonlocal n, m
            map = [0, grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1], grid[x][y-1], 5, grid[x][y+1], grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1]]
            for i in range(1, 10):
                if 0 < map[i] < 10:
                    continue
                return False
            if map[2] + map[8] != 10:
                return False
            if map[4] + map[6] != 10:
                return False
            if map[1] + map[9] != 10:
                return False
            if map[3] + map[7] != 10:
                return False
            if sum(grid[x-1][y-1:y+2]) != 15:
                return False
            if sum(grid[x+1][y-1:y+2]) != 15:
                return False
            if map[4] + map[7] != map[2] + map[3]:
                return False
            if len(set(grid[x-1][y-1:y+2])) != 3:
                return False
            return True
        return sum(1 for i in range(1, n-1) for j in range(1, m-1) if 5 == grid[i][j] and isValid(i, j))

# @lc code=end

