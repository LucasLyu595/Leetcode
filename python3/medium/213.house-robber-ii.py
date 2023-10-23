#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.subRob(nums[1:]), self.subRob(nums[:-1]))

    def subRob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        next_next = 0
        next = nums[-1]
        for i in range(-2, -len(nums) - 1, -1):
            current = max(next, nums[i] + next_next)
            next_next = next
            next = current
        return next
# @lc code=end

