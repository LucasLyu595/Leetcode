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
        for i in range(n):
            num = target - numbers[i]
            idx = bisect.bisect_left(numbers, num)
            if idx < n and num == numbers[idx] and i != idx:
                return sorted([i+1, idx+1])
        
# @lc code=end

