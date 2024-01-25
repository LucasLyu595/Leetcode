#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        num = len(s)
        def isSubPal(i: int, j: int) -> int:
            if i < 0 or j >= num: return 0
            if s[i] != s[j]: return 0
            return 1 + isSubPal(i-1, j+1)
        
        odd = sum([isSubPal(i, i) for i in range(num)])
        even = sum([isSubPal(i, i+1) for i in range(num-1)])
        return odd + even
        
        
# @lc code=end

