#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []
        num = 0
        layer = 0
        while True:
            while j <= n - 1 - layer:
                res.append(matrix[i][j])
                j += 1
                num += 1
            if num == m * n:
                break
            j -= 1
            i += 1
            while i <= m - 1 - layer:
                res.append(matrix[i][j])
                i += 1
                num += 1
            if num == m * n:
                break
            i -= 1
            j -= 1
            while j >= layer:
                res.append(matrix[i][j])
                j -= 1
                num += 1
            if num == m * n:
                break
            j += 1
            i -= 1
            while i >= 1 + layer:
                res.append(matrix[i][j])
                i -= 1
                num += 1
            if num == m * n:
                break
            i += 1
            j += 1
            layer += 1
        return res
        
# @lc code=end

