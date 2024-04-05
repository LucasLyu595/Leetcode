#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        res = deque()
        difference = ord('a') - ord('A')
        for i in range(len(s)):
            if not res:
                res.append(ord(s[i]))
                continue
            cur = ord(s[i])
            if abs(res[-1] - cur) == difference:
                res.pop()
                continue
            res.append(cur)
        return "".join(chr(i) for i in res)

        
# @lc code=end

