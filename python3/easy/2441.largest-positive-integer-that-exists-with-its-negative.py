#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
from collections import Counter
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = -1
        for k in counter:
            if k < 0:
                continue
            if counter[-k] > 0 and k > ans:
                ans = k
        return ans


        
# @lc code=end

