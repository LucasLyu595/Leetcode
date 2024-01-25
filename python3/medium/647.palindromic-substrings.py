#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        i, n = 0, len(s)
        res = 0
        while i < n:
            lower, higher = i - 1, i
            while higher < n - 1 and s[higher] == s[higher+1]:
                higher += 1
            res += (higher - lower) * (higher - lower + 1) // 2
            i = higher + 1
            higher += 1
            while lower >=0 and higher < n and s[lower] == s[higher]:
                lower -= 1
                higher += 1
                res += 1
        return res
        
        
# @lc code=end

