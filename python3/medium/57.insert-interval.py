#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = [], []
        for a, b in intervals:
            start.append(a)
            end.append(b)
        s, e = newInterval
        s_index, e_index = bisect.bisect_left(start, s), bisect.bisect_right(end, e)

        start, interval, end = [], [], []
        if s_index < 1:
            interval.append(s)
        else:
            if intervals[s_index - 1][1] < s:
                start = intervals[:s_index]
                interval.append(s)
            else:
                start = intervals[:s_index - 1]
                interval.append(intervals[s_index - 1][0])

        if e_index == len(intervals):
            interval.append(e)
        else:
            if intervals[e_index][0] > e:
                end = intervals[e_index:]
                interval.append(e)
            else:
                end = intervals[e_index+1:]
                interval.append(intervals[e_index][1])
    
        return start + [interval] + end
        
# @lc code=end

