#
# @lc app=leetcode id=2743 lang=python3
#
# [2743] Count Substrings Without Repeating Character
#

# @lc code=start
from collections import Counter


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        counter = Counter()
        ans = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            counter[char] += 1
            while counter[char] > 1:
                counter[s[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans
        
# @lc code=end

