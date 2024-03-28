#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from itertools import product
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        row = [0] * m
        col = [0] * n
        box = [0] * (n * m // 9)

        for i in range(m):
            for j in range(n):
                tmp = board[i][j]
                if '.' == tmp:
                    continue
                pos = int(tmp)
                mask = 1 << pos
                if row[i] & mask:
                    return False
                row[i] |= mask

                if col[j] & mask:
                    return False
                col[j] |= mask

                idx = (i // 3) * (m // 3) + j // 3
                if box[idx] & mask:
                    return False
                box[idx] |= mask

        return True

        
# @lc code=end

