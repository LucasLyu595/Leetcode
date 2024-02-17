#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        for num in nums[1:]:
            cur = max(num, num + cur)
            res = max(res, cur)
        return res
    

# Your runtime beats 48.73 % of python3 submissions (549 ms)
# Your memory usage beats 68.29 % of python3 submissions (31.1 MB)
        
# @lc code=end

