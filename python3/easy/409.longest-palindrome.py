#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        hasOdd = False
        ans = 0
        for _, num in counter.items():
            if not hasOdd and num & 1:
                hasOdd = True
            ans += (num // 2 * 2)
        if hasOdd:
            ans += 1
        return ans
            

        
# @lc code=end

