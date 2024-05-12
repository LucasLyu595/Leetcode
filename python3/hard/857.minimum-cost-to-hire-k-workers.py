#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#

# @lc code=start
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wage2quality = []
        for q, w in zip(quality, wage):
            wage2quality.append((w/q, q))
        wage2quality.sort(key=lambda x: x[0])
        qualityHeap = []
        totalQuality = 0
        ans = float('inf')
        for ratio, q in wage2quality:
            totalQuality += q
            heapq.heappush(qualityHeap, -q)
            if len(qualityHeap) > k:
                quality = heapq.heappop(qualityHeap)
                totalQuality += quality
            if len(qualityHeap) == k:
                ans = min(ans, totalQuality * ratio)
        return ans

# @lc code=end

