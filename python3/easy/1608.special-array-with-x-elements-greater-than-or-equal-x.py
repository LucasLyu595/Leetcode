#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
import bisect


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1, n+1):
            k = bisect.bisect_left(nums, i)
            if k + i == n:
                return i
        return -1
        
# @lc code=end

