#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
import heapq
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        n = len(nums)
        prev = 0
        while nums:
            cur = heapq.heappop(nums)
            if prev >= n:
                return -1
            elif n <= cur:
                return n
            prev = cur
            n -= 1
        return -1

        
# @lc code=end

