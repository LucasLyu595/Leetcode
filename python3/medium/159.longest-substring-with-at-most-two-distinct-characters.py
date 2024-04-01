#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lastMap = {}
        ans = 0
        left = 0
        numChar = 2
        for right in range(len(s)):
            lastMap[s[right]] = right
            while numChar < len(lastMap):
                idx = min(lastMap.values())
                lastMap.pop(s[idx])
                left = idx + 1
            ans = max(ans, right - left + 1)
        return ans

        
# @lc code=end

