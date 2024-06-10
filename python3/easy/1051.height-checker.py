#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
import heapq


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heap = heights[:]
        heapq.heapify(heap)
        ans = 0
        for i in range(len(heights)):
            cur = heapq.heappop(heap)
            if cur != heights[i]:
                ans += 1
        return ans


        
# @lc code=end

