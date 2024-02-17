#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        cpintervals = intervals + [newInterval]
        cpintervals.sort(key = lambda i : i[0])
        res = [cpintervals[0]]
        for s2, e2 in cpintervals[1:]:
            e1 = res[-1][1]
            if s2 <= e1:
                res[-1][1] = max(res[-1][1], e2)
            else:
                res.append([s2, e2])

        return res
    
# Your runtime beats 92.05 % of python3 submissions
# Your memory usage beats 88.44 % of python3 submissions (19.9 MB)
        
# @lc code=end

