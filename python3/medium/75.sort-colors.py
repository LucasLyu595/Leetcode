#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        p = 0
        i = 0
        while i < len(nums):
            while counter[p]:
                nums[i] = p
                counter[p] -= 1
                i += 1
            p += 1
            

        
# @lc code=end

