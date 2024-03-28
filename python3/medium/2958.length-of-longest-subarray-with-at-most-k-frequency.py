#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        target = 0
        left = 0
        counter[nums[0]] = 1
        res = 0
        for right, num in enumerate(nums):
            while not target:
                counter[nums[left]] -= 1
                if counter.get(nums[left]) <= k:
                    target = 0
                left += 1
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > k:
                target = num
                res = max(res, right - left)
        return res


        
# @lc code=end

