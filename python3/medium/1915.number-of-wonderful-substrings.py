#
# @lc app=leetcode id=1915 lang=python3
#
# [1915] Number of Wonderful Substrings
#

# @lc code=start
from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        maskMap = Counter()
        ans = 0
        base = ord('a')
        numLetters = 10
        numOdd = 0
        for c in word:
            pos = (1 << (ord(c) - base))
            mask ^= pos
            if mask & pos:
                numOdd += 1
            else:
                numOdd -= 1
            diff = 1
            for _ in range(numLetters):
                ans += maskMap[mask ^ diff]
                diff <<= 1
            ans += maskMap[mask]
            maskMap[mask] += 1
            if numOdd < 2:
                ans += 1
        return ans



# @lc code=end


