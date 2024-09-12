#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum(0 if set(word) - allowed_set else 1 for word in words)
        
# @lc code=end

