#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        ans = []
        for j in range(m):
            row = -1
            ma = 0
            for i in range(n):
                if matrix[i][j] > ma:
                    ma = matrix[i][j]
                    row = i
            if matrix[row][j] == min(matrix[row]):
                ans.append(matrix[row][j])
                return ans
        return ans
 
# @lc code=end

