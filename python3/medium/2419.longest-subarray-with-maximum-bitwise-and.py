#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        high = max(nums)
        left = 0
        ans = 1
        for right in range(len(nums)):
            if nums[right] != high:
                left = right + 1
            ans = max(ans, right - left + 1)
        return ans

# @lc code=end

