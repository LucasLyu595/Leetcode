#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        possibleIndices = [-1]

        for i in range(len(s)):
            for possibleIndex in reversed(possibleIndices):

                if s[possibleIndex+1:i+1] in wordSet:
                    possibleIndices.append(i)
                    break
        
        if possibleIndices[-1] == len(s) - 1:
            return True
        else:
            return False

        
# @lc code=end

