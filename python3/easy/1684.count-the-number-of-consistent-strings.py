#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        def isConsistent(word: str) -> bool:
            for c in word:
                if c in allowed_set:
                    continue
                return False
            return True

        return sum(1 if isConsistent(word) else 0 for word in words)
        
# @lc code=end

