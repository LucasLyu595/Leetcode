#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        mi, ma = min(nums), max(nums)
        counter = [0] * (ma - mi + 1)
        for num in nums:
            counter[num - mi] += 1
        ans = 0
        carry = 0
        for count in counter:
            carry += count
            if carry:
                carry -= 1
            ans += carry
        ans += (carry - 1) * carry // 2
        return ans
        
# @lc code=end

