#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter([0])
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            prefix_sum %= k
            ans += counter[prefix_sum]
            counter[prefix_sum] += 1
        return ans

        
        
# @lc code=end

