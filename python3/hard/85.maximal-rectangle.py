#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            tmp = 0
            for j in range(n):
                if "1" == matrix[i][j]:
                    tmp += 1
                    matrix[i][j] = tmp
                else:
                    tmp = 0
                    matrix[i][j] = 0
        ans = 0
        for j in range(n):
            counter = [0] * n
            max_width = 0
            for i in range(m):
                tmp = matrix[i][j]
                for k in range(tmp):
                    counter[k] += 1
                if tmp < max_width:
                    for k in range(tmp, max_width):
                        ans = max(ans, (k+1) * counter[k])
                        counter[k] = 0
                    max_width = tmp
                max_width = max(max_width, tmp)
            for k in range(max_width):
                ans = max(ans, (k+1) * counter[k])
        return ans
                

        
# @lc code=end

