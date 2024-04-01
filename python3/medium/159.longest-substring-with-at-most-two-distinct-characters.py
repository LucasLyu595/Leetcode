#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#

# @lc code=start
from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        frequency = Counter()
        ans = 0
        left = 0
        numChar = 2
        for right in range(n):
            frequency[right] += 1
            if 1 == frequency[right]:
                numChar -= 1
            while numChar < 0:
                frequency[left] -= 1
                if 0 == frequency[left]:
                    numChar += 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        
# @lc code=end

