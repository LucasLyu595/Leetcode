#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i:int, j:int) -> int:
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left -1
        
        left = right = 0
        for i in range(len(s)):
            length = expand(i, i)
            if length > right - left + 1:
                radius = length // 2
                left = i - radius
                right = i + radius 
            length = expand(i, i+1)
            if length > right - left + 1:
                radius = length // 2 - 1
                left = i - radius
                right = i + radius + 1
        return s[left:right + 1]
        
        
# @lc code=end

