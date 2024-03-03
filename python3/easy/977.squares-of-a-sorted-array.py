#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
import bisect
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = bisect.bisect_left(nums, 0)-1
        right = bisect.bisect_right(nums, 0, left+1, n)
        res = [0 for _ in range(left+1, right)]
        if right < n and 0 == nums[right]:
            right += 1
        while left >= 0 and right < n:
            if abs(nums[left]) < nums[right]:
                res.append(pow(nums[left], 2))
                left -= 1
            else:
                res.append(pow(nums[right], 2))
                right += 1
        for i in range(left, -1, -1):
            res.append(pow(nums[i], 2))
        for j in range(right, n):
            res.append(pow(nums[j], 2))
        return res
        
# @lc code=end

