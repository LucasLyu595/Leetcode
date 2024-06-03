#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for i in range(len(s)):
            if s[i] == t[p]:
                p += 1
                if p == len(t):
                    return 0
        return len(t) - p

        
# @lc code=end

