#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
import heapq


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        # Find the four smallest elements
        smallest_four = sorted(heapq.nsmallest(4, nums))

        # Find the four largest elements
        largest_four = sorted(heapq.nlargest(4, nums))

        min_diff = float("inf")
        # Four scenarios to compute the minimum difference
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff

        
        
# @lc code=end

