#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        taken = []
        ans = 0
        curDay = 0
        for duration, lastDay in courses:
            if duration > lastDay:
                continue
            if curDay + duration <= lastDay:
                curDay += duration
                taken.append(duration)
                ans += 1
            else:
                maxI, maxD = -1, duration
                for i, dura in enumerate(taken):
                    if dura > maxD:
                        maxI, maxD = i, dura
                if maxI != -1:
                    taken[maxI] = duration
                    curDay += duration - maxD
        return ans



        
# @lc code=end

