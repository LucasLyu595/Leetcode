#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#

# @lc code=start
class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join([c for c in list(s) if c not in ['a', 'e', 'i', 'o', 'u']])
        
# @lc code=end

