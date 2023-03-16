#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        length = len(nums)
        if length == 1: return
        for i in range(length):
            if nums[i] == 0:
                continue
            if i != pointer:
                nums[pointer] = nums[i]
            pointer += 1
        for i in range(pointer, length):
            nums[i] = 0

        
# @lc code=end

