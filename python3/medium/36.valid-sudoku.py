#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from itertools import product
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            tmp = set()
            for number in line:
                if '.' == number:
                    continue
                if number in tmp:
                    return False
                tmp.add(number)
        for i in range(9):
            tmp = set()
            for j in range(9):
                local = board[j][i]
                if '.' == local:
                    continue
                if local in tmp:
                    return False
                tmp.add(local)
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                tmp = set()
                for x, y in product([-1,0,1], [-1,0,1]):
                    local = board[i+x][j+y]
                    if '.' == local:
                        continue
                    if local in tmp:
                        return False
                    tmp.add(local)
        return True


        
# @lc code=end

