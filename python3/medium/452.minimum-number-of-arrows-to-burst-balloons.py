#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda i: i[1])
        res, last = 0, float('-inf')
        for start, end in points:
            if last < start:
                res += 1
                last = end
        return res 
        
# @lc code=end

