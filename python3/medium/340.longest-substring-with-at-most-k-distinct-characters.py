#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        frequency = {}
        ans = 0
        for i in range(len(s)):
            curFreq = frequency.get(s[i], 0) + 1
            if 1 == curFreq:
                k -= 1
            frequency[s[i]] = curFreq
            if k >= 0:
                ans += 1
            else:
                frequency[s[i-ans]] -= 1
                if not frequency[s[i-ans]]:
                    frequency.pop(s[i-ans])
                    k += 1

        return ans

        
# @lc code=end

