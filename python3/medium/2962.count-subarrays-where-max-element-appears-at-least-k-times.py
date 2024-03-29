#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        indices = []
        maxNum = 0
        res = 0
        for i in range(n):
            if nums[i] > maxNum:
                maxNum = nums[i]
                indices = [i]
                res = 0
            elif nums[i] == maxNum:
                indices.append(i)
            if len(indices) >= k:
                res += indices[-k] + 1
        return res


# @lc code=end

