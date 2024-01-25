#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        one = two = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one
            two_digit = int(s[i-1: i+1])
            if 10 <= two_digit <=26:
                current += two
            two = one
            one = current
        return one
    
# @lc code=end

