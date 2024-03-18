#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda i: i[0])
        prev = points[0][1]
        res = 0
        for start, end in points[1:]:
            if prev >= start:
                prev = min(prev, end)
            else:
                res += 1
                prev = end
        return res + 1
        
# @lc code=end

