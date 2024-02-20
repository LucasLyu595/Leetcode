#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = -inf
        res = 0
        for start, end in intervals:
            if start >= prev:
                prev = end
            else:
                res += 1
        return res        
# @lc code=end

