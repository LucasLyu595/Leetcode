#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        curr = 0
        while curr <= right:
            while left <= right and 0 == nums[left]:
                left += 1
            while left <= right and 2 == nums[right]:
                right -= 1
            if curr < left:
                curr = left
            if curr > right:
                break
            if 0 == nums[curr]:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif 2 == nums[curr]:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1

        
# @lc code=end

