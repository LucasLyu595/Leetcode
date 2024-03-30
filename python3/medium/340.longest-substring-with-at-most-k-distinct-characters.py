#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        frequency = {}
        n = len(s)
        ans = 0
        left = 0
        for right in range(n):
            curFreq = frequency.get(s[right], 0) + 1
            if 1 == curFreq:
                k -= 1
            frequency[s[right]] = curFreq
            while k < 0:
                frequency[s[left]] -= 1
                if 0 == frequency[s[left]]:
                    frequency.pop(s[left])
                    k += 1
                left += 1
            if not k:
                ans = max(ans, right - left + 1)
        if k:
            ans = right - left + 1
        return ans

        
# @lc code=end

