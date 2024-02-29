#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if 0 == matrix[i][j]:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        
        
# @lc code=end

