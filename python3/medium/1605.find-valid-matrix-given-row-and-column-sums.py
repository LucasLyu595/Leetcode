#
# @lc app=leetcode id=1605 lang=python3
#
# [1605] Find Valid Matrix Given Row and Column Sums
#

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        ans = [[0] * m for _ in range(n)]
        rowCur = [0] * n
        colCur = [0] * m
        for i in range(min(n, m)):
            tmp = min(rowSum[i], colSum[i])
            ans[i][i] = tmp
            rowCur[i] = tmp
            colCur[i] = tmp
        for i in range(n):
            if rowCur[i] == rowSum[i]:
                continue
            diff = rowSum[i] - rowCur[i]
            j = 0
            while diff and j < m:
                tmp = min(diff, colSum[j] - colCur[j])
                ans[i][j] += tmp
                diff -= tmp
                rowCur[i] += tmp
                colCur[j] += tmp
                j += 1
        for j in range(m):
            if colCur[j] == colSum[j]:
                continue
            diff = colSum[j] - colSum[j]
            i = 0
            while diff and i < n:
                tmp = min(diff, rowSum[i] - rowCur[i])
                ans[i][j] += tmp
                diff -= tmp
                rowCur[i] += tmp
                colCur[j] += tmp
                i += 1
        return ans

# @lc code=end

