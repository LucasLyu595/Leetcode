#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        high = ans = cur = 0
        for num in nums:
            if num > high:
                high = num
                ans = cur = 0
            if num == high:
                cur += 1
            else:
                cur = 0
            ans = max(ans, cur)
        return ans

# @lc code=end

