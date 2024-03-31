#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        left, right = 0, 0
        ans = 0
        lastMin, lastMax = -1, -1
        while right < n:
            if nums[right] < minK or nums[right] > maxK:
                right += 1
                left = right
                lastMin, lastMax = -1, -1
                continue
            if minK == nums[right]:
                lastMin = right
            if maxK == nums[right]:
                lastMax = right
            if -1 != lastMin and -1 != lastMax:
                ans += min(lastMin, lastMax) - left + 1
            right += 1
        return ans



        
# @lc code=end

