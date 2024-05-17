#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ascii = [0] * 123
        for ch in s:
            i = ord(ch)
            ascii[i] = max(ascii[i - k:i + k + 1]) + 1

        return max(ascii)
        
# @lc code=end

