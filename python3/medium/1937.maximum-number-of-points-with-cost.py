#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        prev, curr = [0] * n, [0] * n
        for row in points:
            running_max = 0
            for col in range(n):
                running_max = max(running_max - 1, prev[col])
                curr[col] = running_max

            running_max = 0
            for col in range(n - 1, -1, -1):
                running_max = max(running_max - 1, prev[col])
                curr[col] = max(running_max, curr[col]) + row[col]

            prev = curr.copy()
        return max(prev)
        
# @lc code=end

