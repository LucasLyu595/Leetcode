#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

# @lc code=start
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        taken = [0]
        curDay = 0
        for duration, lastDay in courses:
            if duration > lastDay:
                continue
            if curDay + duration <= lastDay:
                curDay += duration
                heapq.heappush(taken, -duration)
            else:
                maxD = heapq.heappushpop(taken, -duration)
                curDay += duration + maxD
        return len(taken) - 1



        
# @lc code=end

