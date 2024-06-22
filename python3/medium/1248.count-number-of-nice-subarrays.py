#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        numOdds = [num & 1 for num in nums]
        for i in range(1, len(nums)):
            numOdds[i] += numOdds[i-1]
        high = max(numOdds)
        if k > high:
            return 0
        ans = 0
        counter = Counter(numOdds)
        counter[0] += 1
        for i in range(high + 1):
            if i + k > high:
                break
            ans += counter[i] * counter[i+k]
        return ans


# @lc code=end

