#
# @lc app=leetcode id=1229 lang=python3
#
# [1229] Meeting Scheduler
#

# @lc code=start
import heapq


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        def processSlots(slots: List[List[int]]) -> List[int]:
            nonlocal duration
            ans = []
            for s, e in slots:
                if e - s < duration:
                    continue
                heapq.heappush(ans, (s, e))
            return ans
        
        heap1, heap2 = processSlots(slots1), processSlots(slots2)
        while heap1 and heap2:
            if heap1[0][1] <= heap2[0][0]:
                heapq.heappop(heap1)
            elif heap1[0][0] >= heap2[0][1]:
                heapq.heappop(heap2)
            else:
                start = max(heap1[0][0], heap2[0][0])
                end = start + duration
                if end <= min(heap1[0][1], heap2[0][1]):
                    return [start, end]
                else:
                    if heap1[0][1] > heap2[0][1]:
                        heapq.heappop(heap2)
                    else:
                        heapq.heappop(heap1)
        return []


        
# @lc code=end

