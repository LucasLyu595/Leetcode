#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def scoreOfString(self, s: str) -> int:
        scoreMap = {v: i for i, v in enumerate(ascii_lowercase)}
        ans = 0
        for i in range(1, len(s)):
            ans += abs(scoreMap[s[i]] - scoreMap[s[i-1]])
        return ans

        
# @lc code=end

