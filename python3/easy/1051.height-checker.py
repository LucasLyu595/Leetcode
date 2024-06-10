#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
from collections import Counter


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = Counter(heights)
        mi, ma = min(heights), max(heights)
        i = 0
        ans = 0
        for val in range(mi, ma+1):
            while counter[val] > 0:
                if heights[i] != val:
                    ans += 1
                i += 1
                counter[val] -= 1
        return ans



        
# @lc code=end

