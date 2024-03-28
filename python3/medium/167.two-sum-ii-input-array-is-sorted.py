#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while target != numbers[left] + numbers[right]:
            if target > numbers[left] + numbers[right]:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]
        
# @lc code=end

