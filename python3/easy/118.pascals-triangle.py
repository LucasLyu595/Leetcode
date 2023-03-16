#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(res[i-1][j-1] + res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res

        
# @lc code=end

