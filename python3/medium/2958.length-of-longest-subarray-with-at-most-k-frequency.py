#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        start = 0
        unqualified = 0
        for num in nums:
            frequency[num] += 1
            if k + 1 == frequency[num]:
                unqualified += 1
            if unqualified:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == k:
                    unqualified -= 1
                start += 1
        return len(nums) - start

        
# @lc code=end

