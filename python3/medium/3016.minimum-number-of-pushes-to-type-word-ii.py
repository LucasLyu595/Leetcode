#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        hit = 1
        num = 8
        ans = 0
        for count in sorted(counter.values(), key=lambda x: -x):
            num -= 1
            if num < 0:
                num = 7
                hit += 1
            ans += count * hit
        return ans
        
# @lc code=end

