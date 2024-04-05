#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        s = [c for c in s]
        end = 0
        for i in range(len(s)):
            if end > 0 and abs(ord(s[i]) - ord(s[end-1])) == 32:
                end -= 1
            else:
                s[end] = s[i]
                end += 1
        return "".join(s[:end])

        
# @lc code=end

