#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        def startWith(i: int, word: str) -> bool:
            for j in range(len(word)):
                if word[j] != s[i+j]:
                    return False
            return True
            
        @lru_cache(None)
        def dp(i: int) -> bool:
            prefixLenth = []
            for word in wordDict:
                if i + len(word) <= n and startWith(i, word):
                    prefixLenth.append(len(word))
            if len(prefixLenth) == 0:
                return False
            prefixLenth.sort(reverse=True)
            for size in prefixLenth:
                if i + size == n:
                    return True
            return not all([not dp(i+size) for size in prefixLenth])
        return dp(0)
    
# Your runtime beats 86.16 % of python3 submissions
# Your memory usage beats 76.94 % of python3 submissions (16.7 MB)

        
# @lc code=end

