#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            char = s[i]
            while i <= j and char == s[i]:
                i += 1
            while i <= j and char == s[j]:
                j -= 1
        if i > j:
            return 0
        return j - i + 1
        
# @lc code=end

