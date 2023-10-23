#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current = next_next = 0
        next = nums[-1]
        for i in range(-2, -len(nums) - 1, -1):
            current = max(next, nums[i] + next_next)
            next_next = next
            next = current
        return next
        
# @lc code=end

